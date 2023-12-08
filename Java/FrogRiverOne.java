// https://app.codility.com/demo/results/trainingBRHYHJ-QDR/
import java.util.*;
import java.util.stream.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int X, int[] A) {
        int N = A.length;

        Set<Integer> positions = Arrays.stream(A)
            .filter(e -> e <= X)
            .boxed()
            .collect(Collectors.toSet());

        for (int P = 1; P <= X; P++) {
            if (!positions.contains(P)) {
                return -1;
            }
        }

        for (int K = 0; K < N; K++) {
            positions.remove(A[K]);
            if (positions.isEmpty()) {
                return K;
            }
        }

        return -1;
    }
}
