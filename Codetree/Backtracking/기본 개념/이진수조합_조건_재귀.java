import java.util.ArrayList;
import java.util.List;

public class 이진수조합_조건_재귀 {
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
		
		// 0 선택 시 조건 고려
		if (currNum == 1 || answer.get(answer.size() - 1) != 0) {
			answer.add(0);
			choose(currNum + 1);
			answer.remove(answer.size() - 1);
		}
		
		answer.add(1);
		choose(currNum + 1);
		answer.remove(answer.size() - 1);

		
		return;
	}
	
	public static void main(String[] args) {
		choose(1);		
	}

}
