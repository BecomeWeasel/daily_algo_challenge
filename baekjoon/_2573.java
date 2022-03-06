import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 맵을 여러개두던, 빙산에 대한 큐만 모니터링을 하던
// 중요한건 마지막에 모든 빙산이 녹앗을때 두조각이 안되면 0을 출력하는 부분임
// 62퍼에서 시간초과가 나오는 이유는 이걸 고려하지 않고 계속 수행하기 때문으로 보임.


public class _2573 {
    static class IcePair {

        int x, y, lev;

        IcePair(int y, int x, int lev) {
            this.y = y;
            this.x = x;
            this.lev = lev;
        }
    }

    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    static int N, M;
    static int[][] map;
    static int[][] nMap;
    static boolean[][] visited;
    static Queue<IcePair> icebergQueue;
    static Queue<IcePair> newIcebergQueue;
    static Queue<IcePair> meltedIcebergQueue;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

//        System.out.println(N);

        map = new int[N][M];
        nMap = new int[N][M];
        visited = new boolean[N][M];
        icebergQueue = new LinkedList<>();
        newIcebergQueue = new LinkedList<>();
        meltedIcebergQueue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] > 0) {
                    icebergQueue.add(new IcePair(i, j, map[i][j]));
                }
            }
        }
        int year = 0;

        while (!isEnded()) {
            // 두조각으로 나눠져있는지 체크

            visited = new boolean[N][M];

            // 빙산들 찾고 녹이고

            while (!icebergQueue.isEmpty()) {
                IcePair poll = icebergQueue.poll();
                int y, x;
                y = poll.y;
                x = poll.x;

                if (!visited[y][x]) {
                    Queue<IcePair> q = new LinkedList<>();
                    q.add(new IcePair(y, x, map[y][x]));
                    visited[y][x] = true;
                    bfs(q);
                }
            }

            visited = new boolean[N][M];

            // 새로운 맵으로 반영
            while (!newIcebergQueue.isEmpty()) {
                IcePair poll = newIcebergQueue.poll();
                map[poll.y][poll.x] = poll.lev;
                icebergQueue.add(poll);
            }
            while (!meltedIcebergQueue.isEmpty()) {
                IcePair poll = meltedIcebergQueue.poll();
                map[poll.y][poll.x] = 0;
            }

            boolean isAllMelted = true;
            for (int i = 1; i < N - 1; i++) {
                for (int j = 1; j < M - 1; j++) {
                    if (map[i][j] != 0) {
                        isAllMelted = false;
                    }
                }
            }
            if (isAllMelted) {
                System.out.println(0);
                return;
            }
            year++;

        }
        System.out.println(year);
    }

    private static boolean isEnded() {
        int numberOfIceberg = 0;

        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < M - 1; j++) {
                if (map[i][j] > 0 && !visited[i][j]) {
                    if (numberOfIceberg == 1) return true;

                    Queue<IcePair> q = new LinkedList<>();
                    q.add(new IcePair(i, j, map[i][j]));
                    visited[i][j] = true;
                    checkBFS(q);
                    numberOfIceberg++;
                }
            }
        }
        return false;
    }

    private static void checkBFS(Queue<IcePair> q) {
        while (!q.isEmpty()) {
            IcePair poll = q.poll();
            int y = poll.y;
            int x = poll.x;

            for (int k = 0; k < 4; k++) {
                int ny = y + dy[k];
                int nx = x + dx[k];

                if (isOOB(ny, nx) || map[ny][nx] == 0 || visited[ny][nx]) continue;

                q.add(new IcePair(ny, nx, map[ny][nx]));
                visited[ny][nx] = true;
            }
        }
    }

    private static void bfs(Queue<IcePair> q) {
        while (!q.isEmpty()) {
            IcePair poll = q.poll();
            int y = poll.y;
            int x = poll.x;

            // 여기서 녹이고 nMap에 저장

            melt(y, x);


            for (int k = 0; k < 4; k++) {
                int ny = y + dy[k];
                int nx = x + dx[k];

                if (isOOB(ny, nx) || map[ny][nx] == 0 || visited[ny][nx]) continue;

                q.add(new IcePair(ny, nx, map[ny][nx]));
                visited[ny][nx] = true;

            }
        }


    }

    private static void melt(int y, int x) {
        int prev = map[y][x];
        int near = 0;

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (isOOB(ny, nx)) continue;

            if (map[ny][nx] == 0) {
                near++;
            }
        }

        // 여전히 빙하가 남아있음
        if (prev - near > 0) {
            newIcebergQueue.add(new IcePair(y, x, prev - near));
        }
        // 빙하가 녹음
        else {
            meltedIcebergQueue.add(new IcePair(y, x, 0));
        }
    }


    private static boolean isOOB(int y, int x) {
        return y >= N || y < 0 || x >= M || x < 0;
    }


}
