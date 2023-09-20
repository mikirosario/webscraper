from src.utils.log_config import setup_logger

logger = setup_logger(__name__)

class HackerNewsEntry:
    # Private variables
    _title: str
    _order_num: int
    _comment_count: int
    _points: int

    # Class constructor
    def __init__(self, title: str, order_num: int, comment_count: int, points: int):
            self._title = title
            self._order_num = order_num
            self._comment_count = comment_count
            self._points = points

    # Properties
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = self._validate_str(value, "'title'")
    
    @property
    def order_num(self) -> int:
        return self._order_num

    @order_num.setter
    def order_num(self, value: int) -> None:
        self._order_num = self._validate_int(value, "'order_num'")

    @property
    def comment_count(self) -> int:
        return self._comment_count
    
    @comment_count.setter
    def comment_count(self, value: int) -> None:
        self._comment_count = self._validate_int(value, "'comment_count'")

    @property
    def points(self) -> int:
        return self._points
    
    @points.setter
    def points(self, value: int) -> None:
        self._points = self._validate_int(value, "'points'")

    # 'To String' method
    def __repr__(self):
        return f"<HackerNewsEntry(order_num={self.order_num}, title='{self.title}', comment_count={self.comment_count}, points={self.points})>"
    
    # Validation methods
    def _validate_str(self, value: str, value_name: str) -> str:
        if not isinstance(value, str):
            logger.warning(f"{value_name} must be a string.")
            return 'BAD STRING'
        return value

    def _validate_int(self, value: int, value_name: str) -> int:
        if not isinstance(value, int) or value < 0:
            logger.warning(f"{value_name} number must be a non-negative integer.")
            return -1
        return value