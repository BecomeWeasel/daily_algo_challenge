import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _2437 {

    static int N;

    static int[] weight;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        weight = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            weight[i] = Integer.parseInt(st.nextToken());
        }

        int cumulative=0;

        weight=Arrays.stream(weight).sorted().toArray();

        // 내 현재 추의 무게 w를 기준으로,
        // 구간 [0,cumulative]에서는 w보다 작은 추들을 조합해서 무조건 만들 수 있음.
        // 근데, w>cumulative +1 보다 크다라는 건,
        // [0,... ... cumulative] , cumulative+1 , {...} , w이니
        // 단절된 구간이 생김.
        // 만들 수 있는 구간은 [0,cumulative]이고, cumulative+1은 구간에 포함되어 있지 않음.

        // 만약 w==cumulative+1이면, w보다 작은 추들을 조합해서 w는 만들 수 없지만, w를 하나만 사용해서 cumulative+1을 만들 수 있으니
        // 연속적으로 만들수 있는 구간이 [0,cumulative]에서 [0,w]이 된다는 것이다.
        // 이때부터는 w에 [0,cumulative] 안의 아무 값을 조합해서 [0,cumulative+w]까지 만들수 있음을 의미함.

        // 또 w<cumulative+1이면, w보다 작은 추들을 조합해서 이미 w를 만들 수 있다는것이므로
        // [0,w]는 구간 [0,cumulative]에 이미 포함되어 있음.
        for (int w : weight) {
            if (w>cumulative+1) {
                System.out.println(cumulative+1);
                return;
            }

            cumulative+=w;
        }

        System.out.println(cumulative+1);


    }

}
