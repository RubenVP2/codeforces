import java.util.Arrays;
import java.util.Scanner;

public class SearchEasyProblem {

    public static void main(String[] args) {
        // https://codeforces.com/problemset/problem/1030/A
        Scanner scanner = new Scanner(System.in);
        boolean isEasy = false;
        int count = 1;

        while (scanner.hasNextLine()) {
            String[] lines = scanner.nextLine().split("\\s");

           if (count == 2 && !Arrays.stream(lines).toList().contains("1")) {
               isEasy = true;
               break;
           }
           count++;
        }
        scanner.close();
        System.out.println(isEasy ? "EASY" : "HARD");
    }

}
