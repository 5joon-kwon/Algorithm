import java.util.*;
import java.io.*;

public class SWEA_1251_하나로_프림 {
	public static class Edge implements Comparable<Edge>{
		int to;
		long cost;

		public Edge(int to, long cost) {
			this.to = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return Long.compare(this.cost, o.cost);
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] loc = new int[N][2];

			StringTokenizer stx = new StringTokenizer(br.readLine());
			StringTokenizer sty = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				loc[i][0] = Integer.parseInt(stx.nextToken());
				loc[i][1] = Integer.parseInt(sty.nextToken());
			}

			double E = Double.parseDouble(br.readLine());
			
			PriorityQueue<Edge> pq = new PriorityQueue<>();
			boolean visited[] = new boolean[N];
			int pick = 0;
			pq.offer(new Edge(0, 0)); // 0번 정점 시작
			long sum = 0;
			
			while(!pq.isEmpty()) {
				Edge e = pq.poll();
				if (visited[e.to])
					continue;
				
				visited[e.to] = true;
				pick++;
				sum += e.cost;
				
				if (pick == N)
					break;
				
				for (int i = 0; i < N; i++) {
					if (!visited[i]) {
						long dx = loc[e.to][0] - loc[i][0]; 
						long dy = loc[e.to][1] - loc[i][1];
						long cost = dx * dx + dy * dy;
						pq.offer(new Edge(i, cost));
					}
				}
			}

			long ans = Math.round(E * sum);
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		} // test
		System.out.println(sb.toString());
	}// main
}// class
