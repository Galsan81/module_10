import threading
import random
import time

class Bank(threading.Thread):
    def __init__(self):
        super().__init__() # цеплясь к иниту класса Thread
        self.balance = 0 # начальный баланс
        self.lock = threading.Lock() # lock становиться переменной блокирующей поток, из
                    # класса Lock из threading
    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            t = random.randint(50, 500) #закидываю в переменную t рандомное число чтобы потом использовать в принте
            self.balance += t
            print(f'Пополнение баланса на {t}, текущий баланс {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            k = random.randint(50, 500) # в переменную к закидываем рандомное число для для
                                            # дальнейшего использования
            print(f'Запрос на {k}')
            if k <= self.balance:
                self.balance -= k
                print(f'Снятие: {k}, текущий баланс: {self.balance}')
            else:
                print(' Запрос отклонён, недостаточно средств')
                self.lock.acquire #блокировка потока при недостаточном балансе
            time.sleep(0.001)
# Создаем объект класса Bank
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,)) # 2 потока один для deposit, пополнение
th2 = threading.Thread(target=Bank.take, args=(bk,)) # 2-й для take, для снятия

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

