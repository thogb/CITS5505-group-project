from app import cache, db
from app.models import Category

@cache.cached(timeout=7200, key_prefix="get_all_categories")
def getAllCategories():
    categories = db.session.query(Category).all()
    return categories

def checkIfCategoryExists(id):
    check_Data = Category.query.filter_by(id=id).first()

    return check_Data is not None