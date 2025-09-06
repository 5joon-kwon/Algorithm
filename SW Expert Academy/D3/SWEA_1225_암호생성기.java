import java.util.*;
import java.io.*;
 
public class SWEA_1225_암호생성기 {
 
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 10; t++) {
            br.readLine();
            LinkedList<Integer> list = new LinkedList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 8; i++) {
                list.add(Integer.parseInt(st.nextToken()));
            }
             
            int i = 1;
            while(true) {
                if (i > 5)
                    i = 1;
                 
                int num = list.poll() - i;
                if (num > 0)
                    list.addLast(num);
                else {
                    list.addLast(0);
                    break;
                }
                i++;
            }
             
            sb.append("#").append(t);       
            for (int x : list)
                sb.append(" ").append(x);
            sb.append("\n");
        } // test
        System.out.print(sb.toString());
    } // main
}