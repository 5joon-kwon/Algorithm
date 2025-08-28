import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static List<Integer> answer = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();
	
	static void print() {
		for (int i = 0; i < answer.size(); i++) {
			sb.append(answer.get(i)).append(" ");
//			System.out.print(answer.get(i) + " ");
		}
//		System.out.println();
		sb.append("\n");
	}
	
	static void dfs() {	
		if (answer.size() == M) {
			print();
			return;
		}
		
		for (int i = 1; i <= N; i++) {
			answer.add(i);
			dfs();
			answer.remove(answer.size() - 1);
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		dfs();
		System.out.print(sb.toString());
		
	}//main
}//class
