import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
    static int[] arr, pick;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    
    public static void dfs(int depth) {
    	if (depth == M) {
    		for (int i = 0; i < M; i++) {
				sb.append(pick[i]).append(" ");
			}
    		sb.append("\n");
    		return;
    	}
    	
    	int last = Integer.MIN_VALUE;
    	for (int i = 0; i < N; i++) {
			if (visited[i])
				continue;
			if (arr[i] == last)
				continue;
			visited[i] = true;
			pick[depth] = arr[i];
			dfs(depth + 1);
			visited[i] = false;
			last = arr[i];
		}
    }
    
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		visited = new boolean[N];
		pick = new int[M];
		
		dfs(0);
		System.out.print(sb.toString());
		
	}//main
}//class