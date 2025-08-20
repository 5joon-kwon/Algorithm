import java.util.*;
import java.io.*;

public class Main {
	static List<Integer>[] graph;
	static boolean[] visited;
	static int cnt;
	
	public static void dfs(int currV) {
		for (int nextV : graph[currV]) {
			if (!visited[nextV]) {
				visited[nextV] = true;
				cnt++;
				dfs(nextV);
			}
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		graph = new ArrayList[N + 1];
		for (int i = 0; i < N + 1; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
		}
		
		visited = new boolean[N + 1];
		visited[1] = true;
		dfs(1);
		
		System.out.println(cnt);		
	} //main
} // class
