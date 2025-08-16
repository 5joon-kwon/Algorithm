import java.util.*;
import java.io.*;

public class SWEA_10761_신뢰 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			
			List<Character> works = new ArrayList<>();
			List<Integer> Olist = new ArrayList<>();
			List<Integer> Blist = new ArrayList<>();
			
			for (int i = 0; i < N; i++) {
				String s = st.nextToken();
				if (s.equals("B")) {
					works.add('B');
					Blist.add(Integer.parseInt(st.nextToken()));
				}
				else {
					works.add('O');
					Olist.add(Integer.parseInt(st.nextToken()));
				}
			}
			
			int widx = 0;
			int op = 1;
			int bp = 1;
			int time = 0;
			int oidx = 0;
			int bidx = 0;
			
			while(widx < works.size()) {
				time++;
				boolean button = false;
				
				if (works.get(widx) == 'O') {
					if (oidx < Olist.size() && op == Olist.get(oidx)) {
						button = true;
						oidx++;
						widx++;

						if (bidx < Blist.size()) {
							if (bp < Blist.get(bidx))
								bp++;
							else if (bp > Blist.get(bidx))
								bp--;
						}
					}
				}
				
				else {
					if (bidx < Blist.size() && bp == Blist.get(bidx)) {
						button = true;
						bidx++;
						widx++;
					
						if (oidx < Olist.size()) {
							if (op < Olist.get(oidx))
								op++;
							else if (op > Olist.get(oidx))
								op--;
						}
					}
				}
				
				if(!button) {
					if (oidx < Olist.size()) {
						if (op < Olist.get(oidx))
							op++;
						else if (op > Olist.get(oidx))
							op--;
					}
					
					if (bidx < Blist.size()) {
						if (bp < Blist.get(bidx))
							bp++;
						else if (bp > Blist.get(bidx))
							bp--;
					}
				}
			}
			sb.append("#").append(t).append(" ").append(time).append("\n");
		} // test
		System.out.print(sb.toString());
	} // main
} // class
