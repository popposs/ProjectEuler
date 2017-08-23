
public class SmallestMultiple 
{

	public static void main(String[] args) 
	{
		int x=1;
		while(!divisible(x))
		{
			x++;
		}
		System.out.println(x);
		
	}
	public static boolean divisible(int x)
	{
		int count=0;
		for(int i=1; i<=20; i++)
		{
			if(x%i==0){count++;}
			if(count==20){return true;}
		}
		return false;
	}
	

}
