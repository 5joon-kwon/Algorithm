import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
    static int[] arr, pick;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    
    public static void dfs(int start, int depth) {
    	if (depth == M) {
    		for (int i = 0; i < M; i++) {
				sb.append(pick[i]).append(" ");
			}
    		sb.append("\n");
    		return;
    	}
    	
    	int last = Integer.MIN_VALUE;
    	for (int i = start; i < N; i++) {
    		if (last == arr[i])
    			continue;
    		
			pick[depth] = arr[i];
			last = arr[i];
			dfs(i + 1, depth + 1);
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
			pick = new int[M];
			dfs(0, 0);
			System.out.print(sb.toString());
	}//main
}//class