from threading import Thread
from time import sleep, time

class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name} на нас напали!')
        n = 100
        ts = time()
        while n > 0:
            n = n - self.power
            sleep(1)
            tn = time()
            print(f'{self.name} сражается {round(tn-ts)} дней, осталось {n} воинов \n')
        tk = time()
        print(f'{self.name} одержал победу спустя {round(tk-ts)} дней(дня)')
        return '''f'{self.name} одержал победу спустя {round(tk-tn)} дней(дня)'''''

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
