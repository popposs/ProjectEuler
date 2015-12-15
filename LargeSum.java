import java.math.BigInteger;
import java.util.Scanner;


public class LargeSum 
{
	private static BigInteger sum=new BigInteger("0");
	private static String in="";
	private static int i=1;
	
	public static void main(String args[])
	{
		Scanner c=new Scanner(System.in);
		System.out.print("Enter: ");
		in=c.next();
		System.out.println();
		for(int i=0; i<100; i++)
		{
			increment();
		}
		System.out.println("Answer is " + sum);
	}
	
	public static String tenDigitNumber()
	{
		String number="";
		for(int j=0; j<50; j++)
		{
			if(i%50==0){number+=in.charAt(i-1); i++; break;} 
			number+=in.charAt(i-1);
			i++;
		}
		System.out.println(i);
		return number;
	}
	
	public static void increment()
	{
		sum.add(new BigInteger(tenDigitNumber()));
	}

}


