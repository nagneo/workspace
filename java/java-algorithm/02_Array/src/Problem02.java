import java.util.Scanner;

public class Problem02 {
	
	public void solve() {
		Scanner in = new Scanner(System.in);
		int num = in.nextInt();
		
		int[] array = new int[num];
		for(int i = 0; i < num; i++)
		{
			array[i] = in.nextInt();
		}
		
		int result = solution(array);
		System.out.println(result);
	}

	private int solution(int[] arr) {
		
		int result = 0;
		int max = 0;
		for(int height : arr)
		{
			if(max < height)
			{
				result++;
				max = height;
			}
		}
		
		return result;
		
	}

}
