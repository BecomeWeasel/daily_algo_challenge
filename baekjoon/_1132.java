import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class _1132 {

    static int N;
    static List<String> numbers;

    static boolean[] isComingAtFront = new boolean[]{false, false, false, false, false, false,
        false, false, false, false};

    static Map<Integer, Long> countMap;


    private static class Count {

        long count;
        int alpha;


        public Count(long count, int alpha) {
            this.count = count;
            this.alpha = alpha;
        }

        @Override
        public String toString() {
            return "Count{" +
                "count=" + count +
                ", alpha=" + alpha +
                '}';
        }
    }


    public static void main(String[] var0) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt((new StringTokenizer(br.readLine())).nextToken());
        countMap = new HashMap<>();
        numbers = new LinkedList<>();

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            numbers.add(String.format("%12s", st.nextToken()));
        }

        for (String number : numbers) {
            int numberofspace = 0;
            for (int i = 0; i < number.length(); i++) {

                if (number.charAt(i) == ' ') {
                    numberofspace++;
                    continue;
                }
//                System.out.println(Character.getNumericValue(number.charAt(i)));
                int ascii = (int) number.charAt(i) - 65;

                if (i == numberofspace) {
                    isComingAtFront[ascii] = true;
                }

                if (countMap.containsKey(ascii)) {
                    Long prev = countMap.get(ascii);
                    countMap.put(ascii, (long) (prev + Math.pow(10, 11 - i)));
                } else {
                    countMap.put(ascii, (long) Math.pow(10, 11 - i));
                }

            }
        }

        List<Count> countList = new LinkedList<>();

        for (Integer k : countMap.keySet()) {
            countList.add(new Count(countMap.get(k), k));
        }

        countList.sort(new Comparator<Count>() {
            @Override
            public int compare(Count o1, Count o2) {
                if (o1.count > o2.count) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });

        // 10개 알파벳 모두 사용하고 있으면
        if (countList.size() == 10) {
            // 가장 카운트가 낮은 0으로 시작하지 않는 애를 맨뒤로 보내야함 -> 0을 할당받게
            for (int i = countList.size(); i > -1; i--) {
                Count count = countList.get(i - 1);
                if (!isComingAtFront[count.alpha]) {
                    countList.remove(count);
                    countList.add(count);
                    break;
                }
            }
        }

        Long sum = 0L;

        for (int i = 0; i < countList.size(); i++) {

            sum += (countList.get(i).count * (9 - i));
        }

        System.out.println(sum);

    }


}
