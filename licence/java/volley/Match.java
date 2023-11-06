import java.io.*;

public class Match{
	private static Match INSTANCE = null;
	private Equipe bleu;
	private Equipe rouge;
	private int[] score;
	
	private Match(Equipe b, Equipe r){
		bleu = b;
		rouge = r;
		score = new int[4];
	}
	
	private synchronized static void creatInstance(Equipe b, Equipe r){
		if (INSTANCE == null){
			INSTANCE = new Match(b,r);
		}
	}
	
	public static Match getInstance(Equipe b, Equipe r){
		if (INSTANCE == null){
			creatInstance(b,r);
		}
		return INSTANCE;
	}
	
	public Equipe quiCommence(){
		if (Math.random()<0.5){
			return bleu;
		}else{
			return rouge;
		}
	}
	
	public int[] getScore(){
		return score;
	}
	
	public String affichePoint(Equipe e){
		return "l'equipe "+e.getNom()+" marque 1 point";
	}
	
	public int alea(int n){
		int i = (int)(Math.random()*6);
		while (i == n){
			i = (int)(Math.random()*6);
		}
		return i;
	}
		
	
	public Equipe point(Equipe e0)throws ExceptionEquipe{
		Equipe e1;
		Equipe e2;
		int n;
		int p;
		if (e0 == bleu){
			e1 = bleu;
			e2 = rouge;
		}else{
			e1 = rouge;
			e2 = bleu;
		}
		
		int i =0;
		Joueur r = (e1.getRemplacants())[0];
		while ((e1.getJoueur(i).getFatigue()<6)&(i<5)){
			i = i + 1;
		}
		if (e1.getJoueur(i).getFatigue()>=6){
			
			e1.remplace(e1.getJoueur(i));
		}
		
		r = (e2.getRemplacants())[0];
		while ((e2.getJoueur(i).getFatigue()<6)&(i<5)){
			i = i + 1;
		}
		if (e2.getJoueur(i).getFatigue()>=6){
			
			e2.remplace(e2.getJoueur(i));
		}
		
		if (((Attaquant)(e1.getJoueur(0))).servir() == 0){
			System.out.println("il fait une faute ");
			return e2;
		}
		
		i = 0;
		for (Joueur j : e1.getRemplacants()){
			j.setFatigue();
		}
		for (Joueur j : e2.getRemplacants()){
			j.setFatigue();
		}
		try{
			Thread.sleep(200);
			}catch(InterruptedException ex) {
				Thread.currentThread().interrupt();
					}
					
		while (i<10){
			try{
				Thread.sleep(200);
			}catch(InterruptedException ex) {
				Thread.currentThread().interrupt();
			}
			
			n = 10;
			p = 0;
			if (i!=0){
				n = (int)Math.random()*3 + 1;
				if (((Attaquant)(e2.getJoueur(n))).contre()==1){
					System.out.println((e2.getJoueur(n)).toString()+" contre");

					return e2;
				}
			}
			
			p = alea(n);
			if ((e2.getJoueur(p)).reception() == 0){
				System.out.println("il fait une faute ");
				
				return e1;
			}
		
			n = alea(p);
			if ((e2.getJoueur(n)).passe() == 0){
				System.out.println("il fait une faute ");
				
				return e1;
			}
			p = alea(n);
			while ((e2.getJoueur(p) instanceof Attaquant )== false){
				p = alea(n);
			}
			if (((Attaquant)(e2.getJoueur(p))).smash() == 0){
				System.out.println("il fait une faute ");
				
				return e1;
			}
			
			
			p = 0;
			n = (int)Math.random()*3 + 2;
			if (((Attaquant)(e1.getJoueur(n))).contre() == 1){
				System.out.println((e1.getJoueur(n)).toString()+" contre");
				
			
				return e1;
			}
			p = alea(n);
			if ((e1.getJoueur(p)).reception() == 0){
				System.out.println("il fait une faute ");
				
				return e2;
			}
			n = alea(p);
			if ((e1.getJoueur(n)).passe() == 0){
				System.out.println("il fait une faute ");
				
				return e2;
			}
			p = alea(n);
			while ((e1.getJoueur(p) instanceof Attaquant )== false){
				p = alea(n);
			}
			if (((Attaquant)(e1.getJoueur(p))).smash() == 0){
				System.out.println("il fait une faute ");
				
				return e2;
			}
			i = i + 1;
			
		}
		
		System.out.println("erreur");
		return bleu;
		
	}
	
	public Equipe comptagePoints()throws ExceptionEquipe{
		
		Equipe eq = (point(quiCommence()));
		Equipe tmp;
		if (eq == bleu){
				score [2] = score [2] + 1;
				System.out.println(affichePoint(eq));
			}else{
				score [3] = score [3] + 1;
				System.out.println(affichePoint(eq));
			}
		while ((score[0] <2)&(score[1]<2)){
			while ((score[2] <25)&(score[3]<25)|(Math.abs(score[2]-score[3])<2)){
				
				try{
					Thread.sleep(200);
				}catch(InterruptedException ex) {
					Thread.currentThread().interrupt();
					}
				tmp = eq;
				eq = point(tmp);
				
				if (eq == bleu){
					score [2] = score [2] + 1;
					
				}else{
					score [3] = score [3] + 1;
					
				}
				System.out.println(affichePoint(eq));
				System.out.println("bleu : "+score[2]+" rouge : "+score[3]);
				if (eq!=tmp){
					eq.rotation();
					System.out.println("l'equipe "+eq.getNom()+" fait une rotation ");
					try{
						Thread.sleep(200);
					}catch(InterruptedException ex) {
						Thread.currentThread().interrupt();
					}
				}
				
			}
			
			if (score[2]>score[3]){
				score[0] = score[0] + 1;
				System.out.println("l'equipe bleu remporte un set "+score[2]+" a "+score[3]);
				eq = rouge;
			}else{
				score[1] = score[1] + 1;
				System.out.println("l'equipe rouge remporte un set "+score[3]+" a "+score[2]);
				eq = bleu;
			}
			try{
					Thread.sleep(5000);
					}catch(InterruptedException ex) {
				Thread.currentThread().interrupt();
					}
			score[2] = 0;
			score[3] = 0 ;
			
		}
		if (score[0]>=2){
				return bleu;
			}else{
				return rouge;
			}
	}
		
			
}
		