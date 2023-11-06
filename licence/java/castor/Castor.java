public class Castor{
	private int xCastor;
	private int yCastor;
	private int esp;
	private int nbranches;
	private static int nbCastor=0;
	private int numCastor;
	
	
	
	public Castor (int x, int y){
		xCastor = x;
		yCastor = y;
		esp =34+(int)(Math.random()*4);
		nbranches = 0;
		nbCastor = nbCastor + 1;
		numCastor = nbCastor;
		
	}
	
	public Castor (int x, int y ,int e){
		xCastor = x;
		yCastor = y;
		esp = e;
		nbranches=0;
		nbCastor = nbCastor + 1;
		numCastor = nbCastor;
		
	}
	
	public int getXCastor(){
		return xCastor;
	}
	
	
	
	public int getYCastor(){
		return yCastor;
	}
	
	public int getNbCastor(){
		return nbCastor;
	}
	
	public int getNumCastor(){
		return numCastor;
	}
	
	
	public int getEsp(){
		return esp;
	}
	
	public int getNbBranches(){
		return nbranches;
	}
	
	public void setNbBranches(int n){
		nbranches = n;
	}
	
	public double distance (int x, int y){
		return Math.sqrt((xCastor-x)*(xCastor-x)+(yCastor-y)*(yCastor-y));
	}
	
	public void seDeplace (int xnew, int ynew){
		xCastor = xnew;
		yCastor = ynew;
	}
	
	public void lessEsp(int n){
	
		
			esp = esp-n;
		
	}
	
	public void setEsp(int n){
	
		esp = n;
	}
	
	public Castor cloneCastor(Riviere r){
		Castor c = new Castor(xCastor,r.getPosition());
		int espc =8+(int)(Math.random()*4);
		c.setEsp(espc);
		c.setNbBranches(nbranches);
		return c;
	}
	
	public String toString(){
		return "le castor numero "+numCastor+" est en ["+xCastor+","+yCastor+"] et a une esperence de "+esp;
	}
	
	public String toStringEstMort(){
		return "le castor numero "+numCastor+" est mort";
	}
	
	public String toStringSeDeplace(int x, int y){
		return "le castor numero "+numCastor+" se deplace en  ["+x+","+y+"]";
	}
	
	public String toStringRamasse(){
		return "le castor numero "+numCastor+" ramasse "+nbranches+" branches";
	}
	
	public String toStringConsolide(){
		return "le castor numero "+numCastor+" met "+nbranches+" branches sur le barrage";
	}
	
	public String toStringEstNe(){
		return "le castor numero "+numCastor+" est ne  en  ["+xCastor+","+yCastor+"]";
	}

}
