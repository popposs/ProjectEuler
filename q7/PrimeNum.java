
public class PrimeNum 
{

	public static void main(String[] args) 
	{
		int count=1;
		int prime=2;
		while(count!=10001)
		{
			prime++;
			if(prime(prime)){System.out.println(prime); count++;}
		}

	}
	
	public static boolean prime(int x)
	{
		for(int i=2; i<x; i++)
		{
			if(x%i==0){return false;}
		}
		return true;
	}

}
