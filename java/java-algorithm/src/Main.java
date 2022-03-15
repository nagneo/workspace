import java.util.Scanner;

public class Main
{
	public static void main(String[] args)
	{	
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int number = in.nextInt();
		
		IProblem problem = GetProblem(number);
		if(problem != null)
		{
			problem.solve();
		}
		
		return;
	}
	
	private static IProblem GetProblem(int num)
	{
		IProblem problem = null;
		switch(num)
		{
			case 1: 
				problem = new Problem01();
				break;
			case 2:
				problem = new Problem02();
				break;
			case 3:
				problem = new Problem03();
				 break;
			case 4:
				problem = new Problem04();
				break;
			case 5:
				problem = new Problem05();
				break;
			case 6:
				problem = new Problem06();
				break;
			case 7:
				problem = new Problem07();
				break;
			case 8:
				problem = new Problem08();
				break;
			case 9:
				problem = new Problem09();
				break;
			case 10:
				problem = new Problem10();
				break;
			case 11:
				problem = new Problem11();
				break;
			case 12:
				problem = new Problem12();
				break;
			default:
				System.out.println("Invalid Number");
				break;
		}
		
		return problem;
	}
}
