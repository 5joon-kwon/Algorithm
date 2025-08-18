import java.util.*;
import java.io.*;

public class 야구선수 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			
			int[] player = new int[N];
			int max = 0;
			int min = 1001;
			st = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < player.length; i++) {
				int num = Integer.parseInt(st.nextToken());
				player[i] = num;
				max = Math.max(max, num);
				min = Math.min(min, num);
			}
			
			int[] cnt = new int[max + L + 1];
			for (int i = 0; i < player.length; i++) {
				cnt[player[i]]++;
			}
			
			int res = 0;
			for (int i = min; i <= max; i++) {
				int members = 0;
				for (int j = i; j <= i + L; j++) {
					members += cnt[j];
				}
				res = Math.max(res, members);
			}
			sb.append("#").append(t).append(" ").append(res).append("\n");
		} // testcase
		System.out.print(sb.toString());
	} // main
}
