/*rock-paper-scissors*/
import java.util.Scanner;

public class Problem03 {

	public void solve()
	{
		Scanner scanner = new Scanner(System.in);
		int count = scanner.nextInt();
		
		int[][] input = new int[2][count];
		for(int i = 0 ; i < 2; i++)
		{
			for(int j = 0; j < count; j++)
			{
				input[i][j] = scanner.nextInt();
			}
		}
		
		char[] results = solution(count, input);
		for(char result : results)
		{			
			System.out.println(result);
		}
	}

	private char[] solution(int num, int[][] input) {
		
		char[] results = new char[num];
		for(int i = 0; i < num; i++)
		{
			if(input[0][i] == input[1][i])
			{
				results[i] = 'D';
			}
			else if(input[0][i] - input[1][i] == -1 || input[0][i] - input[1][i] == 2) 
			{
				results[i] = 'B';
			}
			else if(input[0][i] - input[1][i] == 1 || input[0][i] - input[1][i] == -2)
			{
				results[i] = 'A';
			}
		}
		
		return results;
	}
}
