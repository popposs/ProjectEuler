
public class FibonacciNum 
{
	public static void main(String[] args) 
	{
		int sum=0;
		int counter=0;
		int current;
		while(sum<4000000)
		{
			current=fib(counter);
			if(current%2==0){sum+=current;};
			counter++;
		}
		System.out.println(sum);
		
	}
	
	public static int fib(int x)
	{
		if(x==0)return 1;
		if(x==1)return 2;
		return fib(x-1)+fib(x-2);
	}

}
