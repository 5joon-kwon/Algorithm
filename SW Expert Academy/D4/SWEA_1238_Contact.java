import java.io.*;
import java.util.*;

public class SWEA_1238_Contact {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for (int t = 1; t <= 1; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int L = Integer.parseInt(st.nextToken());
			int S = Integer.parseInt(st.nextToken());
			
			int[][] grid = new int[101][101];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < (L / 2); i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				if (grid[from][to] == 1)
					continue;
				grid[from][to] = 1;
			}
			
			boolean[] visited = new boolean[101];
			Queue<Integer> queue = new ArrayDeque<>();
			queue.add(S);
			visited[S] = true;
			int ans = S; // 시작점으로 초기화
			
			while(!queue.isEmpty()) {
				int size = queue.size();
				int max = 0;
				
				for (int s = 0; s < size; s++) {
					int f = queue.poll();
					max = Math.max(max, f);
					
					for (int i = 1; i < 101; i++) {
						if (!visited[i] && grid[f][i] == 1) {
							queue.add(i);
							visited[i] = true;
						}
					}
				}
				ans = max;
			}
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		}//test
		System.out.print(sb.toString());
	}//main
}//class
