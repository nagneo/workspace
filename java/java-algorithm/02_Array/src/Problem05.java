/*Prime number(Eratosthenes' sieve)*/
import java.util.Scanner;

public class Problem05 {

	public void solve()
	{
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		
		System.out.println(solution(n));
	}
	
	public int solution(int n)
	{
		int cnt=0;
		int[] ch = new int[n+1];
		
		for(int i=2; i<=n; i++)
		{
			if (ch[i]==0)
			{
				cnt++;
				for (int j=i; j<=n; j=j+i)
				{
					ch[j]=1;
				}
			}
		}
		
		return cnt;
	}
}
