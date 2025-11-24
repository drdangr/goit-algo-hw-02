import os
from queue import Queue

queue = Queue()
req_id = 1


def show_queue():
    '''Виводить поточний стан черги.'''
    if queue.empty():
        print("Черга порожня.")
    else:
        print("Заявки в черзі:")
        for item in list(queue.queue):
            print(f" • {item}")
        print(f"\nВсього: {queue.qsize()}")


def add_request():
    '''Додає нову заявку до черги.'''
    global req_id
    task = f"Request-{req_id}"
    queue.put(task) # Додаємо заявку до черги
    req_id += 1
    return task


def process_request():
    '''Обробляє (видаляє) заявку з черги.'''
    if queue.empty(): # Якщо черга порожня
        return None # Повертаємо None
    return queue.get() 


def main():
    '''Головна функція для взаємодії з користувачем.'''
    
    while True:     
        cmd = input("\nКоманди: \n1 — Додати\n2 — Обробити\n0 — Вихід\n\nВведіть команду >>> ")

        if cmd == "0":
            print("Завершення роботи.")
            break
        if cmd == "1":
            task = add_request()           
        elif cmd == "2":
            task = process_request()     
        else:
            print("Невірна команда.\n")
            continue
        
        print("=== Сервісна черга ===")
        show_queue()
        print("======================")
        


if __name__ == "__main__":
    main()
