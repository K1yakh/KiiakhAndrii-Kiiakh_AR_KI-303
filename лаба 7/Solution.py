"""
Програма генерує квадратну матрицю за заданим шаблоном.
Варіант: Заповнення верхнього лівого та нижнього правого квадрантів символом.

Введення: розмірність матриці (n) та символ-заповнювач.
Виведення: матриця у консоль.

@author User
@version 1.0
@since version 1.0
"""

from typing import List, Optional, Union

def matrixSquare(n: int, symbol: str) -> List[List[Optional[str]]]:
    """
    Створює матрицю розміром n*n та заповнює квадранти символом.

    Алгоритм перевіряє координати (i, j) відносно центру матриці.
    
    Args:
        n (int): Розмірність квадратної матриці (кількість рядків/стовпців).
        symbol (str): Символ для заповнення областей.

    Returns:
        List[List[str]]: Згенерована матриця.
    """
    # Створення порожньої матриці
    matrix = [[None for _ in range(n)] for _ in range(n)]
    centre = int(n / 2)

    i = 0
    while i < n:
        j = 0
        if i < centre:
            # Верхній лівий
            while j < centre:
                matrix[i][j] = symbol
                j += 1
        if i >= centre:
            # Нижній правий
            j = centre
            while j < n:
                matrix[i][j] = symbol
                j += 1
        i += 1
        # Скидання j не обов'язкове тут, оскільки воно ініціалізується на початку циклу,
        # але залишаємо для збереження вашої логіки.
        j = 0 
        
    return matrix

def printMatrix(n: int, matrix: List[List[Optional[str]]]) -> None:
    """
    Виводить матрицю на екран, замінюючи None на пробіли.

    Args:
        n (int): Розмірність (не використовується для ітерації, але передається).
        matrix (List[List[str]]): Матриця для друку.
    """
    for row in matrix:
        for element in row:
            if element is None:      
                print(" ", end=" ")  
            else:
                print(element, end=" ")
        print()

# Цей блок важливий! 
# Він дозволяє pydoc імпортувати файл без запуску input(),
# але при звичайному запуску програма працюватиме як треба.
if __name__ == "__main__":
    try:
        rowsNcolumns = int(input("Enter number of rows and columns: "))
        symbol = input("Enter symbol to fill matrix: ")

        result_matrix = matrixSquare(rowsNcolumns, symbol)
        printMatrix(rowsNcolumns, result_matrix)
    except ValueError:
        print("Error: Please enter a valid integer for rows/columns.")