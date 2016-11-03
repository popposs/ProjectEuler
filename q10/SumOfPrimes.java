
public class SumOfPrimes {

	public static void main(String[] args) {
		long sum=0l;
		int counter=2;
		while(counter<2000000 && counter>0)
		{
			if(isPrime(counter)){sum+=counter; System.out.println(sum);}
			counter++;
		}
		System.out.println("Sum: " + sum);
	}
	
	public static boolean isPrime(int x)
	{
		for(int i=2; i<x; i++)
		{
			if(x%i==0){return false;}
		}
		return true;
	}

}
