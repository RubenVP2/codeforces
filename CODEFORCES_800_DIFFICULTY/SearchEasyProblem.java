import java.util.Scanner;

public class SearchEasyProblem {

    public static void main(String[] args) {
        // https://codeforces.com/problemset/problem/1030/A
        Scanner scanner = new Scanner(System.in);
        boolean isEasy = true;

        int numberOfProblems = Integer.parseInt(scanner.nextLine());
        String[] difficulties = scanner.nextLine().split("\\s");

        for (int i = 0; i < numberOfProblems; i++) {
            if (difficulties[i].equals("1")) {
                isEasy = false;
                break;
            }
        }

        scanner.close();
        System.out.println(isEasy ? "EASY" : "HARD");
    }

}