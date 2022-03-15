/* 8. 유효한 팰린드롬 */
import java.util.Scanner;

public class Problem08 implements IProblem
{
	@Override
	public void solve()
	{
		Scanner in = new Scanner(System.in);
		String input = in.nextLine();
		in.close();
		
		boolean result = solution(input);
		System.out.println(result == true ? "YES" : "NO");
	}
	
	private boolean solution(String str)
	{
		str = str.toLowerCase().replaceAll("[^A-Za-z]+", "");
		int len = str.length();
		for(int i = 0; i < len / 2; i++)
		{
			if(str.charAt(i) != str.charAt(len - i - 1))
			{
				return false;
			}
		}

		return true;
	}
}
