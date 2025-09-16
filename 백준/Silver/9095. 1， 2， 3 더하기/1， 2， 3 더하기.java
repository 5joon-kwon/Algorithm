import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int n = Integer.parseInt(br.readLine());
			int[] dp = new int[11];
			dp[0] = 1;
			dp[1] = 1;
			dp[2] = 2;
			
			for (int i = 3; i <= n; i++) 
				dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
			
			System.out.println(dp[n]);
		}//test
	}//main
}//class