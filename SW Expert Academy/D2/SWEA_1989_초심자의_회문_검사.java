import java.io.*;

public class SWEA_1989_초심자의_회문_검사 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			String str = br.readLine();
			
			StringBuilder sb = new StringBuilder(str);
			String rev = sb.reverse().toString();
			
			if (rev.equals(str))
				System.out.println("#" + t + " " + 1);
			else
				System.out.println("#" + t + " " + 0);
		}
	}

}
