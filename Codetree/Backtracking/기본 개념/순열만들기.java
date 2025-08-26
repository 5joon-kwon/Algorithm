import java.util.ArrayList;
import java.util.List;

public class 순열만들기 {
	public static int n = 3;
	public static List<Integer> answer = new ArrayList<>();
	public static boolean[] visited = new boolean[n + 1];
	
	public static void print() {
		for (int i = 0; i < answer.size(); i++) {
			System.out.print(answer.get(i) + " ");
		}
		System.out.println();
	}
	
	public static void choose(int currNum) {
		if (currNum == n + 1) {
			print();
			return;
		}
		
		for (int i = 1; i <= n; i++) {
			if (visited[i])
				continue;
			
			visited[i] = true;
			answer.add(i);
			
			choose(currNum + 1);
			
			answer.remove(answer.get(answer.size() - 1));
			visited[i] = false;
		}
	}
	
	public static void main(String[] args) {
		choose(1);
	}

}
