import java.io.*;
import java.util.*;

public class Main {

	private static int S, N, cnt;
	private static int[] arr;
	private static List<Integer> pick;

	private static void dfs(int sum, int depth, int start) {
		if (depth != 0 && sum == S)
			cnt++;

		for (int i = start; i < N; i++) {
			pick.add(arr[i]);
			dfs(sum + arr[i], depth + 1, i + 1);
			pick.remove(pick.size() - 1);
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		pick = new ArrayList<>();
		cnt = 0;
		dfs(0, 0, 0);
		System.out.print(cnt);
	}// main
}// class