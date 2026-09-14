# Hotel Booking System

Лабораторна робота №1 з дисципліни «Професійний Python».

## Опис проєкту
Консольний застосунок для управління номерним фондом готелю (Варіант 8).  
Програма реалізує облік номерів, перегляд списку вільних місць, бронювання та скасування бронювань, пошук найдешевшого номера, а також розрахунок поточної виручки.

## Структура проєкту (src-layout)
```text
hotel_booking/
│
├── pyproject.toml
├── README.md
├── .gitignore
│
└── src/
    └── hotel_booking/
        ├── __init__.py
        ├── models.py
        ├── services.py
        └── main.py
```

- `models.py` — модель даних `Room` (`dataclass`) та власний клас винятку `BookingError`.
- `services.py` — бізнес-логіка (фільтрація вільних номерів, бронювання, скасування, пошук найдешевшого, обчислення виручки).
- `main.py` — інтерактивне консольне меню та точка входу програми.

## Вимоги
- Python 3.11+

## Встановлення та запуск

1. Створення та активація віртуального оточення:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

2. Встановлення пакета в режимі редагування (editable mode):
```bash
python -m pip install -e .
```

3. Запуск застосунку:
```bash
python -m hotel_booking.main
# або через зареєстровану команду:
hotel-booking
```

## Приклад роботи програми
```text
--- Hotel Booking Menu ---
1. Show all rooms
2. Show available rooms
3. Book a room
4. Cancel booking
5. Find cheapest available room
6. Show current revenue
7. Exit
Select command (1-7): 2

Available Rooms:
  Room #101  | Type: Standard   | Price: $60.00   | Status: Available
  Room #201  | Type: Deluxe     | Price: $120.00  | Status: Available
  Room #202  | Type: Deluxe     | Price: $110.00  | Status: Available
```

## Автор
Студент: Івасів Данило

Група: ФЕП-32С