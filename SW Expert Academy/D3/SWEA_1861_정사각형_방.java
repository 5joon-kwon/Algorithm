import java.util.*;
import java.io.*;

public class SWEA_1861_정사각형_방 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, 1, 0, -1};
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] arr = new int[N][N];
			int[][] visited = new int[N][N];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int max = Integer.MIN_VALUE;
			int num = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (visited[i][j] != 0)
						continue;
					
					int cnt = 1;
					visited[i][j] = arr[i][j];
	
					int x = i;
					int y = j;
					
					while (true) {
						int flag = 0;
						for (int dir = 0; dir < 4; dir++) {
							int nx = x + dx[dir];
							int ny = y + dy[dir];
							if (nx < 0 || ny < 0 || nx >= N || ny >= N 
									|| arr[nx][ny] != arr[nx - dx[dir]][ny - dy[dir]] + 1)
								continue;
							visited[nx][ny] = arr[i][j];
							cnt++;
							flag = 1;
							x = nx;
							y = ny;
						}
						if (flag == 0)
							break;
					}
					
					if (max < cnt || (max == cnt && num > arr[i][j])) {
						max = cnt;
						num = arr[i][j];
					}
				}
			}	
			sb.append("#").append(t).append(" ").append(num).append(" ").append(max).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
}
