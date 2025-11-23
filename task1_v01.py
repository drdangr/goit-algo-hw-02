from queue import Queue

def clear_screen():
    """Очищуе консоль."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

class ServiceCenter:
    def __init__(self):
        self.queue = Queue()
        self.request_id = 1

    def generate_request(self):
        """Генерирує нову заявку та додає її до черги."""
        request = f"Request-{self.request_id}"
        self.queue.put(request)
        print(f"➕ Заявка создана: {request}")
        self.request_id += 1

    def process_request(self):
        """Обрабляє заявку з черги."""
        if not self.queue.empty():
            request = self.queue.get()
            print(f"🔧 Обработка заявки: {request}")
        else:
            print("Черга пуста, заявок для обработки нема.")

    def show_queue(self):
        """Показує поточний стан черги."""
        if self.queue.empty():
            pass
            return
        else:
            items = list(self.queue.queue)
            print("📝 Заявки в черзі:")
            for item in items:
                print(f" - {item}") 
            print(f"Поточних заявок у черзі {self.queue.qsize()}")
       
            


def main():
        center = ServiceCenter()

        while True:
            print("\n--- Меню ---")
            print("1 — Создати заявку")
            print("2 — Опрацювати заявку")
            print("3 — Показати чергу")
            print("0 — Вихід")

            choice = input("Оберіть дію: ")

            clear_screen()

            if choice == "1":
                center.generate_request()
                # показати очередь після створення заявки (необов'язково, але так краще видно зміни)
                center.show_queue() 
            elif choice == "2":
                center.process_request()
                # показати очередь після створення заявки (необов'язково, але так краще видно зміни)
                center.show_queue() 
            elif choice == "3":
                center.show_queue()
            elif choice == "0":
                print("Завершення работи.")
                break
            else:
                print("Невірна команда, спробуйте ще раз1.")


if __name__ == "__main__":
    main()
