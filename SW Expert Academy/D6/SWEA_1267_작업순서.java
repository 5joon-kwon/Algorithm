import java.io.*;
import java.util.*;

public class SWEA_1267_작업순서 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int t = 1; t <= 10; t++) {
			sb.append("#").append(t);
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int V = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			
			int[][] graph = new int[V + 1][V + 1];
			int[] inDegree = new int[V + 1];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < E; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				graph[from][to] = 1;
				inDegree[to]++;
			}
			
			Queue<Integer> q = new ArrayDeque<>();
			for (int i = 1; i < V + 1; i++) {
				if (inDegree[i] == 0)
					q.add(i);
			}
			
			while(!q.isEmpty()) {
				int ans = q.poll();
				sb.append(" ").append(ans);
				
				for (int i = 1; i < V + 1; i++) {
					if (graph[ans][i] == 1) {
						inDegree[i]--;
						
						if(inDegree[i] == 0)
							q.add(i);
					}
				}
			}
			sb.append("\n");
		}//test
		System.out.println(sb.toString());
	}//main
}//class
