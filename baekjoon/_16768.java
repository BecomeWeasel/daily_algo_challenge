import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class _16768 {

    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    private static class Point {

        int y, x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            Point point = (Point) o;

            if (y != point.y) {
                return false;
            }
            return x == point.x;
        }

        @Override
        public int hashCode() {
            int result = y;
            result = 31 * result + x;
            return result;
        }
    }

    private static void printBoard(int[][] map) {

        for (int i = 0; i < N; i++) {
            StringBuilder builder = new StringBuilder();
            for (int j = 0; j < WIDTH; j++) {
                builder.append(map[i][j]);

            }
            System.out.println(builder);
        }
    }

    static int N, K;

    static int[][] map;


    private static final int WIDTH = 10;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer s = new StringTokenizer(br.readLine());

        N = Integer.parseInt(s.nextToken());
        K = Integer.parseInt(s.nextToken());

        map = new int[N][WIDTH];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();

            for (int j = 0; j < WIDTH; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        while (true) {
            Set<Point> check = new HashSet<>();

            boolean isUpdated = false;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < WIDTH; j++) {
                    if (map[i][j] != 0) {
                        Point p = new Point(i, j);
                        check.add(p);
                        Queue<Point> q = new LinkedList<>();
                        Queue<Point> candidateQ = new LinkedList<>();
                        q.add(p);
                        candidateQ.add(p);
                        // 업데이트가 아직 소식 없다면, bfs의 결과대로
                        // 이미 업데이트 되었다면 기존 값 그대로 사용
                        boolean ret = bfs(q, candidateQ, check, map[i][j]);
                        isUpdated = isUpdated || ret;
                    }
                }
            }

            if (!isUpdated) {
                break;
            }

            // 중력 적용
            for (int i = 0; i < WIDTH; i++) {
                int cursor = N - 1;
                int[] temp = new int[N];

                for (int j = N - 1; j >= 0; j--) {
                    if (map[j][i] != 0) {
                        temp[cursor] = map[j][i];
                        cursor--;
                    } else {
                        continue;
                    }
                }

                for (int j = N - 1; j >= 0; j--) {
                    map[j][i] = temp[j];
                }
            }


        }

        printBoard(map);


    }

    private static boolean bfs(Queue<Point> q, Queue<Point> candidateQ, Set<Point> check,
        int color) {
        int cnt = 1;
        while (!q.isEmpty()) {
            Point head = q.poll();

            for (int k = 0; k < 4; k++) {
                int ny = head.y + dy[k];
                int nx = head.x + dx[k];

                if (isOOB(ny, nx) || map[ny][nx] != color) {
                    continue;
                }

                Point newP = new Point(ny, nx);

                if (check.contains(newP)) {
                    continue;
                }

                q.add(newP);
                candidateQ.add(newP);
                check.add(newP);
                cnt += 1;
            }

        }

        if (cnt >= K) {
            while (!candidateQ.isEmpty()) {
                // 삭제하기
                Point poll = candidateQ.poll();
                map[poll.y][poll.x] = 0;
            }

            return true;
        } else {
            return false;
        }


    }

    private static boolean isOOB(int y, int x) {
        return y >= N || y < 0 || x >= WIDTH || x < 0;
    }

}
