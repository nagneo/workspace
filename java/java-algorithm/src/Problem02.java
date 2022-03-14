/*  2. 대소문자 변환  */

import java.util.Scanner;

public class Problem02 {
	
	public void solve() {
		
		Scanner in = new Scanner(System.in);
		String input = in.next();
		String result = solution(input);
		in.close();
		System.out.println(result);
	}
	
	private String solution(String str)
	{
		String result = "";
		for(char x : str.toCharArray())
		{
			if(Character.isUpperCase(x))
			{
				result += Character.toLowerCase(x);
			}
			else if(Character.isLowerCase(x))
			{
				result += Character.toUpperCase(x);
			}
		}
		
		return result;
	}

}
