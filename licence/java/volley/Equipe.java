public class Equipe{
	private String nom;
	private Joueur[] tab;
	private Joueur[] remplacants;
	
	public Equipe(String n, Joueur[] r){
		tab = new Joueur[6];
		nom = n;
		remplacants = r;
	}
	
	public Joueur getJoueur(int p){
		return tab[p];
	}
	
	public void setJoueur(int p){
		tab[p] = null;
	}
	
	public String getNom(){
		return nom;
	}
	
	public Joueur[] getRemplacants(){
		return remplacants;
	}
	
	public void ajoute(Joueur j) throws ExceptionEquipe{
		for (Joueur r: remplacants){
			if (j == r){
				throw new ExceptionEquipe ("le joueur "+j.getNom()+" est un remplacant de l'equipe "+nom);
			}
		}
		for (int i = 0; i<tab.length ; ++i){
			if (tab[i] == j){
				throw new ExceptionEquipe ("le joueur "+tab[i].getNom()+" est deja dans l'equipe "+nom);
			}
		}
		int i = 0;
		try{
			while (tab[i]!=null){
				i = i+1;
			}
		}catch (ArrayIndexOutOfBoundsException e){
			System.out.println("l'equipe est deja pleine") ;
		}
		tab[i]=j;
	}
	
	public void rotation()throws ExceptionEquipe{
		Joueur j = tab[0];
		for (int i = 1;i<tab.length; ++i){
			Joueur t = tab[i];
			tab[i] = j;
			j=t;
		}
		tab[0]=j;
		for (int i = 0; i<4; ++i){
			if ((i<4)&(tab[i] instanceof Attaquant == false)){
					remplace(tab[i]);
				
			}
		}
	}
	
	public void remplace(Joueur j)throws ExceptionEquipe{
		int i = 0;
		try{
			while (tab[i]!=j){
				i = i+1;
			}
		}catch (ArrayIndexOutOfBoundsException e){
			System.out.println("le joueur ne peut pas être remplacé, il n'est pas dans l'equipe") ;
		}
		int k = 10;
		int ir = 0;
		int p = 0;
		for ( p = 0 ; p<remplacants.length; ++p){
			
			if ((remplacants[p]).getFatigue()<k){
				if (((remplacants[p]  instanceof Attaquant == false)) &  (i<4)){
				}else{
					k = (remplacants[p]).getFatigue();
					ir = p;
				}
			}
		}
		if (((remplacants[ir]  instanceof Attaquant == false)) &  (i<4)){
			throw new ExceptionEquipe ("le libero de l'equipe "+nom+" ne peut pas etre a une position d'attaque");
		}
		System.out.println((remplacants[ir]).toString()+" remplace "+tab[i].toString());
		Joueur tmp = tab[i];
		tab[i] = remplacants[ir];
		remplacants[ir] = tmp;
		
		try{
			Thread.sleep(200);
		}catch(InterruptedException ex) {
			Thread.currentThread().interrupt();
					}
	}
}
			
			
			