import java.math.BigInteger;


public class LargestProductGrid 
{

	public static void main(String[] args) 
	{
		//replace first number in list with another to work
		BigInteger num=new BigInteger("08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748");
		String grid=String.valueOf(num);
		Integer current=0;
		int tracker=0;
		int largestProduct=1;
		Integer[][] arrayNum=new Integer[20][20];
		
		for(int row=0; row<20; row++)
		{
			for(int col=0; col<20; col++)
			{
				
				current=Integer.valueOf(grid.substring(tracker, tracker+2)); 
				System.out.println(current);arrayNum[row][col]=current;
				if(tracker!=796){tracker+=2;}
				
			}
		}
		System.out.println(arrayNum[0][0]);
		
		for(int row=0; row<20; row++)
		{
			for(int col=0; col<20-3; col++)
			{
				current=arrayNum[row][col]
						*arrayNum[row][col+1]
						*arrayNum[row][col+2]
						*arrayNum[row][col+3];
				if(current>largestProduct){largestProduct=current;}
					
			}
		}
		
		for(int row=0; row<20-3; row++)
		{
			for(int col=0; col<20-3; col++)
			{
				current=arrayNum[row][col]
						*arrayNum[row+1][col]
						*arrayNum[row+2][col]
						*arrayNum[row+3][col];
				if(current>largestProduct){largestProduct=current;}
					
			}
		}
		
		for(int row=0; row<20-3; row++)
		{
			for(int col=0; col<20-3; col++)
			{
				current=arrayNum[row][col]
						*arrayNum[row+1][col+1]
						*arrayNum[row+2][col+2]
						*arrayNum[row+3][col+3];
				if(current>largestProduct){largestProduct=current;}
					
			}
		}
		
		for(int row=0; row<20-3; row++)
		{
			for(int col=3; col<20-3; col++)
			{
				current=arrayNum[row][col]
						*arrayNum[row+1][col-1]
						*arrayNum[row+2][col-2]
						*arrayNum[row+3][col-3];
				if(current>largestProduct){largestProduct=current;}
					
			}
		}
		
		System.out.println(largestProduct);


	}

}
