import java.util.HashMap;

public class Counter {
    public HashMap<Integer,Integer> count(int[] array){
        HashMap<Integer,Integer> a = new HashMap<>();
        for (int i = 0; i < array.length; i++){
            if(a.containsKey(array[i])){
                int b = a.get(array[i])+1;
                a.put(array[i],b);
            }
            else {
                a.put(array[i],1);
            }
        }
        for (int i = 0; i < array.length; i++){
            System.out.println(a.get(i));
        }
        return a;
    }
}

