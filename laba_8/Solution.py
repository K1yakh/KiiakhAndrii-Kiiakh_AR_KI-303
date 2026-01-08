"""
Модуль для обчислення значення функції y = sin(x) / tan(4x).

Модуль виконує:
- обчислення математичної функції
- запис результату у текстовий файл
- запис результату у бінарний файл
- зчитування даних з текстового та бінарного файлів
"""

from math import sin, tan
import struct
import os


def solution(filename_result_txt, filename_result_bin):
    """
    Основна функція програми.

    Обчислює значення функції y = sin(x) / tan(4x),
    зберігає результат у текстовий та бінарний файли.

    Args:
        filename_result_txt (str): ім'я текстового файлу
        filename_result_bin (str): ім'я бінарного файлу
    """
    filename_result_txt = os.path.join(os.getcwd(), filename_result_txt)
    filename_result_bin = os.path.join(os.getcwd(), filename_result_bin)

    try:
        x = float(input("Функція обчислює y = sin(x) / tan(4x).\nВведіть x: "))
    except ValueError:
        print("Помилка: введено некоректне числове значення.")
        return

    try:
        y = sin(x) / tan(4 * x)
    except ZeroDivisionError:
        print("Помилка: ділення на нуль (tan(4x) = 0).")
        return

    # Запис у текстовий файл
    with open(filename_result_txt, "a", encoding="utf-8") as file:
        file.write(f"x = {x}, y = {y}\n")
        print(f"Результат записано у файл: {filename_result_txt}")

    # Запис у бінарний файл
    with open(filename_result_bin, "ab") as file:
        file.write(struct.pack("f", y))
        print(f"Результат записано у файл: {filename_result_bin}")


def read_txt(filename):
    """
    Зчитує вміст текстового файлу.

    Args:
        filename (str): ім'я текстового файлу

    Returns:
        str: вміст файлу або повідомлення про помилку
    """
    filename = os.path.join(os.getcwd(), filename)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Помилка: текстовий файл не знайдено."


def read_binary(filename):
    """
    Зчитує та виводить числа з бінарного файлу.

    Args:
        filename (str): ім'я бінарного файлу
    """
    filename = os.path.join(os.getcwd(), filename)

    print(f"\nВміст бінарного файлу '{filename}':")

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4)
                if not data:
                    break
                number = struct.unpack("f", data)[0]
                print(number)
    except FileNotFoundError:
        print("Помилка: бінарний файл не знайдено.")


if __name__ == "__main__":
    txt_file = "result.txt"
    bin_file = "result.bin"

    solution(txt_file, bin_file)

    print("\n--- Вміст текстового файлу ---")
    print(read_txt(txt_file))

    print("\n--- Вміст бінарного файлу ---")
    read_binary(bin_file)

