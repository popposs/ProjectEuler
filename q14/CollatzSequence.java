import java.util.LinkedList;

public class CollatzSequence
{
	public static void main(String[] args)
	{		
		LinkedList<Long> list=new LinkedList<Long>();
	 
		long length=0;
		int result=0;
	 
		for(int j=10; j<1000000; j++)
		{
			long i=j;
			
			while (i!=1)
			{
				if (i%2==0)
				{	i/=2;
					list.add(i);}
				else
				{	i=(3*i)+1;
					list.add(i);}
			}
			
			if(list.size()>length)
			{	length=list.size();
				result=j;}
			list.clear();
		}
	 
		System.out.println(result+" with chain size: "+ length);
	}
}