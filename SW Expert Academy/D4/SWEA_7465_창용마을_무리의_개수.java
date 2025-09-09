import java.util.*;
import java.io.*;

public class SWEA_7465_창용마을_무리의_개수 {
	private static int[] p;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			p = new int[N + 1]; // 0은 안씀, 1 ~ N
			makeSet(N);
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				union(x, y);
			}
			
			int cnt = 0;
			for (int i = 0; i < p.length; i++) {
				if (p[i] == i)
					cnt++;
			}
			
			sb.append("#").append(t).append(" ").append(cnt).append("\n");
		}//test
		System.out.print(sb.toString());
	}//main
	
	/** x 그룹과 y 그룹 통합 */
	public static void union(int x, int y) {
		int px = findSet(x);	// x 대표자 구하기
		int py = findSet(y);	// y 대표자 구하기
//		if (px == py)	// x의 부모와 y의 부모가 같은 대표자인데, 합치면 사이클 발생 (MST)
//			return false;
		p[py] = px;
	}


	/** x 원소의 대표자 반환 */
	public static int findSet(int x) {
		if (p[x] == x) // 내가 대표이면
			return x;
		else
			return p[x] = findSet(p[x]); // 나의 부모의 부모를 찾아라 (Path Compression)
	}

	/** 대표 배열 */
	public static void makeSet(int N) {
		for (int i = 1; i < N; i++) {
			p[i] = i;
		}
	}
}//class