
public class Palindrome {

	public static void main(String[] args) 
	{
		int palindrome=0;
		for(int i=100; i<1000; i++)
		{
			for(int j=100; j<1000; j++)
			{
				if(isPalindrome(i*j) && i*j>palindrome)
					{palindrome=i*j; System.out.println(palindrome);}}
			}
		}
	public static boolean isPalindrome(int i)
	{
		String num=String.valueOf(i);
		for(int j=0; j<num.length()/2;j++)
		{
			if(!num.substring(j,j+1).equals(num.substring(num.length()-j-1,num.length()-j))){return false;};
		}
		return true;
	}

}
