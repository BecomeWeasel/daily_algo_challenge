import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class _1967 {

    static int N;

    static List<LinkedList<Edge>> edges;
    static boolean[] visited;
    static int longDist;
    static int endPoint;

    private static class Edge {

        int node;
        int weight;

        public Edge(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());

        edges = new LinkedList<>();
        for (int i = 0; i < N+1; i++) {
            edges.add(new LinkedList<>());
        }
        visited = new boolean[N + 1];

        longDist = 0;
        endPoint = 1;

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            edges.get(parent).add(new Edge(child, weight));
            edges.get(child).add(new Edge(parent, weight));
        }

        visited[1] = true;

        dfs(1, 0);

//        System.out.println("longDist = " + longDist);
//        System.out.println("endPoint = " + endPoint);

        visited = new boolean[N + 1];

        visited[endPoint] = true;
        longDist = 0;

        dfs(endPoint, 0);

//        System.out.println("longDist = " + longDist);
//        System.out.println("endPoint = " + endPoint);

        System.out.println(longDist);

    }

    private static void dfs(int nodeNumber, int dist) {
        for (Edge e : edges.get(nodeNumber)) {
            if (!visited[e.node]) {
                if (dist + e.weight >= longDist) {
                    longDist = dist + e.weight;
                    endPoint = e.node;
                }
                visited[e.node] = true;
                dfs(e.node, dist + e.weight);
            }
        }
    }

}
