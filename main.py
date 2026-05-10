import sys


def check_greater_than_100(value):
    """
    Перевіряє, чи є число більшим за 100.

    >>> check_greater_than_100("150")
    True
    >>> check_greater_than_100("50")
    False
    >>> check_greater_than_100("abc")
    Traceback (most recent call last):
        ...
    ValueError: Введене значення не є числом.
    """
    try:
        num = float(value)
        return num > 100
    except ValueError:
        raise ValueError("Введене значення не є числом.")


def main():
    print("Програма для перевірки, чи число більше 100.")
    user_input = input("Введіть число: ")
    try:
        result = check_greater_than_100(user_input)
        if result:
            print(f"Результат: Число {user_input} більше 100.")
        else:
            print(f"Результат: Число {user_input} не більше 100.")
    except ValueError as e:
        print(f"Помилка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()