public class Task_3 implements Task_3_base {
    @Override
    public int subtask_1_for(int n1, int n2, int a, int b) {
        // подсчитать, сколько чисел, кратных a, но не кратных b,
        // находится между числами n1 и n2 включительно
        int cnt = 0;
        if(n1 < n2){
            for(; n1 <= n2; n1++){
                if(n1%a == 0 && n1%b !=0)
                    cnt++;
            }
        } else {
            for(; n2 <= n1; n2++){
                if(n2%a == 0 && n2%b !=0)
                    cnt++;
            }
        }
        return cnt;
    }

    @Override
    public int subtask_2_for(int num) {
        // Последовательность чисел строится следующим образом:
        // сначала идет одна единица,
        // потом две двойки,
        // потом три тройки,
        // ...
        // потом n раз число n
        // ...
        // Найти, какое число будет находиться в этой последовательности
        // на позиции num
        int cnt = 0, LastNum = 0;
        for(int i = 1; i <= num; i++){
            cnt += i;
            if(cnt >= num){
                LastNum = i;
                break;
            }
        }
        return LastNum;
    }


    @Override
    public int subtask_3_for(int num, int d, int cnt) {
        // Дана последовательность
        // a(0) = num
        // a(n) = a(n - 1) * d + 1
        // Найти сумму первых cnt элементов последовательности
        int PrevEl = num, NextEl, s = num;
        for(int i = 1; i < cnt; i++){
            NextEl = PrevEl*d+1;
            s += NextEl;
            PrevEl = NextEl;
        }
        return s;
    }

    @Override
    public int subtask_4_for(int n) {
        // Вычислить сумму
        // S(n) = 1 + 1 * 2 + 1 * 2 * 3 + ... + n!
        // для заданного n
        // (n! - это n-факториал. Кто не знает - гуглите)
        int s = 0, mlt = 1;
        for(int k = 1; k <= n; k++){
            mlt *= k;
            s += mlt;
        }
        return s;
    }
}
