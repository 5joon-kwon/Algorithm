import java.io.*;
import java.util.*;

public class Main {
	public static class member{
		int age;
		String name;
		
		member(int age, String name){
			this.age = age;
			this.name = name;
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<member> list = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			list.add(new member(Integer.parseInt(st.nextToken()), st.nextToken()));
		}
		
		list.sort((m1, m2) -> Integer.compare(m1.age, m2.age));
		
		for (member a : list)
			System.out.println(a.age + " " + a.name);
	}
}
