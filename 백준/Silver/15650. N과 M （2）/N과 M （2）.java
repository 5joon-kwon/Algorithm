import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static List<Integer> answer = new ArrayList<>();
	
	static void print() {
		for (int i = 0; i < answer.size(); i++) {
			System.out.print(answer.get(i) + " ");
		}
		System.out.println();
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
            dfs(i + 1);
            answer.remove(answer.size() - 1);
        }
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		dfs(1);
		
	}//main
}//class
