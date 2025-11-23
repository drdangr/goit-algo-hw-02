from collections import deque

def is_palindrome(text: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    — игнорирует пробелы
    — нечувствительна к регистру
    — использует двустороннюю очередь deque
    """
    # Удаляем пробелы и приводим к одному регистру
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    dq = deque(cleaned)

    # Сравниваем символы с обоих концов
    while len(dq) > 1:
        if dq.popleft() != dq.pop(): #видалим перший і останній та порівняємо
            return False # якщо не співпадають - це не палындром, повертаємо False
    return True # якщо всі співпали - це паліндром, повертаємо True


def main():

    print("=== Перевiрка строки на палiндром ===")
    print("введiть строку. Для виходу — 0.\n")

    while True:
        user_input = input(">> ")

        if user_input == "0":
            print("\n Завершення работи.")
            break

        if is_palindrome(user_input):
            print(f"✔️ '{user_input}' — палiндром.\n")
        else:
            print(f"✖️ '{user_input}' — не палiндром.\n")


if __name__ == "__main__":
    main()
