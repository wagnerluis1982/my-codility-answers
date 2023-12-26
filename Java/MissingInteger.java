// https://app.codility.com/demo/results/trainingQGWZNG-24A/
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        int seq = 1;
        int current, last = 0;
        for (int i = 0; i < A.length; i++) {
            current = A[i];
            if (current <= 0)    continue;
            if (current == last) continue;
            if (current != seq)  return seq;
            last = current;
            seq++;
        }
        return seq;
    }
}
