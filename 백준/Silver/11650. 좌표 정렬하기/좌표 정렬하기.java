import java.io.*;
import java.util.*;

public class Main {
	public static class coordi{
		int x;
		int y;
		
		coordi(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<coordi> list = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			list.add(new coordi(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())));
		}
		
		list.sort((c1, c2) -> {
			if (c1.x == c2.x)
				return Integer.compare(c1.y, c2.y);
			else
				return Integer.compare(c1.x, c2.x);
		});
		
		StringBuilder sb = new StringBuilder();
		for (coordi c : list)
			sb.append(c.x).append(" ").append(c.y).append("\n");
		
		System.out.print(sb.toString());
	}
}
