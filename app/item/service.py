from flask import jsonify
from flask_login import current_user
from app.models import Item, UserItemSaved
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