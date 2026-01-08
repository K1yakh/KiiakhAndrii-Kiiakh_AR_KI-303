import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

/**
 * Лабораторна робота №1.
 * @author Kiiakh
 */
public class kiiakhki303 {

    /**
     * Головний метод програми.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Введіть розмір квадратної матриці (n): ");
            int n = scanner.nextInt();
            scanner.nextLine(); // очищення буфера

            if (n <= 0) {
                System.out.println("Помилка: розмір матриці має бути більший за 0!");
                return;
            }


            System.out.print("Введіть один символ-заповнювач: ");
            String input = scanner.nextLine();

            if (input.length() != 1) {
                System.out.println("Помилка: потрібно ввести рівно один символ!");
                return;
            }

            char filler = input.charAt(0);

            char[][] matrix = generateMatrix(n, filler);

            // Вивід на екран
            System.out.println("Сформована матриця:");
            printMatrix(matrix);

            // Запис у файл
            saveToFile(matrix, "output.txt");
            System.out.println("Матриця збережена у файл output.txt");

        } catch (Exception e) {
            System.out.println("Помилка введення. Програма завершена.");
        } finally {
            scanner.close();
        }
    }

    public static char[][] generateMatrix(int n, char filler) {
        char[][] result = new char[n][n];
        int half = n / 2; // половина розміру

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)


            {
                // верхній лівий квадрант
                if (i < half && j < half ) {
                    if (j == half-1 )
                        result[i][j] = '+';
                    else
                    result[i][j] = filler;

                }
                // нижній правий квадрант
                else if (i >= half && j >= half) {
                         if (j == half-1 )
                        result[i][j] = '+';
                    else
                        result[i][j] = filler;
                }
                // інші квадранти
                else {
                    result[i][j] = ' ';
                }
            }
        }
        return result;
    }

    /**
     * Друкує матрицю у консоль.
     */
    public static void printMatrix(char[][] array) {
        for (char[] row : array) {
            for (char c : row) {
                System.out.print(c + " ");
            }
            System.out.println();
        }
    }

    /**
     * Зберігає матрицю у текстовий файл.
   @throws IOException якщо виникає помилка запису
     */
    public static void saveToFile(char[][] array, String filename) throws IOException {
        try (FileWriter writer = new FileWriter(filename)) {
            for (char[] row : array) {
                for (char c : row) {
                    writer.write(c + " ");
                }
                writer.write("\n");
            }
        }
    }
}

