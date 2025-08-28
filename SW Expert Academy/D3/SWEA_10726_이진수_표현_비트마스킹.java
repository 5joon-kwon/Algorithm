import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class SWEA_10726_이진수_표현_비트마스킹 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int bm = (1 << N) - 1;			
			sb.append("#").append(t).append(" ").append((bm & M) == bm ? " ON\n" : " OFF\n");
		} // test
		System.out.print(sb.toString());
	} // main
} // class
