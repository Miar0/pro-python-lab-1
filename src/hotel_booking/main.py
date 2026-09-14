from hotel_booking.models import BookingError, Room
from hotel_booking.services import (
    book_room,
    cancel_booking,
    calculate_potential_revenue,
    find_cheapest_room,
    get_available_rooms,
)


def create_demo_rooms() -> list[Room]:
    return [
        Room(number=101, room_type="Standard", price=60.0, is_booked=False),
        Room(number=102, room_type="Standard", price=75.0, is_booked=True),
        Room(number=201, room_type="Deluxe", price=120.0, is_booked=False),
        Room(number=202, room_type="Deluxe", price=110.0, is_booked=False),
        Room(number=301, room_type="Suite", price=250.0, is_booked=True),
    ]


def print_rooms(rooms: list[Room], title: str = "Rooms") -> None:
    print(f"\n{title}:")
    if not rooms:
        print("  (empty)")
        return
    for room in rooms:
        print(f"  {room}")


def print_menu() -> None:
    print("\n--- Hotel Booking Menu ---")
    print("1. Show all rooms")
    print("2. Show available rooms")
    print("3. Book a room")
    print("4. Cancel booking")
    print("5. Find cheapest available room")
    print("6. Show current revenue")
    print("7. Exit")


def run_menu(rooms: list[Room]) -> None:
    while True:
        print_menu()
        choice = input("Select command (1-7): ").strip()

        if choice == "1":
            print_rooms(rooms, "All Rooms")

        elif choice == "2":
            available = get_available_rooms(rooms)
            print_rooms(available, "Available Rooms")

        elif choice == "3":
            try:
                number = int(input("Enter room number to book: ").strip())
                room = book_room(rooms, number)
                print(f"Room #{room.number} successfully booked!")
            except ValueError:
                print("Error: Room number must be an integer.")
            except BookingError as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                number = int(input("Enter room number to cancel: ").strip())
                room = cancel_booking(rooms, number)
                print(f"Booking for room #{room.number} cancelled.")
            except ValueError:
                print("Error: Room number must be an integer.")
            except BookingError as e:
                print(f"Error: {e}")

        elif choice == "5":
            cheapest = find_cheapest_room(rooms)
            if cheapest:
                print(f"Cheapest room: #{cheapest.number} ({cheapest.room_type}) - ${cheapest.price:.2f}")
            else:
                print("No available rooms found.")

        elif choice == "6":
            revenue = calculate_potential_revenue(rooms)
            print(f"Current revenue from bookings: ${revenue:.2f}")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Try again.")


def main() -> None:
    rooms = create_demo_rooms()
    run_menu(rooms)


if __name__ == "__main__":
    main()