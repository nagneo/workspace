/* 1. 문자 찾기 */

import java.util.Scanner;

public class Problem01 implements IProblem
{
	@Override
	public void solve()
	{
		Scanner in = new Scanner(System.in);
		String input = in.next();
		char target = in.next().charAt(0);
		in.close();
		
		int result = solution(input, target);
		System.out.println(result);
	}
	
	private int solution(String str, char ch)
	{
		str = str.toLowerCase();
		ch = Character.toLowerCase(ch);
		
		int count = 0;
		for(int i = 0; i < str.length(); i++)
		{
			if(ch == str.charAt(i)) 
			{
				count++;
			}
		}
		
		return count;
	}
}
