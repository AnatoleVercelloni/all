public class Alier extends Joueur implements Attaquant{
	
	public Alier(String nom){
		super(nom);
		
	}
	
	public Alier copie(){
		return new Alier(nom);
	}
	
	public String toString(){
		return "L'ailier "+nom;
	}
	
	public int reception(){
		fatigue = fatigue + 1;
		System.out.println(toString()+" receptionne la balle");
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int contre(){
		fatigue = fatigue + 1;
		return Operation.probabilite(0.4-fatigue/10);
	}
	
	public int smash(){
		System.out.println(toString()+" smash");
		fatigue = fatigue + 1;
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int passe(){
		System.out.println(toString()+" fait une passe");
		fatigue = fatigue + 1;
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int servir(){
		System.out.println(toString()+" sert");
		fatigue = fatigue + 1;
		return Operation.probabilite(0.8-fatigue/10);
	}
	
}