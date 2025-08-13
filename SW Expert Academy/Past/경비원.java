import java.util.*;
import java.io.*;

public class 경비원 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] arr = new int[N][N];
			
			int[] dx = {-1, 0, 1, 0};
			int[] dy = {0, 1, 0, -1};
			
			int x = 0;
			int y = 0;
			
			for (int i = 0; i < arr.length; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < arr.length; j++) {
					int k = Integer.parseInt(st.nextToken());
					if (k == 2) {
						x = i;
						y = j;
					}
					arr[i][j] = k;
				}
			}
			
			arr[x][y] = 3;
			for (int dir = 0; dir < 4; dir++) {
				int startx = x;
				int starty = y;
				while (true) {
					int nx = startx + dx[dir];
					int ny = starty + dy[dir];
					if (nx < 0 || nx >= N || ny < 0 || ny >= N || arr[nx][ny] == 1) {
						dir += 1;
						break;
					}
					arr[nx][ny] = 3;
					startx = nx;
					starty = ny;
				}
			}
			
			int cnt = 0;
			int wall = 0;
			for (int i = 0; i < arr.length; i++) {
				for (int j = 0; j < arr.length; j++) {
					if (arr[i][j] == 0)
						cnt += 1;
				}
			}
			System.out.println(cnt);
		}
		
	}

}
