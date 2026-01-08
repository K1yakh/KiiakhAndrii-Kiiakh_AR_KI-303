package KI303.Kiiakh.Lab3;

import java.io.FileWriter;
import java.io.IOException;


public abstract class Ecosystem {

    private int plantCount;
    private int animalCount;
    private FileWriter fileWriter; // Для логування

    public Ecosystem() {
        this.plantCount = 0;
        this.animalCount = 0;
        try {
            fileWriter = new FileWriter("ecosystem_log.txt");
        } catch (IOException e) {
            System.err.println("Error creating log file: " + e.getMessage());
        }
    }

    public Ecosystem(int plantCount, int animalCount) {
        this.plantCount = plantCount;
        this.animalCount = animalCount;
        try {
            // Той самий код для ініціалізації файлу
            fileWriter = new FileWriter("ecosystem_log.txt");
        } catch (IOException e) {
            System.err.println("Error creating log file: " + e.getMessage());
        }
    }

    public int getPlantCount() {
        return plantCount;
    }

    public int getAnimalCount() {
        return animalCount;
    }

    public void addPlants(int count) {
        this.plantCount += count;
        logActivity("Added " + count + " plants. Total: " + this.plantCount);
    }

    public void addAnimals(int count) {
        this.animalCount += count;
        logActivity("Added " + count + " animals. Total: " + this.animalCount);
    }

    public abstract String getEnvironmentDetails();

    protected void logActivity(String message) {
        if (fileWriter != null) {
            try {
                // Додаємо "\n" для нового рядка
                fileWriter.write(message + "\n");
                // Примусово записуємо дані негайно
                fileWriter.flush();

            } catch (IOException e) {
                System.err.println("Error writing to log file: " + e.getMessage());
            }
        }
    }

    public void closeLog() {
        if (fileWriter != null) {
            try {
                // Закриваємо файл, це зберігає всі зміни
                fileWriter.close();
            } catch (IOException e) {
                System.err.println("Error closing log file: " + e.getMessage());
            }
        }
    }
}