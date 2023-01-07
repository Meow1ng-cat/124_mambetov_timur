import java.util.Arrays;

public class Task_4 implements Task_4_base {
    @Override
    public int[] subtask_1_arrays(int size, int a0, int d) {
        // сгенерировать и вернуть массив размера size, содержащий элементы
        // арифметической прогрессии с первым членом a0 и разностью d
        int[] M = new int[size];
        M[0] = a0;
        for (int i = 1; i < size; i++) {
            M[i] = M[i - 1] + d;
        }
        return M;
    }


    @Override
    public int[] subtask_2_arrays(int size) {
        // сгенерировать и вернуть массив размера size, первые два элемента
        // которого равны единице, а каждый следующий - сумме всех предыдущих
        int[] num = new int[size];
        int s = 2;
        for (int i = 0; i < size; i++) {
            if (i <= 1) {
                num[i] = 1;
            } else {
                num[i] = s;
                s += s;
            }
        }
        return num;
    }

    @Override
    public int[] subtask_3_arrays(int size) {
        // сгенерировать и вернуть массив размера size, содержащий первые
        // size чисел последовательности фибоначчи.
        // https://ru.wikipedia.org/wiki/Числа_Фибоначчи
        int[] num = new int[size];
        for (int i = 0; i < size; i++) {
            if (i == 0)
                num[i] = 0;
            else if (i == 1)
                num[i] = 1;
            else
                num[i] = num[i - 2] + num[i - 1];
        }
        return num;
    }

    @Override
    public int subtask_4_arrays(int[] data) {
        // Для данного массива вычислить максимальный элемент
        int a = Integer.MIN_VALUE;
        for (int i = 0; i<data.length; i++) {
            if (data[i]>a)
                a = data[i];
        }
        return a;
    }

    @Override
    public int subtask_5_arrays(int[] data, int k) {
        // Для данного массива вычислить максимальный элемент
        // кратный k. Гарантируется, что как минумум один такой элемент
        // в массиве есть
        int a = Integer.MIN_VALUE;
        for (int i = 0; i<data.length; i++) {
            if (data[i]>a && data[i]%k==0)
                a = data[i];
        }
        return a;
    }

    @Override
    public int[] subtask_6_arrays(int[] arr1, int[] arr2) {
        // Даны два массива arr1, arr2.
        // Произвести слияние данных массивов в один отсортированный
        // по возрастанию массив.
        int arr3[]= new int[arr1.length + arr2.length];
        int i=0, j=0, k=0;
        while (i< arr1.length && j<arr2.length){
            if (arr1[i]<=arr2[j]){
                arr3[k]=arr1[i];
                i++;
            }
            else{
                arr3[k]= arr2[j];
                j++;
            }
            k++;
        }
        while (i<arr1.length){
            arr3[k]= arr1[i];
            i++;
            k++;
        }
        while (j<arr2.length){
            arr3[k]= arr2[j];
            j++;
            k++;
        }
        Arrays.sort(arr3);
        return arr3;
    }

    @Override
    public int[] subtask_7_arrays(int[] arr1, int[] arr2) {
        // Даны два отсортированных по возрастанию массива arr1, arr2.
        // Произвести слияние данных массивов в один также отсортированный
        // по возрастанию массив.
        // Используйте алгоритм, время работы которого будет пропорционально сумме
        // размеров arr1 и arr2, а не их произведению
        return null;
    }
}
