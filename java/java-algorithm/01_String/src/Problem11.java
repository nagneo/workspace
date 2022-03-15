import java.util.Scanner;

public class Problem11 implements IProblem{

	@Override
	public void solve()
	{
		Scanner in = new Scanner(System.in);
		String str = in.nextLine();
		
		String result = solution(str);
		System.out.println(result);
	}

	private String solution(String str)
	{	
		String result = "";
		for(int i = 0; i < str.length();)
		{
			int duplicatedCount = 1;
			int next = 1;
			if(i+next < str.length())
			{
				while(str.charAt(i) == str.charAt(i+next))
				{
					duplicatedCount++;
					next++;
					
					if(i+next == str.length())
					{
						break;
					}
				}
			}
			
			result += str.charAt(i);
			if(duplicatedCount > 1)
			{
				result += duplicatedCount;
			}
			
			i = i + next;
		}
		
		return result;
	}

}
