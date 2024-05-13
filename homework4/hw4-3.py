import multiprocessing
import threading
import time
from codecs import encode
from datetime import datetime
import os


def log_message(log_file, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file.write(f"{timestamp} - {message}\n")
    log_file.flush()


def process_a(input_queue, output_queue):
    while True:
        message, send_time = input_queue.get()
        if message == "exit":
            output_queue.put(("exit", send_time))
            break
        output_queue.put((message.lower(), send_time))
        time.sleep(5)


def process_b(input_queue, conn):
    while True:
        message, send_time = input_queue.get()
        if message == "exit":
            conn.send(("exit", send_time, datetime.now()))
            break
        encoded_message = encode(message, 'rot_13')
        conn.send((encoded_message, send_time, datetime.now()))


def input_thread(input_queue, log_file):
    while True:
        message = input("Введите сообщение 'exit' чтобы выйти из программы: ")
        send_time = datetime.now()
        log_message(log_file, f"Отправлено: {send_time.strftime('%Y-%m-%d %H:%M:%S')} - Сообщение: {message}")
        input_queue.put((message, send_time))
        if message == "exit":
            break


def output_thread(conn, log_file):
    while True:
        encoded_message, send_time, recv_time = conn.recv()
        if encoded_message == "exit":
            break
        send_time_str = send_time.strftime('%Y-%m-%d %H:%M:%S')
        recv_time_str = recv_time.strftime('%Y-%m-%d %H:%M:%S')
        log_message(log_file, f"Получено: {recv_time_str} - Закодированное сообщение: {encoded_message}")
        print(f"{recv_time_str} - Закодированное сообщение: {encoded_message}")


if __name__ == "__main__":
    queue_a_b = multiprocessing.Queue()
    queue_main_a = multiprocessing.Queue()
    parent_conn, child_conn = multiprocessing.Pipe()

    process_a_proc = multiprocessing.Process(target=process_a, args=(queue_main_a, queue_a_b))
    process_b_proc = multiprocessing.Process(target=process_b, args=(queue_a_b, child_conn))

    process_a_proc.start()
    process_b_proc.start()

    log_file_path = os.path.join("artifacts", "4_3.txt")
    with open(log_file_path, "a") as log_file:
        input_thread_proc = threading.Thread(target=input_thread, args=(queue_main_a, log_file))
        output_thread_proc = threading.Thread(target=output_thread, args=(parent_conn, log_file))

        input_thread_proc.start()
        output_thread_proc.start()

        input_thread_proc.join()
        output_thread_proc.join()

    process_a_proc.join()
    process_b_proc.join()
