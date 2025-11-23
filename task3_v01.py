def is_balanced(sequence: str) -> bool:
    """
    Перевіряє симетричність розділювачів у рядку.
    Використовується стек:
    — відкриваючі дужки кладемо в стек
    — при зустрічі закриваючої — перевіряємо відповідну пару
    """
    
def is_balanced(s: str) -> bool:
    opening = "([{"
    closing = ")]}"
    stack = []

    for ch in s:
        # Якщо відкриваюча дужка — кладемо у стек
        if ch in opening:
            stack.append(ch)

        # Якщо закриваюча — перевіряємо відповідність останньої відкритої
        elif ch in closing:
            if not stack:  
                return False # нема чим закрити, несиметрично
            # Чи збігається тип дужок?
            if opening.index(stack.pop()) != closing.index(ch):
                return False #несиметрично

    # Стек має бути порожній, щоб усі дужки були закриті
    return not stack #симетрично якщо стек порожній, інакше несиметрично



def main():
    print("=== Перевірка симетрії розділювачів ===")
    print("Введіть рядок. Для виходу — 0.\n")

    while True:
        s = input(">> ")

        if s == "0":
            print("Завершення роботи.")
            break

        if is_balanced(s):
            print(f"Симетрично\n")
        else:
            print(f"Несиметрично\n")


if __name__ == "__main__":
    main()
