public class Main {
    public static void main(String[] args) {
        double a = 7.2;
        double b = 3.6;

        Summa sum = new Summa();
        System.out.println(sum.calculate(a,b));

        Difference diff = new Difference();
        System.out.println(diff.calculate(a,b));

        Multiplication mult = new Multiplication();
        System.out.println(mult.calculate(a,b));

        Division div = new Division();
        System.out.println(div.calculate(a,b));
    }
}
