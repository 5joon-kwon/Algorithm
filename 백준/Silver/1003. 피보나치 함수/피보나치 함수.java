import java.util.*;
import java.io.*;

public class Main {	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		int max = 40;
		int[] zero = new int[max + 1];
		int[] one = new int[max + 1];
		
		zero[0] = 1;
		zero[1] = 0;
		one[0] = 0;
		one[1] = 1;
		
		for (int i = 2; i <= max; i++) {
			zero[i] = zero[i - 1] + zero[i - 2];
			one[i] = one[i - 1] + one[i - 2];
 		}
		
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			System.out.println(zero[N] + " " + one[N]);
		}//test
	}//main
}//class
