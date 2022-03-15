/* 6. 중복문자제거 */
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

public class Problem06 implements IProblem
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
		Set<Character> set = new LinkedHashSet<Character>();
		
		for(char ch : str.toCharArray())
		{
			if(!set.contains(ch))
			{
				set.add(ch);
			}
		}
		
		String result = "";
		for(char ch : set)
		{
			result += ch;
		}
		
		return result;
	}
}
