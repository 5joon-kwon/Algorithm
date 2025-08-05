import java.io.*;
import java.util.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		char[][] arr = new char[N][M];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = line.charAt(j);
			}
		}
		
		int[][] chess1 = {
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}};
		
		int[][] chess2 = {
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
				{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
				{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}};
		
		int min = N * M;
		
		for (int i = 0; i < N - 7; i++) {
			for (int j = 0; j < M - 7; j++) {
				int cnt1 = 0;
				int cnt2 = 0;
				
				int ci = 0;
				
				for (int si = i; si < i + 8; si++) {
					int cj = 0;
					for (int sj = j; sj < j + 8; sj++) {
						if(arr[si][sj] != chess1[ci][cj])
							cnt1++;
						cj++;
					}
					ci++;
				}

				ci = 0;
				for (int si = i; si < i + 8; si++) {
					int cj = 0;
					for (int sj = j; sj < j + 8; sj++) {
						if(arr[si][sj] != chess2[ci][cj])
							cnt2++;
						cj++;
					}
					ci++;
				}
				
				min = Math.min(min, Math.min(cnt1, cnt2));
			}
		}
		System.out.println(min);
	}
}
