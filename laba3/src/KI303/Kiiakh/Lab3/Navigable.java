package KI303.Kiiakh.Lab3;

    public interface Navigable {

        boolean isShippingAllowed();

        int getMaxVesselTonnage();

        default void issueNavigationAlert() {
            System.out.println("ALERT: Standard navigation rules apply.");
        }
    }
