import java.util.*;
import java.io.*;
/*
 * 그래프 탐색 : DFS, BFS
 * DFS stack : 반복문, 재귀함수 (장점 : 지금까지의 연산결과를 들고다닌다 => 중복 연산 제거)
 */

public class SWEA_1952_수영장 {
	private static int valDay, val1Month, val3Month, valYear, minVal;
	private static int[] use;

	/** 매달 선택할 수 있는, 구매 옵션 선택 후 다음 달로 넘어가는 재귀함수 
	 * month : 달 선택하기, val : 이전 달까지 지불한 이용권 비용*/
	private static void dfs(int month, int val) { // depth 체크 (month), 계산 결과 (option)
		if (minVal <= val)
			return;
		
		if (month > 12) {
			// 그동안 선택한 내용에 해당하는 비용
			minVal = Math.min(minVal, val);
			return;
		}
		
		if (use[month] == 0) { 	// 이번 달 이용 X
			dfs(month + 1, val); // 다음 달로 넘어가기
		}
		
		dfs(month + 1, val + valDay * use[month]); // 1일 옵션
		dfs(month + 1, val + val1Month); // 1달 옵션
		dfs(month + 3, val + val3Month); // 3달 옵션
//		dfs(month + 12, val + valYear); // 1년 옵션 => 1월에만 1년 옵션 쓰기 (이걸 minVal 의 초기값으로 하기)
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			valDay = Integer.parseInt(st.nextToken());
			val1Month = Integer.parseInt(st.nextToken());
			val3Month = Integer.parseInt(st.nextToken());
			valYear = Integer.parseInt(st.nextToken());
//			minVal = Integer.MIN_VALUE;
			minVal = valYear;
			
			use = new int[13];
			st = new StringTokenizer(br.readLine(), " ");
			for (int i = 1; i < use.length; i++) {
				use[i] = Integer.parseInt(st.nextToken());
			}
			
			dfs(1, 0); // 1월부터 출발, 비용 0
			
			sb.append("#").append(t).append(" ").append(minVal).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
} // class
