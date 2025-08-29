import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static int[] arr;
	static boolean[] visited;
	static List<Integer> list;
	static StringBuilder sb;
	
	public static void print() {
		for (int i = 0; i < list.size(); i++) {
			sb.append(list.get(i) + " ");
		}
		sb.append("\n");
	} //print
	
	public static void dfs() {
		if (list.size() == M) {
			print();
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (!visited[i]) {
				list.add(arr[i]);
				visited[i] = true;
				dfs();
				list.remove(list.size() - 1);
				visited[i] = false;
			}
		}
	} //dfs
	
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
		visited = new boolean[N];
		
		dfs();
		System.out.print(sb.toString());
	} //main
} //class
