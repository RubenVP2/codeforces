import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StringTask {
    public static void main(String[] args) {
        // https://codeforces.com/problemset/problem/118/A

        Scanner scn = new Scanner(System.in);

        String[] input = scn.nextLine().toLowerCase().split("");
        char[] vowels = { 'a', 'o', 'y', 'e', 'u', 'i' };

        Stream<String> stream = Arrays.stream(input);

        String result = stream.map(c -> new String(vowels).contains(c) ? c.replace(c, "") : c)
                .filter(c -> !c.isEmpty())
                .map(c -> ".".concat(c)).collect(Collectors.joining());

        System.out.println(result);
    }
}
