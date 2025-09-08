import java.util.*;
import java.io.*;

public class SWEA_1868_파핑파핑_지뢰찾기 {
	static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
	static int N;
	static char[][] graph;
	static boolean[][] visited;
	static Queue<Pair> queue;
	
	public static class Pair{
		int i;
		int j;
		
		Pair(int i, int j){
			this.i = i;
			this.j = j;
		}
	}
	
	public static void bfs() {
		while(!queue.isEmpty()) {
			Pair p = queue.poll();
			int x = p.i;
			int y = p.j;
			int cnt = 0;
			
			for (int dir = 0; dir < 8; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				if (nx < 0 || ny < 0 || nx >= N || ny >= N)
					continue;
				if (visited[nx][ny])
					continue;
				
				if (graph[nx][ny] == '*') {
					cnt++;
				}
			}
			
			if (cnt == 0) {
				for (int dir = 0; dir < 8; dir++) {
					if (x + dx[dir] < 0 || y + dy[dir] < 0 || x + dx[dir] >= N || y + dy[dir] >= N)
						continue;
					if (visited[x + dx[dir]][y + dy[dir]])
						continue;
					
					queue.add(new Pair(x + dx[dir], y + dy[dir]));
					visited[x + dx[dir]][y + dy[dir]] = true;
					graph[x + dx[dir]][y + dy[dir]] = (char) ('0' + 0);
				}
			}
			else {
				graph[x][y] = (char) ('0' + cnt);
			}
		}
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			graph = new char[N][N];
			for (int i = 0; i < N; i++) {
				graph[i] = br.readLine().toCharArray();
			}
			
			visited = new boolean[N][N];
			queue = new LinkedList<>();
			
			int press = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					boolean flag = false;
					
					if (graph[i][j] == '*')
						continue;
					
					if (visited[i][j])
						continue;
					
					for (int dir = 0; dir < 8; dir++) {
						int ni = i + dx[dir];
						int nj = j + dy[dir];
						
						if (ni < 0 || nj < 0 || ni >= N || nj >= N)
							continue;
						
						if (graph[ni][nj] == '*') {
							flag = true;
							break;
						}
					}
					
					if (flag) // 주위에 지뢰 있으면
						continue;
					else {
						queue.add(new Pair(i, j));
						visited[i][j] = true;
						graph[i][j] = (char) ('0' + 0);
						for (int dir = 0; dir < 8; dir++) {
							if (i + dx[dir] < 0 || j + dy[dir] < 0 || i + dx[dir] >= N || j + dy[dir] >= N)
								continue;
							
							queue.add(new Pair(i + dx[dir], j + dy[dir]));
							visited[i + dx[dir]][j + dy[dir]] = true;
							graph[i + dx[dir]][j + dy[dir]] = (char) ('0' + 0);
						}
						press++;
						bfs();
					}
				}
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (graph[i][j] == '.')
						press++;
				}
			}
			sb.append("#").append(t).append(" ").append(press).append("\n");
		}//test
		System.out.print(sb.toString());
	}//main
}//class
