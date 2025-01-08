#import multiprocessing
import time
from multiprocessing import Pool
#import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    tn = time.time()
    for i in filenames:
        print(i)
        read_info(i)
    te = time.time()
    print(f'Линейный процесс: {te-tn}')
    tn1 = time.time()

    with Pool(4) as p:
        p.map(read_info, filenames)
        te1 = time.time()
    print(f' Время мультипроцесса:{te1-tn1:.6f}')