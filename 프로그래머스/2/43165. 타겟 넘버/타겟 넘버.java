import java.util.*;
import java.io.*;

class Solution {
    public int cnt = 0;

    public void dfs(int start, int[] numbers, int sum, int target){
        if (start == numbers.length){
            if (sum == target)
                cnt++; 
            return;
        }
        
        int temp = numbers[start];
        
        numbers[start] = -temp;
        dfs(start + 1, numbers, sum - 2 * temp, target);

        numbers[start] = temp;
        dfs(start + 1, numbers, sum, target);
    }
    
    public int solution(int[] numbers, int target) {
        int sum = 0;
        for (int n : numbers)
            sum += n;
        
        dfs(0, numbers, sum, target);
        return cnt;
    }
}