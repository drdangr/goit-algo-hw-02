from queue import Queue

def clear_screen():
    """Очищает экран консоли."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

class ServiceCenter:
    def __init__(self):
        self.queue = Queue()
        self.request_id = 1

    def generate_request(self):
        """Генерирует новую заявку и добавляет в очередь."""
        request = f"Request-{self.request_id}"
        self.queue.put(request)
        print(f"➕ Заявка создана: {request}")
        self.request_id += 1

    def process_request(self):
        """Обрабатывает заявку, если очередь не пуста."""
        if not self.queue.empty():
            request = self.queue.get()
            print(f"🔧 Обработка заявки: {request}")
        else:
            print("⚠️ Очередь пуста — нет заявок для обработки.")

    def show_queue(self):
        """Показывает количество заявок в очереди."""
        if self.queue.empty():
            print("ℹ️ Очередь пуста.")
            return
        else:
            items = list(self.queue.queue)
            print("📝 Заявки в очереди:")
            for item in items:
                print(f" - {item}") 
            print(f"📦 Текущих заявок в очереди: {self.queue.qsize()}")
       
            


def main():
        center = ServiceCenter()

        while True:
            print("\n--- Меню ---")
            print("1 — Создать заявку")
            print("2 — Обработать заявку")
            print("3 — Показать очередь")
            print("0 — Выход")

            choice = input("Выберите действие: ")

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
                print("👋 Завершение работы.")
                break
            else:
                print("❗ Неверная команда, попробуйте снова.")


if __name__ == "__main__":
    main()
