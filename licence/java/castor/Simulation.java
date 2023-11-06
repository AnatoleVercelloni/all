public class Simulation{
	private Terrain t;
	private Castor[] populationCastor;
	private Arbre[] foret;
	private TasDeBranches[] barrage;
	private Riviere r;
	private Ours o;
	private static int natot = 0;
	private static int boisRamasse = 0;
	private static int mortVieux =0;
	
	
	
	public Simulation(int hauteur, int largeur,int nc,int cm, int na, int proba, int yr, int lr, int xb){
		t = new Terrain(largeur, hauteur);
		r = new Riviere(lr,yr);
		barrage = new TasDeBranches[lr];     // création du barrage
		for (int i = 0; i<barrage.length ; ++i){            //initialisation du barrage
			barrage[i] = new TasDeBranches(1);                //le barrage initial a une branche par case
			t.setCase(yr+i,xb,barrage[i]);
		}
		populationCastor = new Castor[cm];   //création de la population de castor
		for (int i = 0; i<nc ;++i){                  //initialisation de la population de départ de castor
		    int e = (int)(Math.random()*35)+1;
			populationCastor[i] = new Castor(yr, xb, e);
		System.out.println(populationCastor[i].toString());
		}
		foret = new Arbre[na];                              //création de la foret
		for (int i = 0; i<foret.length ; ++i){                     //initialisation de la foret
			if (Operation.probabilite(proba)){
				foret[i]=new Arbre();
				natot = natot+1;
				int colonnea = Operation.positionHorsRiviere(largeur, hauteur, r);;
				int lignea = (int)(Math.random()*(largeur));;
				if (t.caseEstVide(colonnea,lignea)){
					t.setCase(colonnea,lignea,foret[i]);
					
					System.out.println(foret[i].toString());
				}else{
					foret[i]=null;
				}
			}else{
				foret[i]=null;
			}
		}
		
		
		
		
		o = new Ours(largeur,hauteur);
		
		
	}
	
	public int getNatot(){
		return natot;
		
	}
	
	
	
	public int getBoisRamasse(){
		return boisRamasse;
		
	}
	
	public Castor[] getPopulationCastor(){
		return populationCastor;
		
	}
	
	public TasDeBranches[] getBarrage(){
		return barrage;
		
	}
	
	public Ours getOurs(){
		return o;
		
	}
	
	public int getMortVieux(){
		return mortVieux;
		
	}
	
	
	public void tSimulation( int largeur,int hauteur, int xb, int pc, int proba){
			int m = 10;
			int yTas=0;                                               
			r.setDebit();                                    			//le debit de la riviere change
			
			System.out.println(r.toString());
			o.oursAFaim(r);                                             //l'ours se place sur le terrain
			System.out.println(o.toString());
			o.mangerCastor(populationCastor);                            //l'ours grignotte du castor
			t.affiche();
			for (int j = 0; j<populationCastor.length ; ++j){       
                if (populationCastor[j]!=null){                                              //pour chaque castor:    
					populationCastor[j].lessEsp(1);                                             //l'esperence est decrementée
					
				}
				int l =0;
				
				for (int o = 0; o<populationCastor.length ; ++o){
					if (populationCastor[l]!=null){
							l=l+1;
					}
				}
				if (l == populationCastor.length){
					System.out.println("ERREUR, LA POPULATION A ATTEINT SON SEUIL MAXIMUM!!");
					return;
				}		
				
				if (Operation.probabilite(pc)){
					 if (populationCastor[j]!=null){      
			                       //les castors se clonnent
						                                         
						while ((l<populationCastor.length-1)&(populationCastor[l]!=null)){

							l=l+1;
						}
						    if (l!=populationCastor.length){
								Castor cc = populationCastor[j].cloneCastor(r);       
								populationCastor[l]=cc;
								populationCastor[l].setEsp((int)(Math.random()*12+4));
								System.out.println(cc.toStringEstNe());
							}
						
						
					 }
				}
					
				
				int d = largeur;
				//Arbre a=null;
				if (populationCastor[j]!=null){     
					
					if ((populationCastor[j].getYCastor()>=r.getPosition())&(populationCastor[j].getYCastor()<r.getPosition()+r.getLargeur())&&(populationCastor[j].getNbBranches()==0)){
						int h=0;		
						for (int k=0 ; k<foret.length ; ++k){
							
                            if (foret[k]!=null){
								//System.out.println(foret[k].getY()+" "+foret[k].getX());
								if (((int)(populationCastor[j].distance(foret[k].getY(),foret[k].getX()))<=d)&(foret[k].getAUnCastor()==false)){
									d=(int)populationCastor[j].distance(foret[k].getY(),foret[k].getX());   
									//a = foret[k];                              //les castor sur le barrage vont a l'arbre libre le plus proche
									h = k;
								}
							}
						}
						if (foret[h]!=null){
							if(((int)(populationCastor[j].distance(foret[h].getY(),foret[h].getX()))!=largeur)){//&(a.getY()>=0)&(a.getX()>=0)){
								populationCastor[j].seDeplace(foret[h].getY(), foret[h].getX());
								
								foret[h].setAUnCastor(true);   						//les castor sur un arbre ramasse des branches
								System.out.println(populationCastor[j].toStringSeDeplace(foret[h].getY(), foret[h].getX()));
								populationCastor[j].setNbBranches(foret[h].getQuantite());
								boisRamasse = boisRamasse+foret[h].getQuantite();
								System.out.println(populationCastor[j].toStringRamasse());
								foret[h].setQuantite(0);
								t.videCase(foret[h].getY(), foret[h].getX());
								foret[h]=null;
								
							}
						}
					}else{
						
						if ((populationCastor[j].getYCastor()<r.getPosition())|(populationCastor[j].getYCastor()>=r.getPosition()+r.getLargeur())&(populationCastor[j].getNbBranches()>0)){
							
							
							populationCastor[j].seDeplace( xb,yTas);
							
						}else{
					
							if ((populationCastor[j].getYCastor()>=r.getPosition())&(populationCastor[j].getYCastor()<r.getPosition()+r.getLargeur())&&(populationCastor[j].getNbBranches()>0)){
								if ((populationCastor[j]!=null)){
									for (int t=0; t<=populationCastor[j].getNbBranches(); ++t){
										barrage[t%4].setQuantite(barrage[t%4].getQuantite()+1);
											
										
									}
									System.out.println(populationCastor[j].toStringConsolide());
											
									populationCastor[j].setNbBranches(0);       //les castor renforce le barrage avec des branches
								}
							}
								
								
							
						}
					}
				}
				if (populationCastor[j]!=null){
					if (populationCastor[j].getEsp()==0){
							System.out.println(populationCastor[j].toStringEstMort());
							mortVieux = mortVieux+1;
							populationCastor[j]=null;                            //on retire de la population les castors qui sont morts
					}
					if (populationCastor[j]!=null){
						if (populationCastor[j].getEsp()<0){
							
							populationCastor[j]=null;  
						}
					}
						
				}
			}
			
			                     
			o.aBienMange();                                              //l'ours s'en va
			for (int k = 0; k<r.getLargeur(); ++k){
				if (barrage[k]!=null){
					if ((r.getDebit()>5)&(r.getDebit()<=6)){
						barrage[k].setQuantite(barrage[k].getQuantite()-(int)(0.1*barrage[k].getQuantite()));          //plus le debit est élevé, plus le barrage se détruit
					}
					if ((r.getDebit()>6)&(r.getDebit()<=9)){
						barrage[k].setQuantite(barrage[k].getQuantite()-(int)(0.25*barrage[k].getQuantite()));
					}
					if (r.getDebit()>9){
						barrage[k].setQuantite(barrage[k].getQuantite()-(barrage[k].getQuantite()));
					}
					if (barrage[k].getQuantite()<0){
						barrage[k].setQuantite(0);
					}
				}
			}
			for (int k = 0; k<foret.length ;++k){
				if (Operation.probabilite(proba)){
					                                   //Les arbres se clonent
					int xa = (int)(Math.random()*(largeur-r.getLargeur()));
					int colonnea = 0;
					if (xa<r.getPosition()){
						colonnea = xa;
					}else{
						colonnea = xa + r.getLargeur();
					}
					int lignea = (int)(Math.random()*(hauteur));
					if (t.caseEstVide(colonnea,lignea)){
						Arbre b = new Arbre();
					    int l =0;
						while ((l<foret.length-1)&(foret[l]!=null)){
							l=l+1;
						}
						if ((l!=foret.length)){
							
							foret[l]=b;
							t.setCase(colonnea,lignea,foret[l]);
							
							System.out.println(foret[l].toString());
							
							natot = natot+1;
							
						}else{
							t.videCase(colonnea,lignea);
						}
					}else{
						t.videCase(colonnea,lignea);
					}
					
					
					
					
					
					
				}
			
			}
	
			
	}
	
	public  static class  Operation{
		public static boolean probabilite(int p){
			int x =(int)(Math.random()*100);
			if (x<=p){
				return true;
			}else{
				return false;
			}
		}
		
		public static int positionHorsRiviere(int largeur, int hauteur, Riviere r){
			
			int x = (int)(Math.random()*(largeur-r.getLargeur()+1));
			while ((x>=r.getPosition())&(x<r.getLargeur()+r.getPosition())){    
				x = (int)(Math.random()*(largeur-r.getLargeur()));
			}
			
			return x;
	
		}
	}
	
	
	
	
}

			
			
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		