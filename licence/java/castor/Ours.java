public class Ours{
	private int ligne;
	private int colonne;
	private int nb_lignes;
	private int nb_colonnes;
	private static int nbRepas = 0;
	
	
	
	public Ours(int nb_l, int nb_c){
		nb_lignes=nb_l;
		nb_colonnes = nb_c;
		ligne = -1;
		colonne = -1;
	}
	
	public void oursAFaim(Riviere r){
		ligne = (int)(Math.random()*(nb_lignes));
		colonne = (int)(Math.random()*(nb_colonnes));
	}
	
	public void mangerCastor(Castor[] p){
		int n = 15;
		for (int i = 0; i<p.length; ++i){
			if (p[i]!=null){
				if ((p[i].distance(ligne, colonne)<=1)&(n>0)){
					p[i].lessEsp(50);
					
					n=n-1;
					nbRepas = nbRepas+1;
				}
			}
		}
	}
	
	public int getNbRepas(){
		return nbRepas;
	}
	
	public void aBienMange(){
		ligne = -1;
		colonne = -1;
	}
	
	public String toString(){
		return "Un ours arrive en ["+ligne+","+colonne+"], il a faim";
	}
}

		
		

		
		
		