public class Dubler {
    public int[] doubling (int [] array) {
        int [] array2 = new int[array.length * 2];
        int a = 0;
        for (int i =0; i < array.length; i++){
            array2[a] = array[i];
            a++;
            array2[a] = array[i];
            a++;
        }
        for (int i = 0; i <array2.length; i++) {
            System.out.println(array2[i]);
        }
        return array2;
    }
}
