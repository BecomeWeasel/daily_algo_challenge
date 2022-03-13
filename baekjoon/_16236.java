import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class _16236 {

    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    static int[][] map;
    static int N;

    static int sharkY = 0;
    static int sharkX = 0;

    static int sharkSize=2;
    static int eat=0;

    private static class Fish {

        int y;
        int x;
        int size;
        int dist;

        public Fish(int y, int x, int size, int dist) {
            this.y = y;
            this.x = x;
            this.size = size;
            this.dist = dist;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            Fish fish = (Fish) o;

            if (y != fish.y) {
                return false;
            }
            if (x != fish.x) {
                return false;
            }
            if (size != fish.size) {
                return false;
            }
            return dist == fish.dist;
        }

        @Override
        public int hashCode() {
            int result = y;
            result = 31 * result + x;
            result = 31 * result + size;
            result = 31 * result + dist;
            return result;
        }
    }

    private static class Shark {

        public Shark(int y, int x, int dist,int size) {
            this.y = y;
            this.x = x;
            this.dist = dist;
            this.size=size;
        }

        int y;
        int x;
        int dist;
        int size;

    }

    private static void printBoard(int[][] map) {
        System.out.println();

        for (int i = 0; i < N; i++) {
            StringBuilder builder = new StringBuilder();
            for (int j = 0; j < N; j++) {
                builder.append(map[i][j]);

            }
            System.out.println(builder);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());

        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer s = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(s.nextToken());
                if (map[i][j] == 9) {
                    sharkY = i;
                    sharkX = j;
                }
            }
        }

        int time = 0;

//        printBoard(map);

        while (true) {
            PriorityQueue<Fish> pq = new PriorityQueue<>((o1, o2) -> {
                if (o1.dist > o2.dist) {
                    return 1;
                } else if (o1.dist == o2.dist) {
                    if (o1.y > o2.y) {
                        return 1;
                    } else if (o1.y == o2.y) {
                        if (o1.x >= o2.x) {
                            return 1;
                        } else {
                            return -1;
                        }
                    } else {
                        return -1;
                    }
                } else {
                    return -1;
                }
            });
            Queue<Shark> q = new LinkedList<>();
            boolean visit[][] = new boolean[N][N];

            q.add(new Shark(sharkY, sharkX, 0,sharkSize));
            visit[sharkY][sharkX] = true;

            findFish(pq, q, visit);

            // 먹을 물고기가 없음
            if (pq.isEmpty()) {
                break;
            }

            // 이제 물고기 먹어야함.
            Fish targetFish = pq.poll();

            eatAndMove(targetFish);
//            printBoard(map);
//            System.out.println("targetFish.dist = " + targetFish.dist);
//            System.out.println("sharkSize = " + sharkSize);
//            System.out.println("eat = " + eat);
            time += targetFish.dist;
        }

        System.out.println(time);


    }

    private static void eatAndMove(Fish targetFish) {
        // 일단 배를 채우고
        eat++;
        // 자기 사이즈만큼 먹었다면 승급
        if (eat==sharkSize){
            eat=0;
            sharkSize++;
        }
        // 물고기 자리로 상어가 이동하고
        map[targetFish.y][targetFish.x]=9;
        // 원래 상어자리는 비게 된다
        map[sharkY][sharkX]=0;
        // 상어의 위치 업데이트
        sharkY= targetFish.y;
        sharkX = targetFish.x;

    }



    private static void findFish(PriorityQueue<Fish> pq, Queue<Shark> q, boolean[][] visit) {
        while (!q.isEmpty()) {
            Shark head = q.poll();

            for (int k = 0; k < 4; k++) {
                int ny = head.y + dy[k];
                int nx = head.x + dx[k];

                // 밖이거나, 방문해봤거나,나보다 큰 물고기는 지나갈 수 없음
              if (isOOB(ny, nx) || visit[ny][nx]||map[ny][nx]>head.size) {
                    continue;
                }

                // 나보다 크기가 작은 물고기를 찾았다면
                if (map[ny][nx]!=0 && map[ny][nx]<head.size){
                    pq.add(new Fish(ny, nx, map[ny][nx], head.dist+1));
                    visit[ny][nx] = true;
                    q.add(new Shark(ny, nx, head.dist + 1, head.size));
                    continue;
                }

                // 아예 빈공간이거나, 내 크기랑 같으면, 지나갈수는 있음
               if (map[ny][nx]==0||(map[ny][nx]!=0&&map[ny][nx]==head.size)){
                    visit[ny][nx] = true;
                    q.add(new Shark(ny, nx, head.dist + 1, head.size));
                    continue;
                }


            }


        }
    }

    private static boolean isOOB(int ny, int nx) {
        return ny >= N || ny < 0 || nx >= N || nx < 0;
    }
}
