import java.util.*;
import java.io.*;

public class 퍼펙트_셔플 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			sb.append("#").append(t);
			int N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int n = 0;
			if (N % 2 == 0)
				n = N / 2;
			else
				n = N / 2 + 1;
			
			String[] card1 = new String[n];
			String[] card2 = new String[N - n];
			
			for (int i = 0; i < n; i++)
				card1[i] = st.nextToken();
			
			for (int i = 0; i < N - n; i++)
				card2[i] = st.nextToken();
			
			for (int i = 0; i < n; i++) {
				if (N % 2 != 0 && i == n - 1) {
					sb.append(" ").append(card1[i]);
					break;
				}
				
				sb.append(" ").append(card1[i]).append(" ").append(card2[i]);
			}
			sb.append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
}
