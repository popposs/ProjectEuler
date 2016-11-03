import java.math.BigInteger;


public class LatticePathsDP {

	public static void main(String[] args) {
		BigInteger[][] grid=new BigInteger[21][21];
		
		for(int i=0; i<grid[0].length; i++){
			for(int j=0; j<grid.length; j++){
				grid[i][j]=BigInteger.valueOf(0);
			}
		}
		
		for(int i=0; i<grid[0].length; i++){
			for(int j=0; j<grid.length; j++){
				if(i==0 && j==0){grid[i][j]=BigInteger.valueOf(1); continue;}
				BigInteger n=BigInteger.valueOf(i-1), m=BigInteger.valueOf(j-1); //n is x coordinate, m is y coordinate
				if(n.compareTo(BigInteger.valueOf(0))<0){n=BigInteger.valueOf(0);}
				if(m.compareTo(BigInteger.valueOf(0))<0){m=BigInteger.valueOf(0);}
				grid[i][j]=grid[n.intValue()][j].add(grid[i][m.intValue()]);
				System.out.println(grid[i][j]);
			}
		}
		System.out.println(grid[20][20]);
		
	}
	

}
