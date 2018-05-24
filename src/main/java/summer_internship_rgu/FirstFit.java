package summer_internship_rgu;

import java.lang.reflect.Array;

public class FirstFit {
	
	double cap;
	
	public Integer algoFirstFit(Double items[], Double cap) {
		this.cap=cap;
		Double rem[] = new Double[Array.getLength(items)]; 
		Integer bins = 0;
		
		for(int i = 0; i < Array.getLength(items); i++) {
			Integer j;
			for(j = 0; j < bins; j++) {
				if(rem[j] >= items[i]) {
					rem[j] -= items[i];
					break;
				}
			}
			
			if(j == bins) {
				rem[bins] = cap - items[i];
				bins++;
			}
		}
		
		return bins;
	}

}
