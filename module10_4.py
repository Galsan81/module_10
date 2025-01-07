from time import sleep
from threading import Thread
import queue
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))  # Гость "кушает" случайное время

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()  # Очередь для гостей
        self.tables = tables  # Список столов

    def guest_arrival(self, guests):
        for guest in guests:
            # Пытаемся посадить каждого гостя за стол
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest  # Сажаем гостя за стол
                    guest.start()  # Начинаем "обслуживать" гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если нет свободных столов, ставим гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while True:
            all_tables_free = True  # Проверка, свободны ли все столы
            for table in self.tables:
                # Проверяем, завершил ли гость свою "работу"
                if table.guest is not None:
                    all_tables_free = False
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            if all_tables_free and self.queue.empty():
                # Если все столы свободны и очередь пуста, завершаем цикл
                break
            sleep(1)




# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(tables)

# Прием гостей
cafe.guest_arrival(guests)

# Обслуживание гостей
cafe.discuss_guests()