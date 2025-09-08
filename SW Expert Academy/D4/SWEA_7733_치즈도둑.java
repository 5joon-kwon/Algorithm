import java.util.*;
import java.io.*;

public class SWEA_7733_치즈도둑 {
	public static int N, group_cnt;
	public static int[][] visited, graph;
	public static int[] dx = {-1, 0, 1, 0};
	public static int[] dy = {0, 1, 0, -1};
	public static Queue<Pair> queue;
	
	public static class Pair{
		int i;
		int j;
		
		Pair(int i, int j){
			this.i = i;
			this.j = j;
		}
	}
	
	public static void bfs() {		
		while (!queue.isEmpty()) {
			Pair p = queue.poll();
			int x = p.i;
			int y = p.j;
			for (int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				
				if (nx < 0 || ny < 0 || nx >= N || ny >=N)
					continue;
				
				if (graph[nx][ny] == 0 || visited[nx][ny] > 0)
					continue;
				
				queue.add(new Pair(nx, ny));
				visited[nx][ny] = group_cnt;
			}
		}
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			
			List<Pair>[] count = new List[101];
			for (int i = 0; i < 101; i++)
			    count[i] = new ArrayList<>();
			
			int max_day = 0;
			graph = new int[N][N];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					int num = Integer.parseInt(st.nextToken());
					graph[i][j] = num;
					max_day = Math.max(max_day, num);
					count[num].add(new Pair(i, j));
				}
			}
			
			// 0일째 그룹 세기
			queue = new LinkedList<>();
			visited = new int[N][N];
			group_cnt = 0;

			for (int i = 0; i < N; i++) {
			    for (int j = 0; j < N; j++) {
			        if (graph[i][j] > 0 && visited[i][j] == 0) {
			            group_cnt++;
			            queue.add(new Pair(i, j));
			            visited[i][j] = group_cnt;
			            bfs();
			        }
			    }
			}
			int max_group = group_cnt;
			
			// 1일째부터 그룹 세기
			for (int d = 1; d < max_day; d++) {
				if (count[d].isEmpty())
					continue;
				
				for (int c = 0; c < count[d].size(); c++) {
					Pair p = count[d].get(c);
					graph[p.i][p.j] = 0;
				}
				
				queue = new LinkedList<>();
				visited = new int[N][N];
				group_cnt = 0;
				
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						if(graph[i][j] > 0 && visited[i][j] == 0) {
							group_cnt++;
							queue.add(new Pair(i, j));
							visited[i][j] = group_cnt;
							bfs();
						}
					}
				}
				max_group = Math.max(max_group, group_cnt);
			}
			sb.append("#").append(t).append(" " ).append(max_group).append("\n");
		}//test
		System.out.print(sb.toString());
	}//main
}//class
