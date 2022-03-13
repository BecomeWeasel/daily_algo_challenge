import java.util.LinkedList;
import java.util.Queue;

public class _1631 {

    static int lo = 0;
    static int hi = 1000000;
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    static int R;
    static int C;

    static private class Point {

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
//
//    public static void main(String[] args) {
////        int[][] heights = {{1,2,1,1,1},{1,2,1,2,1},{1,2,1,2,1},{1,2,1,2,1},{1,1,1,2,1}};
//        int[][] heights = {{1, 2, 3}, {3, 8, 4}, {5, 3, 5}};
//        System.out.println(minimumEffortPath(heights));
//    }

    public int minimumEffortPath(int[][] heights) {
        lo = 0;
        hi = 1000000;
        R = heights.length;
        C = heights[0].length;

        int ans = 0;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            System.out.println(lo + " " + hi + " " + mid);
            boolean possible = bfs(mid, heights);
            System.out.println(mid + " is " + possible);
            if (possible) {
                System.out.println("hi shrink " + hi + " to " + (mid - 1));
                hi = mid - 1;
                ans = mid;
            } else {
                System.out.println("lo grow " + lo + " to " + (mid + 1));
                lo = mid + 1;
//                System.out.println("lo grow");
            }
        }
//        System.out.println(lo +" "+ hi);
        return ans;
    }

    private boolean bfs(int maxDiff, int[][] map) {

        Queue<Point> q = new LinkedList<>();
        boolean[][] visit = new boolean[R][C];
        Point initPoint = new Point(0, 0);

        q.add(initPoint);
        visit[0][0] = true;

        boolean isReachable = false;

        while (!q.isEmpty()) {
            Point poll = q.poll();

            for (int k = 0; k < 4; k++) {
                int ny = poll.y + dy[k];
                int nx = poll.x + dx[k];

                if (isOOB(ny, nx) || visit[ny][nx]
                    || Math.abs(map[poll.y][poll.x] - map[ny][nx]) > maxDiff) {
                    continue;
                }

                if (ny == R - 1 && nx == C - 1) {
                    return true;
                }

                Point newPoint = new Point(ny, nx);

                visit[ny][nx] = true;
                q.add(newPoint);


            }

        }

        return isReachable;
    }

    private boolean isOOB(int y, int x) {
        return y >= R || y < 0 || x >= C || x < 0;
    }


}
