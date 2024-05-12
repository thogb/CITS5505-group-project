from app.models import Item
from app.shared.base_filtering_parameters import BaseFilteringParameters
# from sqlalchemy.orm import Query
from flask_sqlalchemy.query import Query

from app.utils.type_utils import str2bool

class ItemFilteringParameters(BaseFilteringParameters):
    category: int
    city: int
    min_price: float
    max_price: float
    used: bool

    def __init__(
            self, 
            page=1, 
            per_page=9, 
            search_text="", 
            category=None, 
            city=None, 
            min_price=None, 
            max_price=None, 
            used=None) -> "ItemFilteringParameters":
        super().__init__(page, per_page, search_text)
        self.category = category
        self.city = city
        self.min_price = min_price
        self.max_price = max_price
        self.used = used

    def from_request(self, request) -> "ItemFilteringParameters":
        super().from_request(request)
        try:
            self.category = int(request.args.get('category')) if request.args.get('category') is not None else None
            self.city = int(request.args.get('city')) if request.args.get('city') is not None else None
            self.min_price = float(request.args.get('min_price')) if request.args.get('min_price') is not None else None
            self.max_price = float(request.args.get('max_price')) if request.args.get('max_price') is not None else None
            self.used = str2bool(request.args.get('used')) if request.args.get('used') is not None else None
        except:
            return

    def getQuery(self, in_query: Query) -> Query:
        query = in_query
        if self.search_text and len(self.search_text) > 0:
            query = query.filter(Item.title.contains(self.search_text))
        if self.category and self.category > 0:
            query = query.filter(Item.category_id == self.category)
        if self.city and self.city > 0:
            query = query.filter(Item.city_id == self.city)
        if self.min_price and self.min_price >= 0 and (not self.max_price or self.min_price < self.max_price):
            query = query.filter(Item.price >= self.min_price)
        if self.max_price and self.max_price >= 0 and (not self.min_price or self.max_price > self.min_price):
            query = query.filter(Item.price <= self.max_price)
        if self.used is not None:
            query = query.filter(Item.used == self.used)

        return query
    
    def filter_to_url_for_string(self) -> str:
        filter_str = super().filter_to_url_for_string();
        if self.category and self.category > 0:
            filter_str += f"&category={self.category}"
        if self.city and self.city > 0:
            filter_str += f"&city={self.city}"
        if self.min_price and self.min_price > 0 and (not self.max_price or self.min_price < self.max_price):
            filter_str += f"&min_price={self.min_price}"
        if self.max_price and self.max_price > 0 and (not self.min_price or self.max_price > self.min_price):
            filter_str += f"&max_price={self.max_price}"
        if self.used is not None:
            filter_str += f"&used={self.used}"

        return filter_str.strip("&")