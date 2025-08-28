import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static List<Integer> answer = new ArrayList<>();
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();
	
	static void print() {
		for (int i = 0; i < answer.size(); i++) {
			sb.append(answer.get(i)).append(" ");
		}
		sb.append("\n");
	}
	
	static void dfs(int c) {	
		if (c == N + 1) {
			if (answer.size() == M) {
				print();
				return;
			}
			return;
		}
		
		if (answer.size() == M) {
			print();
			return;
		}
		
		for (int i = c; i <= N; i++) {
			answer.add(i);
			dfs(i);
			answer.remove(answer.size() - 1);
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		visited = new boolean[N + 1];
		
		dfs(1);
		System.out.print(sb.toString());
		
	}//main
}//class
