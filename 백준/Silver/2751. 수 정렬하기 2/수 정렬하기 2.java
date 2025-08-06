import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[] arr = new int[N];
		int max = 0;
		int min = 1_000_000;
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			max = Math.max(max, arr[i]);
			min = Math.min(min, arr[i]);
		}
		
		int[] cnt = new int[max - min + 1];
		
		
		for (int i = 0; i < arr.length; i++) {
			cnt[arr[i] - min] = 1;
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < cnt.length; i++) {
			if (cnt[i] != 0)
				sb.append(i + min).append("\n");
		}
		System.out.print(sb.toString());
	}
}
