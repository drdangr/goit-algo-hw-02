import os
from queue import Queue


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


queue = Queue()
req_id = 1


def show_queue():
    if queue.empty():
        print("Черга порожня.")
    else:
        print("Заявки в черзі:")
        for item in list(queue.queue):
            print(f" • {item}")
        print(f"\nВсього: {queue.qsize()}")


def add_request():
    global req_id
    task = f"Request-{req_id}"
    queue.put(task)
    req_id += 1
    return task


def process_request():
    if queue.empty():
        return None
    return queue.get()


def main():
    clear()

    while True:
        print("=== Сервісна черга ===")
        show_queue()

        cmd = input("\n1 — Додати\n2 — Обробити\n0 — Вихід\n\n>>> ")

        if cmd == "0":
            clear()
            print("Завершення роботи.")
            break

        clear()

        if cmd == "1":
            task = add_request()
            print(f"Додано: {task}\n")

        elif cmd == "2":
            task = process_request()
            if task:
                print(f"Обробка: {task}\n")
            else:
                print("Черга порожня — нема заявок.\n")

        else:
            print("Невірна команда.\n")


if __name__ == "__main__":
    main()
