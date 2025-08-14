import java.util.*;
import java.io.*;

public class SWEA_14510_나무높이 {

	public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            int[] trees = new int[N];
            int max = 0;

            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(st.nextToken());
                trees[i] = num;
                max = Math.max(max, num);
            }
            
            int cnt1 = 0;
            int cnt2 = 0;
            int res = 0;
            for (int i = 0; i < N; i++) {
            	if (max == trees[i])
            		continue;
            	
				int diff = max - trees[i];
				cnt2 += diff / 2;
				cnt1 += diff % 2;
            }
				
			while (true) {
				if (cnt1 == cnt2 || cnt1 + 1 == cnt2) {
					res = 2 * cnt2;
					break;
				}
				else if (cnt1 > cnt2) {
					res = 2 * cnt1 - 1;
					break;
				}
				else {
					cnt1 += 2;
					cnt2--;
				}
			}
			sb.append("#").append(t).append(" ").append(res).append("\n");
        } // test
        System.out.print(sb.toString());
	} // main
}
