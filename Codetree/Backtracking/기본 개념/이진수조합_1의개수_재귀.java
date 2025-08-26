import java.util.*;

public class 이진수조합_1의개수_재귀 {
	public static int n = 3, m = 2;
	public static List<Integer> answer = new ArrayList<>();
	
	public static void print() {
		for (int i = 0; i < answer.size(); i++) {
			System.out.print(answer.get(i) + " ");
		}
		System.out.println();
	}
	
	public static void choose(int currNum, int cnt) {
		if (currNum == n + 1) {
			if (cnt == m)
				print();
			return;
		}
		
		answer.add(0);
		choose(currNum + 1, cnt);
		answer.remove(answer.get(answer.size() - 1));
	
		answer.add(1);
		choose(currNum + 1, cnt + 1);
		answer.remove(answer.get(answer.size() - 1));
	}
	
	public static void main(String[] args) {
		choose(1, 1);
	}

}
