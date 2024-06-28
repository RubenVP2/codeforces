import java.util.Scanner;

public class theatreSquare {
    public static void main(String[] args) {

        // https://codeforces.com/problemset/problem/1/A
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        long a = scanner.nextLong();

        long x = n / a;
        long y = m / a;

        if (n % a != 0) {
            x++;
        }
        if (m % a != 0) {
            y++;
        }

        System.out.println(x * y);

    }
}