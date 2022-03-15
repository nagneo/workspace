/*  3. 문장 속 단어  */

import java.util.Scanner;

public class Problem03 implements IProblem
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
		String[] words = str.split(" ");
		
		int maxLength = -1;
		String result = "";
		for(String word : words)
		{
			if(word.length() > maxLength)
			{
				result = word;
				maxLength = word.length();
			}
			
		}
		
		return result;
	}
}
