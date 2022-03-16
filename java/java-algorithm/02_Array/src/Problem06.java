/*reversed prime number*/
import java.util.Scanner;
import java.util.ArrayList;

public class Problem06 {
	
	public void solve() {

		Scanner scanner = new Scanner(System.in);
		int count = scanner.nextInt();
		int[] array = new int[count];
		for(int i = 0; i < count; i++)
		{
			array[i] = scanner.nextInt();
		}
		
		ArrayList<Integer> results = solution(array);
		for(int result : results)
		{			
			System.out.print(result + " ");
		}
	}

	private ArrayList<Integer> solution(int[] array)
	{	
		ArrayList<Integer> result = new ArrayList<>();
		for(int num : array)
		{
			String reversed = (new StringBuilder(num+"").reverse()).toString();
			int reversedInt = Integer.parseInt(reversed);
			if(isPrime(reversedInt))
			{
				result.add(reversedInt);
			}
		}	
		
		return result;
	}

	private boolean isPrime(int num)
	{
		if (num==1) return false;
		for (int i = 2; i < num; i++)
		{
			if (num%i==0) 
			{
				return false;
			}
		}
		return true;
	}
}
