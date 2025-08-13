import java.io.*;
import java.util.*;

public class SWEA_2068_최대수_구하기 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int max = 0;
			for (int i = 0; i < 10; i++) {
				int num = Integer.parseInt(st.nextToken());
				if (max < num)
					max = num;
					
			}
		System.out.printf("#%d %d\n", t, max);
		}
	}
}
