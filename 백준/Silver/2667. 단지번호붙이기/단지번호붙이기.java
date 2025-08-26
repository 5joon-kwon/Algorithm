import java.io.*;
import java.util.*;

public class Main {
	static int N, cnt;
	static char[][] graph;
	static boolean[][] visited;
	static int[] dx = { -1, 0, 1, 0 }, dy = { 0, 1, 0, -1 };

	static void dfs(int x, int y) {
		visited[x][y] = true;
		cnt++;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i], ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= N)
				continue;
			
			if (!visited[nx][ny] && graph[nx][ny] == '1')
				dfs(nx, ny);
		}
	}

	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		visited = new boolean[N][N];
		graph = new char[N][N];
		for (int i = 0; i < N; i++)
			graph[i] = br.readLine().toCharArray();

		List<Integer> home = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cnt = 0;
				if (!visited[i][j] && graph[i][j] == '1') {
					dfs(i, j);
					home.add(cnt);
				}
			}
		}

		Collections.sort(home);
		System.out.println(home.size());
		for (int h : home) {
			System.out.println(h);
		}
	}
}