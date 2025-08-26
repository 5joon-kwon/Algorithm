import java.io.*;
import java.util.*;

public class Main {
	static int N, cnt;
	static int[] graph;
	
	static void dfs(int k) {
		if (k == N) {
			cnt++;
			return;
		}
		
		for (int c = 0; c < N; c++) {
			if (canPlace(k, c)) {
				graph[k] = c;
				dfs(k + 1);
			}
		}
	}
	
	static boolean canPlace(int k, int c) {
		for (int r = 0; r < k; r++) {
			if (graph[r] == c || Math.abs(k - r) == Math.abs(c - graph[r]))
				return false;
		}
		return true;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N];
        cnt = 0;
        
        dfs(0);
        System.out.println(cnt);
	}//main
}//class
