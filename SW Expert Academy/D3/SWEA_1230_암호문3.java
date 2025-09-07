import java.util.*;
import java.io.*;

public class SWEA_1230_암호문3 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for (int t = 1; t <= 10; t++) {
			sb.append("#").append(t);
			int N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());

			LinkedList<String> list = new LinkedList<>();
			for (int i = 0; i < N; i++) {
				list.add((st.nextToken()));
			}

			int M = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				String str = st.nextToken();
				if (str.equals("I")) {
					int x = Integer.parseInt(st.nextToken());
					int y = Integer.parseInt(st.nextToken());
					for (int j = 0; j < y; j++) {
						list.add(x++, st.nextToken());
					}
				} else if (str.equals("D")) {
					int x = Integer.parseInt(st.nextToken());
					int y = Integer.parseInt(st.nextToken());
					for (int j = 0; j < y; j++) {
						list.remove(x++);
					}
				} else {
					int y = Integer.parseInt(st.nextToken());
					for (int j = 0; j < y; j++) {
						list.addLast(st.nextToken());
					}
				}
			}
			for (int i = 0; i < 10; i++) {
				sb.append(" ").append(list.poll());
			}
			sb.append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
}