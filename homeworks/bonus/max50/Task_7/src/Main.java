import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        TimeController One = new TimeController();

        ArrayList<String> subject = new ArrayList<String>();
        subject.add("Math");
        subject.add("English");
        subject.add("Chemestry");

        ArrayList<Integer> time = new ArrayList<Integer>();
        time.add(12);
        time.add(6);
        time.add(3);

        One.TimeController(subject,time);
    }
}