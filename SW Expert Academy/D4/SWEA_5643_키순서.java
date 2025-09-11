import java.util.*;
import java.io.*;

public class SWEA_5643_키순서 {
	private static int N, M;
	private static List<Integer>[] Node, RNode;
	
	private static int bfs(int start) {
		boolean[] visited = new boolean[N + 1];
		Queue<Integer> queue = new ArrayDeque<>();
		queue.add(start);
		visited[start] = true;
		int cnt = 0;
		
		while (!queue.isEmpty()) {
			int cur = queue.poll();
			for (int next : Node[cur]) {
				if (!visited[next]) {
					queue.add(next);
					visited[next] = true;
					cnt++;
				}
			}
		}
		return cnt;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			M = Integer.parseInt(br.readLine());
			
			Node = new ArrayList[N + 1];
			RNode = new ArrayList[N + 1];
			for (int i = 0; i < N + 1; i++) {
				Node[i] = new ArrayList<>();
				RNode[i] = new ArrayList<>();
			}
			
			StringTokenizer st;
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				Node[a].add(b); // 키 작은 -> 키 큰
				RNode[b].add(a); // 키 큰 -> 키 작은
			}
			
			int count = 0;
			for (int i = 1; i <= N; i++) {
				int big = bfs(i);
				int small = bfs(i);
				
				if (big + small == N - 1)
					count++;
			}
						
			sb.append("#").append(t).append(" ").append(count).append("\n");
		}//test
		System.out.print(sb.toString());
	}//main
}//class
