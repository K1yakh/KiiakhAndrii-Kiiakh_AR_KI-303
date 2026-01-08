package KI303.Kiiakh.Lab3;

    public class Sea extends Ecosystem implements Navigable {

        private String seaName;
        private double salinity; // Salinity in PSU (Practical Salinity Units)

        public Sea() {
            super();
            this.seaName = "Unnamed Sea";
            this.salinity = 35.0; // Average ocean salinity
        }

        public Sea(String name, int plantCount, int animalCount, double salinity) {
            super(plantCount, animalCount);
            this.seaName = name;
            this.salinity = salinity;
        }

        public String getSeaName() {
            return seaName;
        }

        public double getSalinity() {
            return salinity;
        }

        public void setSalinity(double newSalinity) {
            this.salinity = newSalinity;
            logActivity("Salinity changed to: " + newSalinity + " PSU for " + this.seaName);
        }

        public void simulateStorm() {
            logActivity("A storm occurred in " + seaName + ". Ecosystem is affected.");
            // Example: reduce plants and animals by 10%
            int plantsLost = (int) (getPlantCount() * 0.1);
            int animalsLost = (int) (getAnimalCount() * 0.1);

            addPlants(-plantsLost); // Using addPlants with negative value to reduce
            addAnimals(-animalsLost);
        }

        @Override
        public String getEnvironmentDetails() {
            return "Sea Name: " + seaName + ", Salinity: " + salinity + " PSU.";
        }

        @Override
        public boolean isShippingAllowed() {
            return true;
        }

        @Override
        public int getMaxVesselTonnage() {
            return 150000;
        }
    }

