package summer_internship_rgu;

import java.lang.reflect.Array;

public class NextFit {
	
	public Integer algoNextFit(Double items[], Double cap) {
		Double rem = cap;
		Integer bins = 1;
		for (int i = 0; i < Array.getLength(items); i++) {
			if (items[i] > rem) {
				bins++;
				rem = cap - items[i];
			}
			else {
				rem = rem - items[i];
			}
		}
		return bins;
	}
}
