import java.util.*;
import java.io.*;

public class Main {
	static int[][] graph;
	static int M, N, K, cnt;
	static int[] dx = {-1, 0, 1, 0}, dy = {0, 1, 0, -1};
	static boolean[][] visited;
	
	static void dfs(int x, int y) {
		visited[x][y] = true;
		
		for (int dir = 0; dir < 4; dir++) {
			int nx = x + dx[dir], ny = y + dy[dir];
			
			if (nx < 0 || ny < 0 || nx >= M || ny >= N)
				continue;
			
			if (!visited[nx][ny] && graph[nx][ny] == 1)
				dfs(nx, ny);
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			
			graph = new int[M][N];
			for (int k = 0; k < K; k++) {
				st = new StringTokenizer(br.readLine());
				int i = Integer.parseInt(st.nextToken());
				int j = Integer.parseInt(st.nextToken());
				graph[i][j] = 1;
			}
			
			visited = new boolean[M][N];
			cnt = 0;
			
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < N; j++) {
					if (graph[i][j] == 1 && !visited[i][j]) {
						dfs(i, j);
						cnt++;
					}
				}
			}
			System.out.println(cnt);
		}//test
	}//main
}//class
