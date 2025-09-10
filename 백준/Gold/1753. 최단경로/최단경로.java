import java.util.*;
import java.io.*;

public class Main {
	public static class Node implements Comparable<Node> {
		int to;
		int weight;

		@Override
		public int compareTo(Node o) {
			return this.weight - o.weight;
		}

		public Node(int to, int weight) {
			this.to = to;
			this.weight = weight;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(br.readLine());
		
		ArrayList<Node>[] graph = new ArrayList[V + 1];
		int[] dist = new int[V + 1];
		boolean[] visited = new boolean[V + 1];
		
		for (int i = 0; i <= V; i++) {
			graph[i] = new ArrayList<>();
			dist[i] = Integer.MAX_VALUE;
		}
		
		for (int i = 1; i <= E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			graph[from].add(new Node(to, weight));
		}
		
		PriorityQueue<Node> queue = new PriorityQueue<>();
		dist[K] = 0;
		queue.add(new Node(K, 0));
		
		while(!queue.isEmpty()) {
			Node q = queue.poll();
			visited[q.to] = true;
			for (Node node : graph[q.to]) {
				if (!visited[node.to]) {
					if (dist[q.to] + node.weight < dist[node.to]) {
						dist[node.to] = dist[q.to] + node.weight;
						queue.add(new Node(node.to, dist[node.to]));
					}
				}
			}
		}
		
		for (int i = 1; i <= V; i++) {
			if (dist[i] == Integer.MAX_VALUE)
				sb.append("INF").append("\n");
			else
				sb.append(dist[i]).append("\n");
		}
		System.out.print(sb.toString());
	}// main
}// class