import java.util.*;
import java.io.*;

public class Main {
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int R, C;
//	static char[][] graph; 
	
	static Queue<Pair> fqueue;
	static Queue<Pair> jqueue;
	
	public static class Pair{
		int x;
		int y;
		int time;
		
		Pair(int x, int y, int time){
			this.x = x;
			this.y = y;
			this.time = time;
		}
	}
	
	public static int bfs(char[][] graph) {
		
		while (!jqueue.isEmpty()) {			
			Pair curr = jqueue.poll();
			int x = curr.x, y = curr.y, jtime = curr.time;
			
			if (x == 0 || y == 0 || x == R - 1 || y == C - 1)
				return jtime + 1;
			
			while (!fqueue.isEmpty()) {
				if (jtime != fqueue.peek().time)
					break;
				
				Pair curr_fire = fqueue.poll();
				int cfx = curr_fire.x, cfy = curr_fire.y, ftime = curr_fire.time;
				
				for (int dir = 0; dir < 4; dir++) {
					int nfx = cfx + dx[dir], nfy = cfy + dy[dir];
					
					if (nfx < 0 || nfy < 0 || nfx >= R || nfy >= C) {
						continue;
					}
					
					if (graph[nfx][nfy] == '#' || graph[nfx][nfy] == 'F') {
						continue;
					}
					
					fqueue.add(new Pair(nfx, nfy, ftime + 1));
					graph[nfx][nfy] = 'F';
				}
			}
			
			
			for (int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir], ny = y + dy[dir];
				
				if (nx < 0 || ny < 0 || nx >= R || ny >= C) {
					continue;
				}
				
				if (graph[nx][ny] == '#' || graph[nx][ny] == 'F' || graph[nx][ny] == 'J') {
					continue;
				}
				
				jqueue.add(new Pair(nx, ny, jtime + 1));
				graph[nx][ny] = 'J';
				
			}
		}
		return 0;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		char[][] graph = new char[R][C];
		fqueue = new ArrayDeque<>();
		jqueue = new ArrayDeque<>();
		
		for (int i = 0; i < R; i++) {
			graph[i] = br.readLine().toCharArray();
			for (int j = 0; j < C; j++) {
				if (graph[i][j] == 'J')
					jqueue.add(new Pair(i, j, 0));
				else if (graph[i][j] == 'F')
					fqueue.add(new Pair(i, j, 0));
			}
		}
		
		
		int res = bfs(graph);
		
		if (res != 0)
			System.out.println(res);
		else
			System.out.println("IMPOSSIBLE");
		
	} // main
} // class
