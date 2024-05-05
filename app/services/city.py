from app import cache, db
from app.models import City

@cache.cached(timeout=7200)
def getCities():
    cities = db.session.query(City).all()
    return cities

def checkIfCityExists(id):
    check_Data = City.query.filter_by(id=id).first()

    return check_Data is not None