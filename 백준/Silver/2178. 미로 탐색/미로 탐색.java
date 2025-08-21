import java.util.*;
import java.io.*;

public class Main {
	static char[][] graph;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int N, M;
	
	public static class Pair{
		int x;
		int y;
		int cnt;
		
		Pair(int x, int y, int cnt){
			this.x = x;
			this.y = y;
			this.cnt = cnt;
		}
	}
	
	public static void bfs(int[][] visited) {
		Queue<Pair> queue = new ArrayDeque<>();
		queue.add(new Pair(0, 0, 1));
		visited[0][0] = 1;
		
		while(!queue.isEmpty()) {
			Pair pre = queue.poll();
			int x = pre.x, y = pre.y, cnt = pre.cnt;

			for (int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir], ny = y + dy[dir];
				if (nx < 0 || ny < 0 || nx >= N || ny >= M || 
						visited[nx][ny] != 0 || graph[nx][ny] == '0')
					continue;
				queue.add(new Pair(nx, ny, cnt + 1));
				visited[nx][ny] = cnt + 1;
			}
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		graph = new char[N][M];
		for (int i = 0; i < N; i++) {
			graph[i] = br.readLine().toCharArray();
		}
		
		int[][] visited = new int[N][M];
		bfs(visited);
		
//		for(int[] arr : visited)
//			System.out.println(Arrays.toString(arr));
		
		System.out.println(visited[N - 1][M - 1]);
	}
}
