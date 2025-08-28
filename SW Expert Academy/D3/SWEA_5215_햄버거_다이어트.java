import java.util.*;
import java.io.*;

public class SWEA_5215_햄버거_다이어트 {
	static int cal_sum = 0, best = 0, score_sum = 0;
	static int N, limit;
	static List<Inform> list = new ArrayList<>();

	static class Inform {
		int score;
		int cal;

		Inform(int score, int cal) {
			this.score = score;
			this.cal = cal;
		}
	}

	static void dfs(int start) {
		if (cal_sum > limit)
			return;

		if (start == N) {
			best = Math.max(best, score_sum);
			return;
		}
		
		dfs(start + 1);

		Inform I = list.get(start);
		cal_sum += I.cal;
		score_sum += I.score;
		dfs(start + 1);
		cal_sum -= I.cal;
		score_sum -= I.score;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			limit = Integer.parseInt(st.nextToken());

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				list.add(new Inform(a, b));
			}

			dfs(0);
			sb.append("#").append(t).append(" ").append(best).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
} // class
