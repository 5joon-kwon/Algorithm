import java.util.Scanner;
public class SWEA_1217_거듭제곱 {
	static int power(int N, int M) {
		if (M == 0)
			return 1;
		
		if (M % 2 == 0) {
			int res = power(N, M / 2);
			return res * res;
		}
		else {
			int res = power(N, (M - 1) / 2);
			return res * res * N;
		}
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		for (int t = 0; t < 10; t++) {
			int T = scanner.nextInt();
			int N = scanner.nextInt();
			int M = scanner.nextInt();
			
			System.out.println("#" + T + " " + power(N, M));
		}
	}

}
