import multiprocessing
import time
from codecs import encode


def worker_a(input_queue, output_pipe):
    while True:
        if not input_queue.empty():
            msg = input_queue.get().lower()
            output_pipe.send(msg)
            time.sleep(5)


def worker_b(input_pipe, output_pipe):
    while True:
        if input_pipe.poll():
            msg = input_pipe.recv()
            encoded_msg = encode(msg, 'rot_13')
            output_pipe.send(encoded_msg)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    a_to_b, b_to_a = multiprocessing.Pipe()
    main_to_b, b_to_main = multiprocessing.Pipe()

    process_a = multiprocessing.Process(target=worker_a, args=(queue, a_to_b))
    process_b = multiprocessing.Process(target=worker_b, args=(b_to_a, b_to_main))
    process_a.start()
    process_b.start()

    try:
        with open("artifacts/4_3.txt", "w") as log_file:
            while True:
                msg = input("Введите сообщение (или 'exit' для выхода): ")
                if msg == 'exit':
                    break
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                log_file.write(f"Отправлено в {timestamp}: {msg}\n")
                queue.put(msg)
                if main_to_b.poll(10):  # Ожидание сообщения в течение 10 секунд
                    received_msg = main_to_b.recv()
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    log_file.write(f"Получено в {timestamp}: {received_msg}\n")
    finally:
        process_a.terminate()
        process_b.terminate()
