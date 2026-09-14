from hotel_booking.models import BookingError, Room
from hotel_booking.services import (
    book_room,
    calculate_potential_revenue,
    cancel_booking,
    find_cheapest_room,
    get_available_rooms,
)


def test_get_available_rooms() -> None:
    rooms = [
        Room(number=101, room_type="Standard", price=60.0, is_booked=False),
        Room(number=102, room_type="Standard", price=75.0, is_booked=True),
    ]
    available = get_available_rooms(rooms)
    assert len(available) == 1
    assert available[0].number == 101


def test_book_room_success() -> None:
    rooms = [Room(number=101, room_type="Standard", price=60.0, is_booked=False)]
    room = book_room(rooms, 101)
    assert room.is_booked is True


def test_cancel_booking() -> None:
    rooms = [Room(number=101, room_type="Standard", price=60.0, is_booked=True)]
    room = cancel_booking(rooms, 101)
    assert room.is_booked is False


def test_find_cheapest_room() -> None:
    rooms = [
        Room(number=101, room_type="Standard", price=80.0, is_booked=False),
        Room(number=102, room_type="Standard", price=50.0, is_booked=False),
    ]
    cheapest = find_cheapest_room(rooms)
    assert cheapest is not None
    assert cheapest.number == 102


def test_calculate_potential_revenue() -> None:
    rooms = [
        Room(number=101, room_type="Standard", price=60.0, is_booked=True),
        Room(number=102, room_type="Standard", price=70.0, is_booked=True),
        Room(number=103, room_type="Standard", price=80.0, is_booked=False),
    ]
    assert calculate_potential_revenue(rooms) == 130.0