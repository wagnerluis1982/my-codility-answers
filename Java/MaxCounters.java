// https://app.codility.com/demo/results/training5F8AZK-2V4/

class Solution {
    public int[] solution(int N, int[] A) {
        int[] counters = new int[N];
        int maxCounter = 0;
        int lastMaxCounter = 0;
        boolean hasMaxCounter = false;

        for (int X : A) {
            // operation: 'increase(X)'
            if (1 <= X && X <= N) {
                // adjust counter on position X to the last 'max counter' operation
                if (hasMaxCounter && counters[X - 1] < lastMaxCounter) {
                    counters[X - 1] = lastMaxCounter;
                }
                // hold max counter so far for a future 'max counter' operation
                maxCounter = Math.max(maxCounter, ++counters[X - 1]);
            }
            // operation: 'max counter'
            else if (X == N + 1) {
                lastMaxCounter = maxCounter;
                hasMaxCounter = true;
            }
        }

        // fix counters with eventual values not adjusted by 'max counter' operation
        if (hasMaxCounter) {
            for (int i = 0; i < N; i++) {
                if (counters[i] < lastMaxCounter) {
                    counters[i] = lastMaxCounter;
                }
            }
        }

        return counters;
    }
}
