import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Problem10 implements IProblem{

	@Override
	public void solve()
	{	
		Scanner in = new Scanner(System.in);
		String input = in.nextLine();
		String[] strs = input.split(" ");
		String str = strs[0];
		char ch = strs[1].charAt(0);
		
		int[] result = solution(str, ch);
		
		for(int x : result)
		{
			System.out.print(x+" ");
		}
	}

	private int[] solution(String str, char ch)
	{	
		int len = str.length();
		int[] result = new int[len];
		Arrays.fill(result, 100);
		
		List<Integer> posList = new ArrayList<>();
		for(int i = 0; i < len; i++)
		{
			if(str.charAt(i) == ch)
			{
				posList.add(i);
			}
		}
		
		for(int i = 0; i < len; i++)
		{
			for(int pos : posList)
			{
				int distance = Math.abs(pos - i);
				if(result[i] > distance)
				{
					result[i] = distance;
				}
			}
			
			//System.out.println(result[i]);
		}	
		
		return result;
	}
}
