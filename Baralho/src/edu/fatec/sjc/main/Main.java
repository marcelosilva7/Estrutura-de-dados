package edu.fatec.sjc.main;

import edu.fatec.sjc.Baralho;
import edu.fatec.sjc.Carta;
import edu.fatec.sjc.SemCartaException;

public class Main {

	public static void main(String[] args) throws SemCartaException {
		Baralho b = new Baralho();
		b.embaralhar();
		while (b.hasCarta()) {
			Carta c = b.distribuirCarta();
			if (c != null)
				System.out.println(c.imprimir());
		}

	}

}
