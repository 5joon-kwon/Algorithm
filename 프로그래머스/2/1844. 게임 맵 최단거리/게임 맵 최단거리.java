import java.io.*;
import java.util.*;

class Solution {    
    public int[] di = {-1, 0, 1, 0};
    public int[] dj = {0, 1, 0, -1};
    public boolean[][] visited;
    public boolean flag;
    public int count;
    
    public class Pair{
        int i;
        int j;
        int cnt;
        
        Pair(int i, int j, int cnt){
            this.i = i;
            this.j = j;
            this.cnt = cnt;
        }
    }
    
    public void bfs(int i, int j, int[][] maps){
        Queue<Pair> q = new ArrayDeque<>();
        q.add(new Pair(i, j, 1));
        visited[i][j] = true;
        
        while(!q.isEmpty()){
            Pair p = q.poll();
            
            if (p.i == maps.length - 1 && p.j == maps[0].length - 1){
                flag = true;
                count = p.cnt;
                return;
            }
            
            for (int dir = 0; dir < 4; dir++){
                int ni = p.i + di[dir];
                int nj = p.j + dj[dir];
                
                if (ni < 0 || nj < 0 || ni >= maps.length || nj >= maps[0].length)
                    continue;
                
                if (!visited[ni][nj] && maps[ni][nj] == 1){
                    q.add(new Pair(ni, nj, p.cnt + 1));
                    visited[ni][nj] = true;
                }
            }
        }
    }
    
    public int solution(int[][] maps) {
        visited = new boolean[maps.length][maps[0].length];
        flag = false;
        count = 0;

        bfs(0, 0, maps);
        
        if (flag)
            return count;
        else
            return -1;
    }
}