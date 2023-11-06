public class TasDeBranches extends Ressource{
	
	
	public TasDeBranches ( int n){
		
		super("XXXXX",n);
	}

	
	public void Accident (int na){
		int new_nb_branches = (int)(getQuantite() - (na/getQuantite()));
		if (new_nb_branches<0){
			setQuantite(0);
		}else{
			setQuantite(new_nb_branches);
		}
	}
}


