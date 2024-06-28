import java.util.Scanner;

public class VanyaAndFence {

    public static void main(String[] args) {

        // https://codeforces.com/problemset/problem/677/A
        Scanner scanner = new Scanner(System.in);

        int numberOfFriends = scanner.nextInt();
        int heightOfFence = scanner.nextInt();
        int widthOfRoad = 0;

        for (int i = 0; i < numberOfFriends; i++) {
            int heightOfFriend = scanner.nextInt();
            if (heightOfFriend > heightOfFence) {
                widthOfRoad += 2;
            } else {
                widthOfRoad += 1;
            }
        }

        scanner.close();
        System.out.println(widthOfRoad);

    }

}
