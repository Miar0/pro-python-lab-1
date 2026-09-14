from hotel_booking.models import BookingError, Room


def get_available_rooms(rooms: list[Room]) -> list[Room]:
    """1. Список вільних номерів."""
    return [room for room in rooms if not room.is_booked]


def find_room_by_number(rooms: list[Room], room_number: int) -> Room:
    """Пошук номера за його номером."""
    for room in rooms:
        if room.room_number == room_number:
            return room
    raise BookingError(f"Номер {room_number} не знайдено.")


def book_room(rooms: list[Room], room_number: int) -> Room:
    """2. Бронювання номера."""
    room = find_room_by_number(rooms, room_number)
    if room.is_booked:
        raise BookingError(f"Номер {room_number} вже заброньовано.")
    room.is_booked = True
    return room


def cancel_booking(rooms: list[Room], room_number: int) -> Room:
    """3. Скасування бронювання."""
    room = find_room_by_number(rooms, room_number)
    if not room.is_booked:
        raise BookingError(f"Номер {room_number} не заброньовано.")
    room.is_booked = False
    return room


def find_cheapest_room(rooms: list[Room]) -> Room | None:
    """4. Пошук найдешевшого номера серед вільних."""
    available = get_available_rooms(rooms)
    if not available:
        return None
    return min(available, key=lambda room: room.price)


def calculate_potential_revenue(rooms: list[Room]) -> float:
    """5. Обчислення можливої виручки заброньованих номерів."""
    return sum(room.price for room in rooms if room.is_booked)