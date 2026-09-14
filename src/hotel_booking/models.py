from dataclasses import dataclass


class BookingError(Exception):
    """Виняток для помилок операцій з номерами."""
    pass


@dataclass
class Room:
    number: int
    room_type: str
    price: float
    is_booked: bool = False

    @property
    def status(self) -> str:
        return "Booked" if self.is_booked else "Available"

    def __str__(self) -> str:
        return f"Room #{self.number:<4} | Type: {self.room_type:<10} | Price: ${self.price:<7.2f} | Status: {self.status}"