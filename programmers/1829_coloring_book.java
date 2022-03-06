import java.util.*;

class Solution {

    class Pair {
        int x, y;

        Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    int[] dy = {-1, 1, 0, 0};
    int[] dx = {0, 0, -1, 1};

    HashSet<Pair> visited;

    int numberOfArea = 0;
    int maxSizeOfOneArea = 0;

    int g_m, g_n = 0;

    public int[] solution(int m, int n, int[][] picture) {

        g_m = m;
        g_n = n;

        visited = new HashSet<>();

        int[][] copy = new int[picture.length][picture[0].length];
        for(int i=0; i<copy.length; i++){
            copy[i] = picture[i].clone();
        }



        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Pair p =new Pair(i,j);
                if (copy[i][j] > 0) {
                    numberOfArea++;
                    Queue<Pair> q = new ArrayDeque<>();

                    q.add(p);

                    int ret = bfs(copy, q, copy[i][j]);

                    copy[i][j]=0;

                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, ret);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;

        return answer;
    }

    private boolean isOOB(int y, int x) {
        return y >= g_m || y < 0 || x >= g_n || x < 0;
    }

    private int bfs(int[][] picture, Queue<Pair> queue, int color) {
        int area = 0;


        while (!queue.isEmpty()) {
            Pair head = queue.poll();


            int y = head.y;
            int x = head.x;



            for (int k = 0; k < 4; k++) {
                int ny = y + dy[k];
                int nx = x + dx[k];

                Pair p = new Pair(ny, nx);

                if (isOOB(ny, nx) || picture[ny][nx] != color)
                    continue;

                queue.add(p);
                picture[ny][nx]=0;
                area++;
            }
        }


        return area;

    }
}

