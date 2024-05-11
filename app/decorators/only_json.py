from functools import wraps
from flask import json, request

# Retrieved from https://stackoverflow.com/questions/24238743/flask-decorator-to-verify-json-and-json-schema
# Date: 07/05/2024
def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            if not request.is_json:
                raise Exception
            
            # request.json on empty payload throws errors, make sure that body 
            # is not empty before perform a json parse.
            if request is not None and len(request.get_data()) > 0:
                request.json
        except :
            # msg = "payload must be a valid json"
            msg = "content type must be application/json"
            return json.jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper