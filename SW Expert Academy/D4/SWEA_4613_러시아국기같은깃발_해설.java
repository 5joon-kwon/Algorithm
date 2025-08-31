
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.StringTokenizer;

public class N4613_러시아국기같은깃발_강사님ver {
	private static int[][] map;
	private static int M;

	/*
	 * 두개의 영역만 고르기 흰 0~i 파 i~j 빨 j~N
	 * 
	 * i j 범위 1 <= i < N-1 i <= j < N
	 * 
	 * n-2 C 2 조합문제, nCr에서 r값이 고정이면 반복문으로 구현할 수 있다. 3개의 영역으로 나누는데 구분할 두개의 행 i, j를
	 * 결정하자 각 줄의
	 */
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int TC = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= TC; testCase++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken()); // 행, 3 이상 50 이하
			M = Integer.parseInt(st.nextToken()); // 열, 3 이상 50 이하

			// 각 행에 들어간 색깔의 개수
			map = new int[N][3]; // [i번째행][0:W, 1:B, 2:R]
			for (int i = 0; i < N; i++) { // 행
				String s = br.readLine(); // WWWRBWBB
				for (int j = 0; j < M; j++) { // 열
					char c = s.charAt(j);
					switch (c) {
					case 'W':
						map[i][0]++;
						break;
					case 'B':
						map[i][1]++;
						break;
					case 'R':
						map[i][2]++;
						break;

					default:
						break;
					}

				}

			}

			// 3개의 영역으로 나누자 i, j 1~N-1 숫자 중 2개를 뽑으면 됨. n-2C2 조합문제
//          W : 0행 <= W < i행
//    		B : i행 <= B < j행
//    		R : j행 <= w < N행
			int minCnt = Integer.MAX_VALUE;
			for (int i = 1; i < N - 1; i++) {
				for (int j = i; j < N; j++) {
					// 각 영역이 정해지면 바꿔야되는 색깔의 개수 카운팅, 최소값을 업데이트
					int w = cntChar(0, i, 'W');
					int b = cntChar(i, j, 'B');
					int r = cntChar(j, N, 'R');
					minCnt = Math.min(minCnt, w + b + r);
				}
			}

			sb.append("#").append(testCase).append(" ").append(minCnt).append("\n");
		} // end for testCase
		System.out.print(sb.toString());
	}

	// s행 이상 e미만 범위에서 c글자로 변경시 바뀌어야하는 글자수 리턴
	public static int cntChar(int s, int e, int c) {
		int cnt = 0;
		for (int i = s; i < e; i++) {
			switch (c) {
			case 'W':
				cnt += map[i][1] + map[i][2];
//				cnt += M - map[i][0];

				break;
			case 'B':
				cnt += map[i][0] + map[i][2];
				break;
			case 'R':
				cnt += map[i][0] + map[i][1];
				break;

			}
		}
		return cnt;

	} // end of main

} // end of class
