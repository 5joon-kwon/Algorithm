import java.util.*;
import java.io.*;

public class Main {
	private static int M, N;
	private static final int INF = Integer.MAX_VALUE;
	public static List<Edge>[] edges;
	private static long[] dist;
	private static PriorityQueue<Edge> pq;
	private static boolean[] visited;

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

	private static long dijkstra(int start, int end) {
		while(!pq.isEmpty()){
			Edge cur = pq.poll();
			
			if (visited[cur.to]) // 방문 했다면
				continue;
			visited[cur.to] = true;
			
			if (cur.to == end)
				return cur.cost;
			
			for (Edge e : edges[cur.to]) {
				if (visited[e.to])
					continue;
				
				long sum = cur.cost + e.cost;
				if (dist[e.to] > sum) {
					dist[e.to] = sum;
					pq.add(new Edge(e.to, dist[e.to]));
				}
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		dist = new long[N + 1];
		Arrays.fill(dist, INF);
		visited = new boolean[N + 1];
		
		edges = new ArrayList[N + 1];
		for (int i = 0; i <= N; i++)
			edges[i] = new ArrayList<>();
		
		StringTokenizer st;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			edges[from].add(new Edge(to, cost));
		}
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		
		dist[start] = 0;
		pq = new PriorityQueue<>();
		pq.add(new Edge(start, 0));
		
		System.out.println(dijkstra(start, end));
		
	}//main
}//class
