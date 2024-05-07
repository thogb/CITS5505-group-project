from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


def only_anonymous(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            # return redirect(url_for('login', next=request.url))
            return redirect(url_for('main.home'))
        return f(*args, **kwargs)
    
    return decorated_function