import java.util.*;
import java.io.*;

public class Main {
	private static int N, M;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			boolean[] visited = new boolean[N + 1];
            List<Integer>[] edges = new ArrayList[N +1];
            for (int i = 1; i <= N; i++) 
            	edges[i] = new ArrayList<>();
            
            for (int i = 0; i < M; i++) {
            	st = new StringTokenizer(br.readLine(), " ");
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                edges[from].add(to);
                edges[to].add(from);
            }
            
            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(1);
            visited[1] = true;
            int count = 0;
            
            while (!queue.isEmpty()) {
                int cur = queue.poll();
                for (int next : edges[cur]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.add(next);
                        count++;
                    }
                }
            }
            
            sb.append(count).append('\n');
		}//test
		System.out.print(sb.toString());
	}//main
}//class
