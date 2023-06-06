package edu.fatec.sjc;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import edu.fatec.sjc.enums.Naipe;
import edu.fatec.sjc.enums.Valor;

public class Baralho {
	private static final int NR_EMBARALHADAS = 100;
	
	private List<Carta> cartas;
	
	public Baralho() {
		setCartas(new ArrayList<Carta>());
		int i = 0;
		for(Naipe n : Naipe.getValues()) {
			for (Valor v : Valor.getValues()) {
				getCartas().add( new Carta(n, v));
			}
		}
		while(i < 56) {
			getCartas().add(new Carta(Naipe.CORINGA, Valor.CORINGA));
		}
	}
	
	public void embaralhar() {
		 List<Carta> c =  getCartas(); 
	    Collections.shuffle(cartas);
	}
	
	
	public Carta distribuirCarta() throws SemCartaException  {
		if(hasCarta())
			return getCartas().remove(cartas.size()-1);
		else {
			   throw new SemCartaException("Sem cartas no baralho");
		}
		}
	
	public boolean hasCarta() {
		return !cartas.isEmpty();
	}
	
	public String imprimirBaralho() {
		StringBuilder sb = new StringBuilder();
		for (Carta carta : cartas) {
	        sb.append(carta.imprimir()).append("\n");
	    }
		return sb.toString();
	}

	private List<Carta> getCartas() {
		return this.cartas;
	}
	
	private void setCartas(List<Carta> c) {
		this.cartas = c;
	}
}
