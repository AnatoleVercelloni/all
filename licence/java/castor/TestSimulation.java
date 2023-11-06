public class TestSimulation{
	public static void main(String[] args){
	
		int hauteur=10;   //hauteur du terrain
		int largeur=10;    //largeur du terrain
		int nc=25;          //nombre de castors de départ
		int cm=10000;          //nombre maximum de castor
		int na=10;          //nombre maximaum d'arbres
		int proba=40;        //probabilité qu'un arbre pousse
		int yr=5;            //position de la riviere
		int lr=4;             //largeur de la riviere
		int xb=5;            //position du barrage
		int nbEnVie=0;           //nombre de castor en vie à la fin
		int pc=11;            //probabilité qu"un castor se clone
		
		Simulation s = new Simulation(hauteur, largeur,nc,cm, na, proba, yr, lr, xb);
		
		for (int i = 0; i<200; ++i){
			s.tSimulation(largeur,hauteur,xb,pc, proba);
		}

		Castor c = new Castor(0,0);
		System.out.println("il y a eu "+s.getNatot()+" arbres");
		System.out.println("il y a eu "+(c.getNbCastor()-1)+" castors");
		for (int i = 0; i<cm ;++i){
			Castor[] pop = s.getPopulationCastor();
			if ((pop[i])!=null){
				nbEnVie = nbEnVie+1;
			}
		}
		System.out.println("il reste "+nbEnVie+" castors");
		System.out.println("l'ours a mange "+(s.getOurs()).getNbRepas()+" castors");
		System.out.println(s.getMortVieux()+" castors sont morts de vieillesse");
		System.out.println("les castors ont ramasses "+s.getBoisRamasse()+" branches");
		TasDeBranches[] b = s.getBarrage();
		System.out.println("le barrage: ");
		for (int i = 0; i<lr ; ++i){
			System.out.print("|"+b[i].getQuantite());
		}
		System.out.println("|");
		Castor[] pop = s.getPopulationCastor();
		
	}
}