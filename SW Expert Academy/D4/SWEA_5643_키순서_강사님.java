import java.util.*;
import java.io.*;

/**
 * 인접행렬로 저장 후 나보다 큰 친구 정보를 저장 (Memoization)
 */

public class SWEA_5643_키순서_강사님 {
	private static int N, M;
	private static int[][] graph;
	
	/** start 보다 큰 사람을 체크*/
	public static void dfs(int start) {
		if (graph[start][0] == -1)	// 이미 연산한 행이면 반환
			return;
		
		for (int i = 1; i <= N; i++) {
			if (graph[start][i] == 1) {	// 나보다 큰 사람
				dfs(i);	// 너보다 큰 사람 정보 다 가져와
				for (int j = 1; j <= N; j++) {	// 너보다 큰 사람 정보 내꺼에 덮어쓸게
					graph[start][j] |= graph[i][j];	// bit or 연산
				}
			}
		}
		graph[start][0] = -1;	// 해당 행은 연산 완료
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			M = Integer.parseInt(br.readLine());
			
			graph = new int[N + 1][N + 1];
			StringTokenizer st;
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int small = Integer.parseInt(st.nextToken());
				int tall = Integer.parseInt(st.nextToken());
				graph[small][tall] = 1; // 단방향
			}
			
			// 모든 정점에 대해 dfs 탐색 + 탐색한 정보를 저장
			for (int i = 1; i <= N; i++) {
				dfs(i);
			}
			
			int cnt = 0;
			for (int i = 1; i < N + 1; i++) {
				int sum = 0;
				for (int j = 1; j < N + 1; j++) {
					sum += graph[i][j] + graph[j][i];	// 나보다 큰 사람 + 작은 사람
				}
				if (sum == N -1)
					cnt++;
			}
						
			sb.append("#").append(t).append(" ").append(cnt).append("\n");
		}//test
		System.out.print(sb.toString());
	}//main
}//class
