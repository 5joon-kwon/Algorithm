import java.io.*;
import java.util.*;

public class Main {
	public static int[] dx = {-1, 0, 1, 0};
	public static int[] dy = {0, 1, 0, -1};
	private static int[][] box;
	private static int N, M, cnt;
	private static Queue<Pair> q;
	
	public static class Pair{
		int i;
		int j;
		
		public Pair(int i, int j) {
			this.i = i;
			this.j = j;
		}
	}
	
	private static void bfs() {
		while(!q.isEmpty()) {
			int size = q.size();	// 날짜 체크
			cnt++;
			for (int i = 0; i < size; i++) {
				Pair loc = q.poll();
				int x = loc.i;
				int y = loc.j;
				
				for (int dir = 0; dir < 4; dir++) {
					int nx = x + dx[dir];
					int ny = y + dy[dir];
					
					if (nx < 0 || ny < 0 || nx >= N || ny >= M)
						continue;
					
					if (box[nx][ny] != 0)
						continue;
					
					box[nx][ny] = 1;
					q.add(new Pair(nx, ny));
				}
			}
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		box = new int[N][M];
		boolean init = false;
		q = new ArrayDeque<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				box[i][j] = Integer.parseInt(st.nextToken());
				
				if (box[i][j] == 0)	// 익지 않은 토마토 존재
					init = true;
				
				if (box[i][j] == 1)
					q.add(new Pair(i, j));	// 처음 익은 토마토 위치
			}
		}

		// 모두 익은 토마토이면 끝
		if (!init) {
			System.out.println(0);
			return;
		}
		
		cnt = -1;
		bfs();	// 초기 익은 토마토 위치로 탐색
				
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (box[i][j] == 0) {
					System.out.println(-1);
					return;
				}
			}
		}
		System.out.println(cnt);
	}//main
}//class
