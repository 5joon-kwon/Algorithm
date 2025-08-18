import java.util.*;
import java.io.*;

public class Solution {
	public static int cross(int[][] arr, int i, int j, int M) {
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, 1, 0, -1};
		int sum = 0;
		
		for (int dir = 0; dir < 4; dir++) {
			int x = i;
			int y = j;
			int f = 0;
			while(true) {				
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				if (nx < 0 || ny < 0 || nx >= arr.length || ny >= arr.length || f == M - 1) {
					break;
				}
				sum += arr[nx][ny];
				x = nx;
				y = ny;
				f++;
			}
		}
		return sum + arr[i][j];
	}
	
	public static int xx(int[][] arr, int i, int j, int M) {
		int[] dx = {-1, -1, 1, 1};
		int[] dy = {-1, 1, 1, -1};
		int sum = 0;
		
		for (int dir = 0; dir < 4; dir++) {
			int x = i;
			int y = j;
			int f = 0;
			while (true) {		
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				if (nx < 0 || ny < 0 || nx >= arr.length || ny >= arr.length || f == M - 1) {
					break;
				}
				sum += arr[nx][ny];
				x = nx;
				y = ny;
				f++;
			}
		}
		return sum + arr[i][j];
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int[][] arr = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int max = 0;
			
			for (int i = 0; i < arr.length; i++) {
				for (int j = 0; j < arr.length; j++) {
					max = Math.max(max, Math.max(cross(arr, i, j, M), xx(arr, i, j, M)));
				}
			}
			
			sb.append("#").append(t).append(" ").append(max).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
}
