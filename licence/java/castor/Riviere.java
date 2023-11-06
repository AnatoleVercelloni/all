public class Riviere{
	private int largeur;
	private int position;
	private int debit;
	
	public Riviere(int l, int x){
		largeur = l;
		position = x;
		debit = 5;
	}
	
	public int getLargeur(){
		return largeur;
	}
	
	public int getPosition(){
		return position;
	}
	
	public int getDebit(){
		return debit;
	}
	
	
	public void setDebit(){
		int x = (int)(Math.random()*100)+1;
		if (x==1){
			debit=0;
		}
		if ((x>1)&(x<=3)){
			debit=1;
		}
		if ((x>3)&(x<=10)){
			debit=2;
		}
		if ((x>10)&(x<=30)){
			debit=3;
		}
		if ((x>30)&(x<=70)){
			debit=4;
		}
		if ((x>70)&(x<=90)){
			debit=5;
		}
		if ((x>90)&(x<=97)){
			debit=6;
		}
		if ((x>97)&(x<=99)){
			debit=7;
		}
		if (x==100){
			debit=8;
		}
	}
	
	public String toString(){
		return "la riviere a un debit de "+debit;
	}
		
		
		
}
	