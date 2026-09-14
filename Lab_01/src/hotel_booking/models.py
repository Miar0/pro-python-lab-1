from dataclasses import dataclass


class BookingError(Exception):
    """Виняток для операцій бронювання готелю."""
    pass


@dataclass
class Room:
    """Модель кімнати готелю (Варіант 8)."""
    room_number: int
    room_type: str
    price: float
    is_booked: bool = False

    @property
    def number(self) -> int:
        """Номер кімнати."""
        return self.room_number

    @property
    def booking_status(self) -> bool:
        """Статус бронювання."""
        return self.is_booked

    @property
    def status(self) -> str:
        return "Заброньовано" if self.is_booked else "Вільний"

    def __str__(self) -> str:
        return f"Номер: {self.room_number}, Тип: {self.room_type}, Ціна: {self.price}, Статус: {self.status}"