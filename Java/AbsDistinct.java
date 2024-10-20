import java.util.stream.IntStream;

class Solution {
    public int solution(int[] A) {
        return (int) IntStream.of(A)
            .map(Math::abs)
            .distinct()
            .count();
    }
}
