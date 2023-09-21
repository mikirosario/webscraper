from src.utils.log_config import setup_logger

logger = setup_logger(__name__)

class HackerNewsEntry:
    # Private variables
    _default_str_val = 'BAD STRING'
    _default_int_val = -1
    _title: str = _default_str_val
    _order_num: int = _default_int_val
    _comment_count: int = _default_int_val
    _points: int = _default_int_val

    # Class constructor
    def __init__(self, title: str, order_num: int, comment_count: int, points: int):
            self._title = title
            self._order_num = order_num
            self._comment_count = comment_count
            self._points = points

    # Equality operator override
    def __eq__(self, other):
        if isinstance(other, HackerNewsEntry):
            return (self.title == other.title and
                    self.order_num == other.order_num and
                    self.points == other.points and
                    self.comment_count == other.comment_count)
        return False

    # 'To String' override
    def __repr__(self):
        return f"<HackerNewsEntry(order_num={self.order_num}, title='{self.title}', comment_count={self.comment_count}, points={self.points})>"

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

    # Validation methods
    def _validate_str(self, value: str, value_name: str) -> str:
        if not isinstance(value, str):
            logger.warning(f"{value_name} must be a string.")
            return self._default_str_val
        return value

    def _validate_int(self, value: int, value_name: str) -> int:
        if not isinstance(value, int) or value < 0:
            logger.warning(f"{value_name} number must be a non-negative integer.")
            return self._default_int_val
        return value
    