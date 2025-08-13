import java.util.*;
import java.io.*;

public class SWEA_5432_쇠막대기_자르기 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			List<Character> arr = new ArrayList<>();
			String line = br.readLine();
			for (int i = 0; i < line.length(); i++) {
				arr.add(line.charAt(i));
			}
			
			int cnt = 0;
			int q = 0;
			
			
			for (int i = 0; i < arr.size() - 1; i++) {
				if (arr.get(i) == '(' && arr.get(i + 1) == ')')
					cnt += q;
				
				else if (arr.get(i) == ')' && arr.get(i + 1) == ')') {
					cnt++;
					q--;
				}
				
				else if (arr.get(i) == '(' && arr.get(i + 1) == '(') {
					q++;
				}
				
				else
					continue;
			}
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(t).append(" ").append(cnt).append("\n");
			System.out.print(sb.toString());
		}

	}

}
