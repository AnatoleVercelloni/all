public class Centraux extends Joueur implements Attaquant{
	
	public Centraux(String nom){
		super(nom);
		
	}
	
	public Centraux copie(){
		return new Centraux(nom);
	}
	
	public String toString(){
		return "Le Central "+nom;
	}
	
	public int reception(){
		System.out.println(toString()+" receptionne la balle");
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int contre(){
		
		return Operation.probabilite(0.6-fatigue/10);
	}
	
	public int smash(){
		System.out.println(toString()+" smash");
		fatigue = fatigue + 1;
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int passe(){
		fatigue = fatigue + 1;
		System.out.println(toString()+" fait une passe");
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int servir(){
		fatigue = fatigue + 1;
		System.out.println(toString()+" sert");
		return Operation.probabilite(0.7-fatigue/10);
	}
}