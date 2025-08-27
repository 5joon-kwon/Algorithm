import java.util.*;
import java.io.*;

public class Main {
    static List<Integer> answer = new ArrayList<>();
    static boolean[] visited;
    static int N, M;

    static void print() {
        for (int x : answer) 
	        System.out.print(x + " ");
        System.out.println();
    }

    static void choose() {                 // ← c 제거
        if (answer.size() == M) {          // 길이 M이면 출력
            print();
            return;
        }
        
        for (int i = 1; i <= N; i++) {     // 매 단계에서 1..N 전체 탐색
            if (!visited[i]) {
                visited[i] = true;
                answer.add(i);

                choose();                  // 다음 자리 채우기

                answer.remove(answer.size() - 1);
                visited[i] = false;        // 복구
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new boolean[N + 1];

        choose();
    }
}
