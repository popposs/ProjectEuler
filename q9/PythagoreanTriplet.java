
public class PythagoreanTriplet 
{

	public static void main(String[] args) 
	{
		int af=0;
		int bf=0;
		int cf=0;
		for(int c=5; c<1000; c++)
		{
			for(int b=4; b<c; b++)
				{
					for(int a=3; a<b; a++)
						{
							if(a+b+c==1000 && a*a+b*b==c*c){af=a;bf=b;cf=c;}
						}
				}
		}	
		
			System.out.println(af*bf*cf);
	}
	
	
	

}
