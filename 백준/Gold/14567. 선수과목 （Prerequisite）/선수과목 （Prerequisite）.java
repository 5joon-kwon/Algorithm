import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Queue<Integer> queue = new LinkedList<>();
		ArrayList<Integer>[] subjects = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			subjects[i] = new ArrayList<>();
		}
		
		int[] indegree = new int[N + 1];
		int[] res = new int[N];
				
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			subjects[A].add(B);
			indegree[B]++;
		}
		
		for (int i = 1; i <= N; i++) {
			if (indegree[i] == 0)
				queue.add(i);
		}
		
		int semester = 1;
		while(!queue.isEmpty()) {
			int size = queue.size();
			for (int s = 0; s < size; s++) {
				int x = queue.poll();
				res[x - 1] = semester;
				
				for (int i = 0; i < subjects[x].size(); i++) {
					int y = subjects[x].get(i);
					indegree[y]--;
					
					if (indegree[y] == 0)
						queue.add(y);
				}
			}
			semester++;
		}
		
		for (int r : res)
			sb.append(r).append(" ");
		
		System.out.print(sb.toString());
	}
}
