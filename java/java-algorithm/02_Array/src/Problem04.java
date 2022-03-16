/*Fibonacci*/
import java.util.Scanner;

public class Problem04 {
	
	public void solve() {
		
		Scanner scanner = new Scanner(System.in);
		int count = scanner.nextInt();
		
		int[] result = solution(count);
		for(int x :result) 
		{
			System.out.print(x+" ");
		}
	}

	private int[] solution(int count) {
		
		int [] result = new int[count];
		result[0] = 1;
		result[1] = 1;
		
		for(int i = 2; i < count; i++)
		{
			result[i] = result[i-1] + result[i-2];
		}
		
		return result;
	}

}
