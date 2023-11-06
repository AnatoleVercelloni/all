public class Pointu extends Alier implements Attaquant{
	
	public Pointu(String nom){
		super(nom);
	}
	
	public Pointu copie(){
		return new Pointu(nom);
	}
	
	public String toString(){
		return "Le Pointu "+nom;
	}
	
	public int reception(){
		System.out.println(toString()+" receptionne la balle");
		return Operation.probabilite(0.6-fatigue/10);
	}
	
	public int contre(){
		
		return Operation.probabilite(0.8-fatigue/10);
	}
	
	public int smash(){
		System.out.println(toString()+" smash");
		fatigue = fatigue + 1;
		return Operation.probabilite(1.0-fatigue/10);
	}
	
	
}
	