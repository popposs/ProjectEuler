import java.util.ArrayList;


public class LPrimeFactor 
{

	public static void main(String[] args) 
	{
		ArrayList<Long> list=new ArrayList<Long>();
		long num=600851475143l;
		for(long i=2; i<num; i++)
		{
			if(num%i==0){num/=i;}
		}
		System.out.println(num);
		

	}

}
