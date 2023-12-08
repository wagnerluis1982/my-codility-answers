// https://app.codility.com/demo/results/trainingHBMMDW-DFZ/
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // Implement your solution here
        Arrays.sort(A);
        int N = 1;
        for (int e : A) {
            if (e != N++) return 0;
        }
        return 1;
    }
}
