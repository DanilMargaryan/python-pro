# -*- coding: utf-8 -*-
import logging
import math
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
output = []

def integrate2(args):
    f, a, iteration, step = args
    return f(a + iteration * step) * step


def run_executor(executor_class, f, a, b, n_iter, n_jobs):
    step = (b - a) / n_iter
    args = [(f, a, i, step) for i in range(n_iter)]
    start_time = time.time()

    with executor_class(max_workers=n_jobs) as executor:
        results = list(executor.map(integrate2, args))

    end_time = time.time()
    logging.info(f"Время выполнения с {n_jobs} рабочими: {end_time - start_time} секунд")
    output.append(f"Время выполнения с {n_jobs} рабочими: {end_time - start_time} секунд")
    return sum(results)


if __name__ == '__main__':
    n_iter = 1000
    a = 0
    b = math.pi / 2
    cpu_num = multiprocessing.cpu_count()

    output.append("ThreadPoolExecutor:")
    for n_jobs in range(1, cpu_num * 2 + 1):
        run_executor(ThreadPoolExecutor, math.cos, a, b, n_iter, n_jobs)

    output.append("ProcessPoolExecutor:")
    for n_jobs in range(1, cpu_num * 2 + 1):
        run_executor(ProcessPoolExecutor, math.cos, a, b, n_iter, n_jobs)

    with open("artifacts/4_2.txt", "w") as file:
        file.write('\n'.join(output))