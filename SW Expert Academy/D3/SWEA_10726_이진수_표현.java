import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class SWEA_10726_이진수_표현 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			boolean flag = true;
			
			List<Integer> list = new ArrayList<>();
			while (true) {
				if (M <= 1) {
					list.add(M);
					break;
				}
				
				list.add(M % 2);
				M = M / 2;
			}
			
			if (N > list.size()) {
				sb.append("#").append(t).append(" ").append("OFF").append("\n");
				continue;
			}
			
			for (int i = 0; i < N; i++) {
				if (list.get(i) != 1) {
					sb.append("#").append(t).append(" ").append("OFF").append("\n");
					flag = false;
					break;
				}
			}
			
			if (flag)
				sb.append("#").append(t).append(" ").append("ON").append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
} // class
