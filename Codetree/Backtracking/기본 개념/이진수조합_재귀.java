import java.util.*;

public class 이진수조합_재귀 {
	public static int n = 3;
	public static List<Integer> answer = new ArrayList<>();

	public static void printAnswer() {
		for (int i = 0; i < answer.size(); i++)
			System.out.print(answer.get(i) + " ");
		System.out.println();
	}
	
	public static void choose(int currNum) {
		if (currNum == n + 1) {
			printAnswer();
			return;
		}
		
		for (int i = 0; i < 2; i++) {
			answer.add(i);
			choose(currNum + 1);
			answer.remove(answer.size() - 1);
		}
		
		return;
	}
	
	public static void main(String[] args) {
		choose(1);		
	}

}
