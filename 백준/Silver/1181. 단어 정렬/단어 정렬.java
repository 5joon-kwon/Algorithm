import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		Set<String> set = new HashSet<>();
		for (int i = 0; i < N; i++) {
			set.add(br.readLine());
		}
		
		String[] arr = set.toArray(new String[0]);

		List<String>[] list = new ArrayList[51];
		for (int i = 0; i <= 50; i++) {
			list[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < set.size(); i++) {
			list[arr[i].length()].add(arr[i]);
		}
		
		for (List<String> s : list) {
			Collections.sort(s);
		}
		
		for (int i = 1; i <= 50; i++) {
			for (String s : list[i])
				System.out.println(s);
		}
		
	}
}
