public class Task_2 implements Task_2_base {
    @Override
    public int subtask_1_while(int num) {
        // Найти максимальное число, являющееся полным квадратом,
        // не превосходящее заданное натуральное num
        int FirstNum = 0, LastNum = 0;
        while (FirstNum <= num){
            if(FirstNum*FirstNum <= num)
                LastNum = FirstNum*FirstNum;
            else
                break;
            FirstNum++;
        }
        return LastNum;
    }

    @Override
    public int subtask_2_while(int num) {
        // Последовательность целых чисел p(n) определяется следующим образом:
        // p(0) = 1
        // p(k) = 2 * p(k - 1) + 6, k > 0
        //Найти элемент последовательности с номером num

        int FirstNum = 1, PrevEl = 1, NextEl = 0;
        if(num == 0)
            return 1;
        else {
            while (FirstNum <= num){
                NextEl = 2*PrevEl + 6;
                FirstNum++;
                PrevEl = NextEl;
            }
            return NextEl;
        }
    }

    @Override
    public boolean subtask_3_while(int num, int base) {
        // Проверить, является ли число num натуральной степенью числа base
        int a = base;
        while(a < num) {
            a *= base;
        } return num==a;
    }

    @Override
    public int subtask_4_while(int start, int end) {
        // Вычислить, за какое минимальное число операций
        // вычесть 1
        // поделить на 2
        // число start можно превратить в end. Гарантируется, что start >= end >= 1
        int a = 0;
        while (start>end) {
            if(start%2 != 0 || start-end <= 2) {
                start -= 1;
                a++;
            } else {
                start /= 2;
                a++;
            }
        } return a;
    }
}
