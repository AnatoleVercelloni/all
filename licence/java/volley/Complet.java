public class Complet extends Alier implements Attaquant{
	 
	public Complet(String nom){
		super(nom);
	}
	
	public Complet copie(){
		return new Complet(nom);
	}
	
	public String toString(){
		return "Le complet "+nom;
	}
	
	public int reception(){
		fatigue = fatigue + 1;
		System.out.println(toString()+" receptionne la balle");
		return Operation.probabilite(0.9-fatigue/10);
	}
	
	public int servir(){
		System.out.println(toString()+" sert");
		fatigue = fatigue + 1;
		return Operation.probabilite(0.7-fatigue/10);
	}
}
	