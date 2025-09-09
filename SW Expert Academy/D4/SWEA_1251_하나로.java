import java.util.*;
import java.io.*;

public class SWEA_1251_하나로 {
	public static class Edge {
		int from, to;
		long w;

		public Edge(int from, int to, long w) {
			this.from = from;
			this.to = to;
			this.w = w;
		}
	}

	private static int[] p;

	public static void makeSet(int N) {
		for (int i = 0; i < N; i++) {
			p[i] = i;
		}
	}

	public static int findSet(int x) {
		if (p[x] != x)
			p[x] = findSet(p[x]);
		return p[x];
	}

	public static boolean union(int x, int y) {
		int px = findSet(x);
		int py = findSet(y);
		if (px == py)
			return false;
		else {
			p[py] = px;
			return true;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[] X = new int[N];
			int[] Y = new int[N];

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++)
				X[i] = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++)
				Y[i] = Integer.parseInt(st.nextToken());

			double E = Double.parseDouble(br.readLine());

			Edge[] edges = new Edge[N * (N - 1) / 2]; // 모든 간선
			int idx = 0;
			for (int i = 0; i < N; i++) {
				for (int j = i + 1; j < N; j++) { // 중복 없이 모든 섬 쌍
					long dx = X[i] - X[j];
					long dy = Y[i] - Y[j];
					long w = dx * dx + dy * dy;
					edges[idx++] = new Edge(i, j, w);
				}
			}

			Arrays.sort(edges, (a, b) -> Long.compare(a.w, b.w)); // 가중치 오름차순

			p = new int[N + 1];
			makeSet(N);

			long sum = 0;
			int edge_num = 0;
			for (Edge e : edges) {
				if (union(e.from, e.to)) {
					edge_num++;
					sum += e.w;
					if (edge_num == N - 1)
						break;
				}
			}

			long ans = Math.round(E * (double) sum);
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		} // test
		System.out.println(sb.toString());
	}// main
}// class
