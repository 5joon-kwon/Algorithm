import java.util.*;
import java.io.*;
 
public class SWEA_6808_규영이와_인영이의_카드게임 {
    private static int[] gyu, in;
    private static int win, lose, gscore, iscore;
    private static List<Integer> list;
    private static boolean[] visited;
     
    public static void compare() {
        gscore = 0;
        iscore = 0;
        for (int i = 0; i < 9; i++) {
            int gc = gyu[i];
            int ic = list.get(i);
             
            if (gc > ic)
                gscore += gc + ic;
            else
                iscore += gc + ic;
        }
         
        if (gscore > iscore)
            win++;
        else if (gscore < iscore)
            lose++;
    }
     
    public static void dfs() {
        if (list.size() == 9) {
            compare();
            return;
        }
         
        for (int i = 0; i < 9; i++) {
            if (!visited[i]) {
                list.add(in[i]);
                visited[i] = true;
                dfs();
                list.remove(list.size() - 1);
                visited[i] = false;
            }
        }
         
    }
     
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            gyu = new int[9];
            in = new int[9];
            win = 0;
            lose = 0;
            list = new ArrayList<>();
            visited = new boolean[9];
            boolean[] check = new boolean[19];
             
            for (int i = 0; i < 9; i++) {
                int card = Integer.parseInt(st.nextToken());
                gyu[i] = card;
                check[card] = true;
            }
             
            int j = 0;
            for (int i = 1; i <= 18; i++) {
                if (!check[i]) {
                    in[j] = i;
                    j++;
                }
            }
             
            dfs();
            sb.append("#").append(t).append(" ").append(win).append(" ").append(lose).append("\n");
        }//test
        System.out.print(sb.toString());
    }//main
}//class
