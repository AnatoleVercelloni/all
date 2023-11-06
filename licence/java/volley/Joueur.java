public abstract class Joueur{
	protected String nom;
	protected int num = 0;
	protected int fatigue;
	
	public Joueur(String s){
		nom = s;
		num = num + 1;
		fatigue = 0;
	}
	
	public  String toString(){
		return nom;
	}
	
	public String getNom(){
		return nom;
	}
	
	public int getFatigue(){
		return fatigue;
	}
	
	public void setFatigue(){
		if (fatigue>3){
			fatigue = fatigue - 3;
		}else{
			fatigue = 0;
		}
	}
	
	
	
	public abstract int reception();
	public abstract int passe();
	
	public  static class  Operation{
		public static int probabilite(double p){
			double x = Math.random();
			if (x<=p){
				return 1;
			}else{
				return 0;
			}
		}
		
		
	}
	
}