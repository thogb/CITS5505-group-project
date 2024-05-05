from .base_pagination_parameters import BasePaginationParameters

class BaseFilteringParameters(BasePaginationParameters):
    search_text: str

    def __init__(self, page=1, per_page=9, search_text=None) -> "BaseFilteringParameters":
        super().__init__(page, per_page)
        self.search_text = search_text

    def from_request(self, request) -> None:
        super().from_request(request)
        self.search_text = request.args.get('search_text', None)

    def filter_to_url_for_string(self) -> str:
        return f"search_text={self.search_text}" if self.search_text else ""