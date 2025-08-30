import java.util.*;
import java.io.*;

public class SWEA_1218_괄호_짝짓기 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int t = 1; t <= 10; t++) {
			int N = Integer.parseInt(br.readLine());
			Stack<Character> stack = new Stack<>();
			char[] arr = br.readLine().toCharArray();
			
			int flag = 1;
			
			for (int i = 0; i < N; i++) {
				char c = arr[i];
				
				if (c == '(' || c == '{' || c == '[' || c == '<')
					stack.push(c);
				else {
					if (stack.isEmpty()) {
						flag = 0;
						break;
					}
					
					char top = stack.pop();
					
					if ((c == ')' && top != '(') ||
						(c == '}' && top != '{') ||
						(c == ']' && top != '[') ||
						(c == '>' && top != '<')) {
						flag = 0;
						break;
					}
				}	
			}
			
			if (!stack.isEmpty())
				flag = 0;

			sb.append("#").append(t).append(" ").append(flag).append("\n");
		}
		System.out.print(sb.toString());
	}

}
