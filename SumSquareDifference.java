
public class SumSquareDifference 
{

	public static void main(String[] args) 
	{
		int square=0;
		int sum=0;
		for(int i=1; i<=100; i++)
		{
			square+=i*i;
			sum+=i;
		}
		System.out.println(square);
		System.out.println(sum*sum);
		System.out.println(sum*sum-square);
	}

}
