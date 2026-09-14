from hotel_booking.models import BookingError, Room


def get_available_rooms(rooms: list[Room]) -> list[Room]:
    return [room for room in rooms if not room.is_booked]


def find_room_by_number(rooms: list[Room], number: int) -> Room:
    for room in rooms:
        if room.number == number:
            return room
    raise BookingError(f"Room #{number} not found.")


def book_room(rooms: list[Room], number: int) -> Room:
    room = find_room_by_number(rooms, number)
    if room.is_booked:
        raise BookingError(f"Room #{number} is already booked.")
    room.is_booked = True
    return room


def cancel_booking(rooms: list[Room], number: int) -> Room:
    room = find_room_by_number(rooms, number)
    if not room.is_booked:
        raise BookingError(f"Room #{number} is not booked.")
    room.is_booked = False
    return room


def find_cheapest_room(rooms: list[Room]) -> Room | None:
    available = get_available_rooms(rooms)
    if not available:
        return None
    return min(available, key=lambda room: room.price)


def calculate_potential_revenue(rooms: list[Room]) -> float:
    return sum(room.price for room in rooms if room.is_booked)