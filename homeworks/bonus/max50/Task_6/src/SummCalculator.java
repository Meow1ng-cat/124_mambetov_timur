import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class SummCalculator {
    public int calculateSumm(HashMap<String, Integer> product, HashMap<String, Integer> cost) {
        int summ = 0;
        for (Map.Entry entry : cost.entrySet()) {
            if (product.containsKey(entry.getKey())) {
                summ += product.get(entry.getKey()) * cost.get(entry.getKey());
            }
        }
        System.out.println(summ);
        return summ;
    }
}



