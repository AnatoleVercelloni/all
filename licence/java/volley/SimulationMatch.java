public class SimulationMatch{
	public static void main(String args[]) throws ExceptionEquipe{
		Complet c1 = new Complet("Sabacon plaiteux");
		Centraux c = new Centraux("Tohou Violon");
		Alier p2 = new Alier("Hercule Jauni");
		Joueur[] remplacantsBleu = {c1, c, p2};
		Equipe bleu = new Equipe("bleu", remplacantsBleu);
		bleu.ajoute(new Passeur("Johan Sires"));
		bleu.ajoute(new Complet("Marc Deluxe"));
		bleu.ajoute( new Complet("Teument Monstrueux"));
		bleu.ajoute(new Pointu("Garounet"));
		bleu.ajoute(new Centraux("Vincent Tropi"));
		bleu.ajoute(new Libero("Tule Enacier"));
		
		
		Pointu p1 = new Pointu("Heurant Serie");
		Passeur p = new Passeur("Huges");
		Complet c2 = new Complet("Ignasse drios");
		Joueur[] remplacantsRouge = {p1, p, c2};
		Equipe rouge = new Equipe("rouge",remplacantsRouge);
		rouge.ajoute(new Passeur("Henri Zotto"));
		rouge.ajoute(new Complet("George"));
		rouge.ajoute(new Alier("Gaspard Di"));
		rouge.ajoute(new Pointu("Rene Risser"));
		rouge.ajoute(new Centraux("Denis Rondelle"));
		rouge.ajoute(new Libero("Thor Ticolli"));
		
		
		Equipe vainqueur = Match.getInstance(bleu,rouge).comptagePoints();
		System.out.println("le grand vainqueur est l'equipe "+vainqueur.getNom());
		System.out.println("Tableau des scores: "+"bleu : "+(Match.getInstance(bleu,rouge).getScore())[0]+"  rouge : "+ (Match.getInstance(bleu,rouge).getScore())[1]);
		
			
	}
}