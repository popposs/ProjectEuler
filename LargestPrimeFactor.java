public class LargestPrimeFactor 
{

	public static void main(String[] args) 
	{
		System.out.println(primeFactor(600851475143L));

	}
	
	public static long primeFactor(long x)
	{
		for(long i=x-1; i>0; i--)
		{
			System.out.println(i);
			if(prime(i) && x%i==0){return i;}
		}
		return -1;
	}
	public static boolean prime(long i2)
	{
		for(int i=2; i<i2; i++)
		{
			if(i2%i==0){return false;}
		}
		return true;
	}
	

}


