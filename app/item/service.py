from flask import jsonify, request
from flask_login import current_user
from marshmallow import ValidationError
from app.item.dto.item_request_send_dto import ItemRequestSendDTO
from app.models import Item, ItemRequest, UserItemSaved
from app import db

class ItemService:
    def save(item_id: int, save: bool):
        item = Item.query.get(item_id)

        if not item:
            return jsonify({"message": "Item not found"}), 404
        
        if current_user.id == item.user_id:
            return jsonify({"message": "Cannot save your own item"}), 400

        saved_by_user = UserItemSaved.query.filter_by(user_id=current_user.id, item_id=item_id).first()        

        if save:
            if saved_by_user:
                return jsonify({"message": "Already saved"}), 400
            user_item_saved = UserItemSaved(user_id=current_user.id, item_id=item_id)
            db.session.add(user_item_saved)
        else:
            if not saved_by_user:
                return jsonify({"message": "Already unsaved"}), 400
            db.session.delete(saved_by_user)

        db.session.commit()

        return jsonify({"message": "Success"}), 200
    
    def send_request(item_id: int):
        try:
            data = ItemRequestSendDTO().load(request.json)
        except ValidationError as err:
            return jsonify(err.messages), 400
        
        # Check item exist
        item = Item.query.get(item_id)

        if not item:
            return jsonify({"message": "Item not found"}), 404
        
        # Check if item is owned by user
        if current_user.id == item.user_id:
            return jsonify({"message": "Cannot send request to your own item"}), 400
        
        # Check if user already made one request
        user_item_request = ItemRequest.query\
            .filter(ItemRequest.sender_id == current_user.id, ItemRequest.item_id == item_id)\
            .first()
        
        if user_item_request:
            return jsonify({"message": "User have already sent request for this item"}), 400
        
        user_item_request = ItemRequest(
            sender_id=current_user.id, 
            item_id=item_id,
            receiver_id=item.user_id,
            offer_amount=float(data['amount']),
            sender_message=data['message']
        )
        db.session.add(user_item_request)

        db.session.commit()

        return jsonify({"message": "Success"}), 200