import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] graph;           // 비용(도둑루피) 맵
    static int[][] D;               // 최단 비용 맵
    static boolean[][] visited;     // 방문 확정 맵
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Node implements Comparable<Node> {
        int x;
        int y;
        int cost;

        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    static int dijkstra() {
        for (int i = 0; i < N; i++) {
            Arrays.fill(D[i], Integer.MAX_VALUE);
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        D[0][0] = graph[0][0];
        pq.add(new Node(0, 0, D[0][0]));

        while (!pq.isEmpty()) {
            Node q = pq.poll();

            if (visited[q.x][q.y]) 
            	continue;
            
            visited[q.x][q.y] = true;

            for (int dir = 0; dir < 4; dir++) {
                int nx = q.x + dx[dir];
                int ny = q.y + dy[dir];
                
                if (nx < 0 || ny < 0 || nx >= N || ny >= N) 
                	continue;

                int alt = D[q.x][q.y] + graph[nx][ny];
                if (!visited[nx][ny] && alt < D[nx][ny]) {
                    D[nx][ny] = alt;
                    pq.add(new Node(nx, ny, alt));
                }
            }
        }

        return D[N - 1][N - 1];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int test = 0;

        while (true) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            if (N == 0) 
            	break;

            graph = new int[N][N];
            D = new int[N][N];
            visited = new boolean[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            
            int res = dijkstra();
            test++;
            sb.append("Problem ").append(test).append(": ").append(res).append('\n');
        }
        System.out.print(sb.toString());
    }
}
