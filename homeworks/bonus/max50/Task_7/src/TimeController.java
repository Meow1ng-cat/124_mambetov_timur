import java.util.ArrayList;
import java.util.Collections;

public class TimeController {
    public String TimeController(ArrayList<String> subjName, ArrayList<Integer> spentTime){
        Integer max = Collections.max(spentTime);
        Integer maxIndex = spentTime.indexOf(max);
        System.out.println(subjName.get(maxIndex));
        return subjName.get(maxIndex);
    }
}
