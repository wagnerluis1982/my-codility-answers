// https://app.codility.com/demo/results/trainingCK5CX2-84D/
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        int x = 1;
        int[] XS = Arrays.stream(A)
            .sorted()
            .filter(n -> n > 0)
            .distinct()
            .toArray();
        for (int i = 0; i < XS.length; i++) {
            if (x != XS[i]) return x;
            x++;
        }
        return x;
    }
}
