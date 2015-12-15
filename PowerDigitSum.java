import java.math.BigInteger;
import java.util.ArrayList;


public class PowerDigitSum {

	public static void main(String[] args) {
		
		ArrayList<BigInteger> pds=new ArrayList<BigInteger>();
		pds.add(BigInteger.valueOf(2).pow(1000));
		System.out.println("Answer: " + sum(pds,0).subtract(pds.get(0)));
		
		
	
	}
	
	public static BigInteger sum(ArrayList<BigInteger> m, int index){
		if(m.get(0).compareTo(BigInteger.valueOf(10))==-1){m.set(0, BigInteger.valueOf(0)); return BigInteger.valueOf(1);}
		m.add(m.get(0).mod(BigInteger.valueOf(10)));
		BigInteger temp=m.get(0).divide(BigInteger.valueOf(10)); 
		m.set(0, temp); System.out.println(m.get(index));
		return sum(m, index+1).add(m.get(index));
	}

}
