import java.util.*;
import java.io.*;

public class SWEA_3289_서로소_집합 {

	private static int[] p;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			sb.append("#").append(t).append(" ");
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			p = new int[n + 1];
			makeSet(n);

			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int b = Integer.parseInt(st.nextToken());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				if (b == 0)
					union(x, y);
				else {
					if (findSet(x) == findSet(y))
						sb.append(1);
					else
						sb.append(0);
				}
			}
			sb.append("\n");
		}//test
		System.out.print(sb.toString());
	}//main

	public static void union(int x, int y) {
		int px = findSet(x);
		int py = findSet(y);
		
		p[py] = px;
	}

	public static int findSet(int x) {
		if (p[x] == x)
			return x;
		else
			return p[x] = findSet(p[x]);
	}

	public static void makeSet(int n) {
		for (int i = 1; i <= n; i++) {
			p[i] = i;
		}
	}
}//class
