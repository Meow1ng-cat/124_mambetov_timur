import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        SummCalculator One = new SummCalculator();

        HashMap<String, Integer> product = new HashMap<>();
        product.put("Чай", 2);
        product.put("Печенье", 2);
        product.put("Мед", 1);

        HashMap<String, Integer> cost = new HashMap<>();
        cost.put("Чай", 17);
        cost.put("Печенье", 6);
        cost.put("Мед", 20);

        One.calculateSumm(product,cost);

    }
}