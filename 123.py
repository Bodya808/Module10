import threading
import time


def numbers():
    for i in range(1, 6):
        print(f'Число: {i}')
        time.sleep(1)


def bukvi():
    for j in 'ABCDEFG':
        print(f'Буква: {j}')
        time.sleep(1)


thread1 = threading.Thread(target=numbers())
thread2 = threading.Thread(target=bukvi())


thread1.start()
thread2.start()


thread1.join()
thread2.join()