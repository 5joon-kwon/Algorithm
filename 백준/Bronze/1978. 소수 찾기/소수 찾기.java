import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int cnt = 0;
		
		for (int x : arr) {
			int flag = 0;
			
			if (x == 1)
				continue;
			
			for (int j = 2; j <= Math.pow(x, 0.5); j++) {
				if (x % j == 0) {
					flag = 1;
					break;
				}
			}
			
			if (flag == 0)
				cnt++;
		}
		System.out.println(cnt);
	}
}
