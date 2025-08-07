import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Set<Integer> set = new HashSet<>();
		for (int i = 0; i < N; i++) {
			set.add(Integer.parseInt(st.nextToken()));
		}
		
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < M; i++) {
			int num = Integer.parseInt(st.nextToken());
			if (set.contains(num))
				sb.append(1).append("\n");
			else
				sb.append(0).append("\n");
		}
		System.out.print(sb.toString());
	}
}
