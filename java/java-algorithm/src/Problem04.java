/*  4. 단어 뒤집기  */
import java.util.Scanner;

public class Problem04 implements IProblem
{
	@Override
	public void solve()
	{
		Scanner in = new Scanner(System.in);
		int count = in.nextInt();
		String[] array = new String[count];
		
		for (int i = 0; i < count; i++)
		{
			array[i] = in.next();
		}
		
		in.close();
		
		String[] result = solution(array);
		for(String str: result)
		{
			System.out.println(str);
		}
	}
	
	private String[] solution(String[] array)
	{
		int len = array.length;
		String[] result = new String[len];
		
		for (int i = 0; i < len; i++)
		{
			String current = array[i];
			result[i] = new StringBuilder(current).reverse().toString();
		}
		
		return result;
	}
}
