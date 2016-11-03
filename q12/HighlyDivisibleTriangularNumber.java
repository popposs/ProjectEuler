
public class HighlyDivisibleTriangularNumber 
{
	public static int count=1;
	public static int numDivisors=500; //# of divisors to look for
	public static int divisors=0;
	
	public static void main(String[] args) 
	{
		
		System.out.println("Highly Divisible Triangular Number= " + triangleNumber(1));
		System.out.println("Numbers of Divisors: " + divisors);
	}
	
	public static boolean FiveDivisors(int d)
	{
		divisors=0;
		int sqrt=(int)Math.sqrt(d);
		for(int i=1; i<=sqrt; i++)
		{
			if(d%i==0){divisors+=2;}
			if(divisors==numDivisors){return true;}
		}
		if(sqrt*sqrt==d){divisors--;}
		if(divisors>numDivisors){return true;}//divisors==number of divisors
		return false;
	}
	
	public static int triangleNumber(int c)
	{
	
		if(FiveDivisors(c)){return c;}
		count++;
		return triangleNumber(c+count);
		
	}
	
}
