public class Passeur extends Joueur implements Attaquant{
	
	
	public Passeur(String nom){
		super(nom);
		
	}
	
	
	public Passeur copie(){
		return new Passeur(nom);
	}
	
	public String toString(){
		return "Le passeur "+nom + " ";
	}
	
	public int reception(){
		System.out.println(toString()+"receptionne la balle");
		fatigue = fatigue + 1;
		if ((Math.random())<(0.7-fatigue/10)){
			return 1;
		}
		return 0;
	}
	
	public int passe(){
		System.out.println(toString()+"fait une passe");
		fatigue = fatigue + 1;
		if ((Math.random())<(1.0-fatigue/10)){
			return 1;
		}
		return 0;
	}
	
	public int contre(){
		fatigue = fatigue + 1;
		if ((Math.random())<(0.8-fatigue/10)){
			return 1;
		}
		return 0;
	}
	
	public int smash(){
		System.out.println(toString()+"smash");
		fatigue = fatigue + 1;
		if ((Math.random())<(0.4-fatigue/10)){
			return 1;
		}
		return 0;
	}
	
	public int servir(){
		fatigue = fatigue + 1;
		System.out.println(toString()+"sert");
		if ((Math.random())<(0.6-fatigue/10)){
			
			return 1;
		}
		
		return 0;
	}
	
}