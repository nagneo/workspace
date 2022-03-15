import java.util.Scanner;
import java.util.ArrayList;

public class Problem01 {

	public void solve()
	{
		Scanner in = new Scanner(System.in);
		
		int count = in.nextInt();
		
		int[] arr = new int[count];
		for (int i = 0; i < count; i++)
		{
			arr[i]=in.nextInt();
		}
		
		ArrayList<Integer> result = solution(count, arr);
		for(int n : result)
		{
			System.out.print(n + " ");
		}
	}

	private ArrayList<Integer> solution(int num, int[] arr) {
		
		ArrayList<Integer> results = new ArrayList<>();
		results.add(arr[0]);
		for (int i = 1; i < num; i++)
		{
			if(arr[i] > arr[i-1])
			{
				results.add(arr[i]);
			}
		}
		
		return results;
	}

	
}
