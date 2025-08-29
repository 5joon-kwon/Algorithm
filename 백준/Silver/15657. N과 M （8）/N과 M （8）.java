import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static int[] arr;
	static List<Integer> list;
	static StringBuilder sb;
	
	public static void print() {
		for (int i = 0; i < list.size(); i++) {
			sb.append(list.get(i) + " ");
		}
		sb.append("\n");
	}//print
	
	public static void dfs(int start) {
		if (list.size() == M) {
			print();
			return;
		}
		
		for (int i = start; i < N; i++) {
			list.add(arr[i]);
			dfs(i);
			list.remove(list.size() - 1);
		}
	}//dfs
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		arr = new int[N];
		for (int i = 0; i < N; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		Arrays.sort(arr);
		list = new ArrayList<>();
		
		dfs(0);
		System.out.print(sb.toString());
	}//main
}//class
