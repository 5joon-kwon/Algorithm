import java.util.*;
import java.io.*;

public class 스위치_켜기 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			sb.append("#").append(t).append(" ");
			
			int[] arr = new int[N + 1];
			for (int i = 1; i < arr.length; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
						
			int cnt = 0;
			int[] comp = new int[N + 1];
			
			for (int i = 1; i < arr.length; i++) {
				if (arr[i] != comp[i]) {
					for (int j = 1; j < arr.length; j++) {
						
						if (i * j >= arr.length)
							break;
						
						if (comp[i * j] == 1)
							comp[i * j] = 0;
						else
							comp[i * j] = 1;					
						}
					cnt++;
				}
				
			}
			sb.append(cnt).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
}
