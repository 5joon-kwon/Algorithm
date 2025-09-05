import java.util.*;
import java.io.*;

public class SWEA_14229_백만_개의_정수_정렬 {
	static int[] arr;
	static int MAX_VALUE = 1_000_000;
	static int[] tmp = new int[MAX_VALUE];
	
	public static void mergeSort(int start, int end) {
		if (start >= end)
			return;
		
		int mid = (start + end) / 2;
		mergeSort(start, mid);
		mergeSort(mid + 1, end);
		merge(start, mid, end);
	}
	
	public static void merge(int start, int mid, int end) {
		int L = start;
		int R = mid + 1;
		int idx = start;
		
		while(L <= mid && R <= end) {
			if (arr[L] <= arr[R])
				tmp[idx++] = arr[L++];
			else
				tmp[idx++] = arr[R++];
		}
		
		while (L <= mid) {
			tmp[idx++] = arr[L++];
		}
		
		while (R <= end){
			tmp[idx++] = arr[R++];
		}
		
		System.arraycopy(tmp, start, arr, start, end - start + 1);
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr = new int[MAX_VALUE];
		for (int i = 0; i < MAX_VALUE; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		mergeSort(0, MAX_VALUE - 1);
		System.out.println(arr[500000]);
	} // main
} // class
