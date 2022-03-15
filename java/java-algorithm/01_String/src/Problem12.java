import java.util.Scanner;

public class Problem12 implements IProblem{

	@Override
	public void solve()
	{
		Scanner in = new Scanner(System.in);
		int count = in.nextInt();
		String input = in.next();
		
		String result = solution(count, input);
		System.out.println(result);
	}
	
	private String solution(int num, String str)
	{
		String result = "";
		for(int i = 0; i < num; i++)
		{
			String current = str.substring(0, 7).replace('#', '1').replace('*', '0');
			int binary = Integer.parseInt(current, 2);
			result += (char)binary;
			str = str.substring(7);
		}
		
		return result;
	}

	@SuppressWarnings("unused")
	private String solution(String input)
	{	
		String[] codes = input.split("(?<=\\G.{7})");
		String result = "";
		for(String str : codes)
		{
			String binary = str.replace('#', '1').replace('*', '0');
			int num = Integer.parseInt(binary, 2);
			result += (char)num;
		}	
		
		return result;
	}	
}
