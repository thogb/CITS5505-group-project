class BasePaginationParameters:
    page: int
    per_page: int

    def __init__(self, page=1, per_page=9) -> "BasePaginationParameters":
        self.page = page
        self.per_page = per_page

    def from_request(self, request) -> None:
        try:
            self.page = int(request.args.get('page', 1))
            self.per_page = int(request.args.get('per_page', 9))
        except:
            return