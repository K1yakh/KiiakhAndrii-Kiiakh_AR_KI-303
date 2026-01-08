package KI303.Kiiakh.Lab3;

    public class SeaDriver {
        public static void main(String[] args) {
            // Create a Sea object
            Sea blackSea = new Sea("Black Sea", 500, 1500, 18.0);

            System.out.println("--- Initial Ecosystem Info ---");
            System.out.println(blackSea.getEnvironmentDetails());
            System.out.println("Plant count: " + blackSea.getPlantCount());
            System.out.println("Animal count: " + blackSea.getAnimalCount());

            System.out.println("\n--- Navigation Info ---");
            System.out.println("Is shipping allowed? " + blackSea.isShippingAllowed());
            System.out.println("Max vessel tonnage: " + blackSea.getMaxVesselTonnage() + " tons");
            blackSea.issueNavigationAlert(); // Calling the default interface method

            System.out.println("\n--- Simulating Events ---");
            blackSea.addPlants(100);
            blackSea.addAnimals(200);
            System.out.println("After adding life -> Plants: " + blackSea.getPlantCount() + ", Animals: " + blackSea.getAnimalCount());

            blackSea.setSalinity(18.5);
            System.out.println("Salinity changed. Current salinity: " + blackSea.getSalinity() + " PSU");

            blackSea.simulateStorm();
            System.out.println("After storm -> Plants: " + blackSea.getPlantCount() + ", Animals: " + blackSea.getAnimalCount());

            // Don't forget to close the log file to save all changes
            blackSea.closeLog();
            System.out.println("\nProgram finished. Check 'water_log.txt' for activity log.");
        }
    }

