import java.util.*;
import java.io.*;

public class SWEA_1251_하나로_강사님풀이 {
	public static class Edge implements Comparable<Edge>{
		int from, to;
		long cost;

		public Edge(int from, int to, long cost) {
			this.from = from;
			this.to = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return Long.compare(this.cost, o.cost); // 오름차순
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
		if (px == py)		// 같은 집합 : 합치면 사이클 발생
			return false;	// 합치지마
		else {				// 다른 집합
			p[py] = px;		// 두 집합 합쳐
			return true;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] loc = new int[N][2]; // 각 섬의 x, y 좌표
			StringTokenizer stx = new StringTokenizer(br.readLine());
			StringTokenizer sty = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				loc[i][0] = Integer.parseInt(stx.nextToken());
				loc[i][1] = Integer.parseInt(sty.nextToken());
			}

			double E = Double.parseDouble(br.readLine());
			// MST 크루스칼 : 간선의 개수가 적을 때 유리
			// 모든 정점의 비용을 구하고, 간선 정보를 우선순위큐에 저장
			PriorityQueue<Edge> pq = new PriorityQueue<>();
			for (int i = 0; i < N; i++) {
				for (int j = i + 1; j < N; j++) { // 중복 없이 모든 섬 쌍
					long dx = loc[i][0] - loc[j][0]; // cost 타입 맞추기위해 long 으로 맞추기
					long dy = loc[i][1] - loc[j][1];
					long cost = dx * dx + dy * dy;
					pq.offer(new Edge(i, j, cost));
				}
			}

			// 사이클이 발생하지 않도록 N - 1 개 간선을 선택 (비용을 누적) => Disjoint Set

			p = new int[N];
			makeSet(N);

			long sum = 0;
			int edge_num = 0; // 선택된 간선 수
			while(!pq.isEmpty()) {
				Edge edge = pq.poll();
				if (union(edge.from, edge.to)) {	// 다른 집합이면
					edge_num++;
					sum += edge.cost;
					if (edge_num == N - 1)	// MST 완성
						break;
				}
			}

			long ans = Math.round(E * sum);
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		} // test
		System.out.println(sb.toString());
	}// main
}// class
