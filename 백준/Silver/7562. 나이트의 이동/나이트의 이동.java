import java.io.*;
import java.util.*;

public class Main {
	
	private static int l;
	private static boolean[][] grid;
	private static int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
	private static int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};
	
	public static class Pair{
		int i;
		int j;
		Pair(int i, int j){
			this.i = i;
			this.j = j;
		}
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			l = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			int sx = Integer.parseInt(st.nextToken());
			int sy = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			int tx = Integer.parseInt(st.nextToken());
			int ty = Integer.parseInt(st.nextToken());
			
			grid = new boolean[l][l];
			Queue<Pair> q = new ArrayDeque<>();
			q.add(new Pair(sx, sy));
			grid[sx][sy] = true;
			int cnt = -1;
			boolean flag = false;
			
			while(!q.isEmpty()) {
				if (flag)
					break;
				
				int size = q.size();
				cnt++;
				for (int i = 0; i < size; i++) {
					Pair p = q.poll();
					int pi = p.i;
					int pj = p.j;
					
					if (tx == pi && ty == pj) {
						flag = true;
						break;
					}
					
					for (int dir = 0; dir < 8; dir ++) {
						int ni = pi + dx[dir];
						int nj = pj + dy[dir];
						
						if (ni < 0 || nj < 0 || ni >= l || nj >= l)
							continue;
						
						if (grid[ni][nj])
							continue;
						
						grid[ni][nj] = true;
						q.add(new Pair(ni, nj));
					}
				}
			}
			System.out.println(cnt);
		}//test
	}//main
}//class
