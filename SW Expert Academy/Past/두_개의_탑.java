import java.util.*;
import java.io.*;

public class 두_개의_탑 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M1 = Integer.parseInt(st.nextToken()); // 탑1 층수
			int M2 = Integer.parseInt(st.nextToken()); // 탑2 층수
			
			int[] arr = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(arr);
			
			int[] top1 = new int[M1];
			int height1 = 0;
			
			int[] top2 = new int[M2];
			int height2 = 0;
			
			int f = 0;
			for (int i = N - 1; i >= 0; i--) {
				if (i == N - 1) {
					top1[f] = arr[i];
					top2[f] = arr[i - 1];
					height1++;
					height2++;
					i -= 2;
					f++;
				}
				
				if (height1 == M1) {
					if (height2 == M2)
						break;
					
					for (int j = i; j >= 0; j--) {
						top2[f] = arr[j];
						f++;
					}
					break;
				}
				
				if (height2 == M2) {
					if (height1 == M1)
						break;
					
					for (int j = i; j >= 0; j--) {
						top1[f] = arr[j];
						f++;
					}
					break;
				}
				
				top1[f] = arr[i];
				height1++;
				i--;
				
				if (height1 + height2 == N)
					break;
				
				top2[f] = arr[i];
				height2++;
				f++;
				}
			
			int sum = 0;
			int h1 = 1;
			for (int m = 0; m < top1.length; m++) {
				sum += top1[m] * h1;
				h1++;
			}
			
			int h2 = 1;
			for (int m = 0; m < top2.length; m++) {
				sum += top2[m] * h2;
				h2++;
			}
			sb.append("#").append(t).append(" ").append(sum).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
}
