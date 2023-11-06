public class Arbre extends Ressource{
	private boolean b;
	private static int nbArbre = 0;
	
	public Arbre (){
		super("arbre",(int)(Math.random()*5)+5);
		b=false;
		nbArbre = nbArbre+1;
		
	}
	
	
	
	public void AttaqueDeCastor(){
		setQuantite(0);
	}
	
	
	
	public boolean getAUnCastor(){
		return b;
	}
	
	public void setAUnCastor(boolean p){
		b=p;
	}
	
	public int getNbArbre(){
		return nbArbre;
	}
	
	public String toString(){
		
		return "il y a un arbre avec "+getQuantite()+" branches en ["+getY()+","+getX()+"]";
		
	}
	
	
	
	
}
	
	