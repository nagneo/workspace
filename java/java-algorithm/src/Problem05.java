/* 5. 특정 문자 뒤집기 */

import java.util.Scanner;

public class Problem05 implements IProblem
{
	@Override
	public void solve()
	{
		Scanner in = new Scanner(System.in);
		String input = in.nextLine();
		in.close();
		
		String result = solution(input);
		System.out.println(result);
	}
	
	private String solution(String str)
	{
		String alphabetStr = str.replaceAll("[^A-Za-z]+", "");
		String reversed = new StringBuilder(alphabetStr).reverse().toString();
		
		String result = "";
		int index = 0;
		for(char ch : str.toCharArray())
		{
			if(Character.isLetter(ch))
			{
				result += reversed.charAt(index);
				index++;
			}
			else 
			{
				result += ch;
			}
		}
		
		return result;
	}
}
