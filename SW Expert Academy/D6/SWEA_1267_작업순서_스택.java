import java.io.*;
import java.util.*;

public class SWEA_1267_작업순서_스택 {
	
	private static int V, E;
	private static List<Integer>[]  graph;
	private static Stack<Integer> stack;
	private static boolean[] visited;


	private static void dfs(int start) {
		visited[start] = true;
		
		for (int next : graph[start]) {
			if(!visited[next]) {
				dfs(next);
			}
		}
		stack.push(start);
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int t = 1; t <= 10; t++) {
			sb.append("#").append(t);
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			
			graph = new ArrayList[V + 1];
			for (int i = 1; i < V + 1; i++) 
				graph[i] = new ArrayList<>();
			
			int[] inDegree = new int[V + 1];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < E; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				graph[from].add(to);
				inDegree[to]++;
			}
			
			stack = new Stack<>();
			visited = new boolean[V + 1];
			for (int i = 1; i < V + 1; i++) {
				if (inDegree[i] == 0)
					dfs(i);
			}
			
			while(!stack.isEmpty())
				sb.append(" ").append(stack.pop());
			
			sb.append("\n");
		}//test
		System.out.println(sb.toString());
	}//main
}//class
