/* 7. 회문 문자열 */

import java.util.Scanner;


public class Problem07 {

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
		int len = str.length();
		str = str.toLowerCase();
		for(int i = 0; i < len / 2; i++)
		{
			if(str.charAt(i) != str.charAt(len-1-i))
			{
				return false;
			}
		}
		
		return true;
	}
}
