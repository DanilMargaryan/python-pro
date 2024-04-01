import time
from threading import Thread
from multiprocessing import Process


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    fib = 35
    number = 10
    times = []

    start_time = time.time()
    for _ in range(number):
        fibonacci(fib)
    end_time = time.time()
    times.append(f"Синхронное выполнение: {end_time - start_time} сек.")

    start_time = time.time()
    threads = []
    for _ in range(number):
        thr = Thread(target=fibonacci, args=(fib,))
        threads.append(thr)
        thr.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    times.append(f"Выполнение с использованием потоков: {end_time - start_time} сек.")

    start_time = time.time()
    processes = []
    for _ in range(number):
        pr = Process(target=fibonacci, args=(fib,))
        processes.append(pr)
        pr.start()
    for process in processes:
        process.join()
    end_time = time.time()
    times.append(f"Выполнение с использованием процессов: {end_time - start_time} сек.")

    with open("artifacts/4_1.txt", "w") as file:
        file.write('\n'.join(times))
