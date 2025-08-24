import java.util.*;
import java.io.*;

public class Main {
	static int N, K;
	static final int MAX_VALUE = 100000;

	public static class Pair {
		int x;
		int cnt;

		Pair(int x, int cnt) {
			this.x = x;
			this.cnt = cnt;
		}
	}

	public static int bfs(boolean[] visited) {
		Queue<Pair> queue = new ArrayDeque<>();
		queue.add(new Pair(N, 0));
		visited[N] = true;

		while (!queue.isEmpty()) {
			Pair curr = queue.poll();
			int x = curr.x, cnt = curr.cnt;

			if (x == K)
				return cnt;
			
			int[] nexts = {x - 1, x + 1, 2 * x};
			for (int next : nexts) {
				if (0 <= next && next <= MAX_VALUE && !visited[next]) {
					queue.add(new Pair(next, cnt + 1));
					visited[next] = true;
				}
			}
		}
		return -1;
	} // bfs()
	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		if (N >= K) {
			System.out.println(N - K);
			return;
		}

		boolean[] visited = new boolean[MAX_VALUE + 1];
		System.out.println(bfs(visited));

	} // main
} // class
