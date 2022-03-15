import java.util.Scanner;

public class Problem09 implements IProblem
{
	@Override
	public void solve()
	{	
		Scanner in = new Scanner(System.in);
		String input = in.next();
		
		int result = solution(input);
		System.out.println(result);
	}

	private int solution(String str)
	{	
		String numString = str.replaceAll("[^0-9]+", "");
		numString = new StringBuilder(numString).reverse().toString();
		int digit = 0;
		int result = 0;
		for(char ch : numString.toCharArray())
		{
			int current =  Character.getNumericValue(ch) * (int)Math.pow(10, digit);
			result += current;
			digit++;
		}
		
		return result;
	}	
}
