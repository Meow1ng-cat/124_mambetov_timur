public class Main {
    public static void main(String[] args) {
        Car Skyline =new Car("Skyline", "Nissan", 1957, 100);
        System.out.println(Skyline.getTotal_distance());
        Skyline.trip(14);
        System.out.println(Skyline.getTotal_distance());
    }
}
