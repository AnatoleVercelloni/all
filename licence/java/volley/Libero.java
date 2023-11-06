public class Libero extends Joueur{
	
	public Libero(String nom){
		super(nom);
	}
	
	public String toString(){
		return "le libero "+nom;
	}
	
	public int passe(){
		System.out.println(toString()+" fait une passe");
		fatigue = fatigue + 1;
		return Operation.probabilite(0.7-fatigue/10);
		
	}
	
	public int reception(){
		System.out.println(toString()+" receptionne la balle");
		fatigue = fatigue + 1;
		return Operation.probabilite(1.0-fatigue/10);
	}
}