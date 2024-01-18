import java.util.Scanner;
import java.util.regex.Pattern;

import static java.lang.System.in;

public class BeautifulYear {

    public static void main(String[] args) {

        // https://codeforces.com/problemset/problem/271/A

        Scanner scanner = new Scanner(in);

        // Récupération de la valeur en int
        int year = scanner.nextInt();

        // Trouver la prochaine année avec des chiffres distincts
        int nextDistinctYear = findNextDistinctYear(year);

        // Output the result
        System.out.println(nextDistinctYear);

    }

    private static int findNextDistinctYear(int year) {
        while (true) {
            year++;

            if (areDigitsDistinct(year)) {
                return year;
            }
        }
    }

    private static boolean areDigitsDistinct(int number) {
        int[] digitCount = new int[10];

        // Check each digit in the number
        while (number > 0) {
            int digit = number % 10;
            if (digitCount[digit] > 0) {
                return false; // Digit is repeated
            }

            digitCount[digit]++;
            number /= 10;
        }

        return true; // All digits are distinct
    }

}
