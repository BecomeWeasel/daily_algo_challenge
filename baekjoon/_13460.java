import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _13460 {
    private static class Point {
        int y, x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static class Node {
        Point red;
        Point blue;
        int count;

        public Node(Point red, Point blue, int count) {
            this.red = red;
            this.blue = blue;
            this.count = count;
        }
    }

    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    static int N, M;

    private static final int WALL = -1;
    private static final int BLANK = 0;
    private static final int GOAL = 318;

    static int[][] map;
    static boolean[][][][] check;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        check = new boolean[N][M][N][M];

        int r_y, r_x, b_y, b_x, goal_y, goal_x;
        r_y = r_x = b_y = b_x = goal_y = goal_x = 0;

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                switch (s.charAt(j)) {
                    case '#':
                        map[i][j] = WALL;
                        break;
                    case '.':
                        map[i][j] = BLANK;
                        break;
                    case 'R':
                        map[i][j] = BLANK;
                        r_y = i;
                        r_x = j;
                        break;
                    case 'B':
                        map[i][j] = BLANK;
                        b_y = i;
                        b_x = j;
                        break;
                    case 'O':
                        map[i][j] = GOAL;
                        goal_y = i;
                        goal_x = j;
                        break;
                }
            }
        }


        Queue<Node> q = new LinkedList<Node>();
        q.add(new Node(new Point(r_y, r_x), new Point(b_y, b_x), 0));
        check[r_y][r_x][b_y][b_x] = true;

        while (!q.isEmpty()) {
            Node poll = q.poll();

            Point red = poll.red;
            Point blue = poll.blue;

            int count = poll.count;

            if (poll.count == 10) {
                System.out.println(-1);
                return;
            }

            for (int k = 0; k < 4; k++) {
                int r_ny, r_nx, b_ny, b_nx;

                r_ny = red.y;
                r_nx = red.x;

                b_ny = blue.y;
                b_nx = blue.x;



                /*
                switch (k) {
                    // 위로 굴리기
                    case 0:
                        /*
                        // x좌표 같으니 y좌표 작은거부터 굴리기
                        if (r_nx == b_nx) {
                            if (r_nx == goal_x) {
                                // 무조건 실패
                                continue;
                            }

                            if (r_ny < b_ny) {
                                while(r_ny)
                            }
                        }



                        break;
                    // 아래로 굴리기 , y 좌표 큰거 먼저
                    case 1:

                        break;
                    // 좌로 굴리기 , y 좌표 작은거 먼저
                    case 2:

                        break;
                    // 우로 굴리기 , y 좌표 큰거 먼저
                    case 3:

                        break;
                }*/

                boolean isRedGoal, isBlueGoal;

                isRedGoal = isBlueGoal = false;


                // 빨강이 먼저 이동
                while (map[r_ny + dy[k]][r_nx + dx[k]] != WALL) {
                    r_ny += dy[k];
                    r_nx += dx[k];

                    if (r_ny == goal_y && r_nx == goal_x) {
                        isRedGoal = true;
                        break;
                    }
                }

                // 파랑이 먼저 이동
                while (map[b_ny + dy[k]][b_nx + dx[k]] != WALL) {
                    b_ny += dy[k];
                    b_nx += dx[k];

                    if (b_ny == goal_y && b_nx == goal_x) {
                        isBlueGoal = true;
                        break;
                    }
                }

                // 근데 이동하다보면 둘이 겹칠수가 있음
                // 그럴땐 먼저 도착한 구슬은 그대로, 뒤늦게 도착한건 방향 기준 한칸 뒤로
                // 먼저 도착한건 이동량으로 판단함
                // 이동량은 처음 좌표와 새로운 좌표의 절댓값으로 계산함
                if (r_ny == b_ny && r_nx == b_nx) {
                    int redMoveDistance = Math.abs(r_ny - red.y) + Math.abs(r_nx - red.x);
                    int blueMoveDistance = Math.abs(b_ny - blue.y) + Math.abs(b_nx - blue.x);

                    if (redMoveDistance > blueMoveDistance) {
                        r_ny-=dy[k];
                        r_nx-=dx[k];
                    } else {
                        b_ny-=dy[k];
                        b_nx-=dx[k];
                    }

                }


                if (check[r_ny][r_nx][b_ny][b_nx]) continue;


                if (isBlueGoal) continue;


                if (isRedGoal && !isBlueGoal) {
                    System.out.println(count + 1);
                    return;
                }

                q.add(new Node(new Point(r_ny, r_nx), new Point(b_ny, b_nx), count + 1));
                check[r_ny][r_nx][b_ny][b_nx] = true;

            }


        }

        System.out.println(-1);
    }
}
