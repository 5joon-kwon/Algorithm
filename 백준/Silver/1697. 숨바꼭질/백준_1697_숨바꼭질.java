import java.util.*;
import java.io.*;

public class 백준_1697_숨바꼭질 {
    static int N, K;
    static final int MAX = 100000;

    public static int bfs() {
        int[] dist = new int[MAX + 1];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new ArrayDeque<>();
        q.add(N);
        dist[N] = 0;

        while (!q.isEmpty()) {
            int x = q.poll();
            if (x == K) return dist[x];

            int[] nexts = { x - 1, x + 1, x * 2 };
            for (int nx : nexts) {
                if (0 <= nx && nx <= MAX && dist[nx] == -1) {
                    dist[nx] = dist[x] + 1;
                    q.add(nx);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        if (N >= K) {
            System.out.println(N - K);
            return;
        }

        System.out.println(bfs());
    }
}
