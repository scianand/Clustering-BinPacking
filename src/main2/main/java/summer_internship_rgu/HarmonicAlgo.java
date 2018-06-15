package summer_internship_rgu;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class HarmonicAlgo {
	NextFit b;
	CheckClass cl;
	
	public Integer algoHarm(Double items_norm[], Double cap, Integer k) {
		
		b=new NextFit();
		Integer total_bins = 0, clas = 0;
		Integer bins_in_classes[] = new Integer[k];
		cl =new CheckClass();
		ArrayList<ArrayList<Double>> listOLists = new ArrayList<ArrayList<Double>>();
		ArrayList<Double> ele_of_class_i = new ArrayList<Double>();
		
		for(int i = 0; i < k; i++) {
			ArrayList<Double> singleList = new ArrayList<Double>();
			listOLists.add(singleList);
		}
		
		for(int i = 0; i < Array.getLength(items_norm); i++) {
			clas = cl.checkClass(items_norm[i], k);
			listOLists.get(clas).add(items_norm[i]);
		}
		
		for(int i = 0; i < k; i++) {
			ele_of_class_i = listOLists.get(i);
			Double ele_of_class_i_double[] = ele_of_class_i.toArray(new Double [ele_of_class_i.size()]);
			if (ele_of_class_i.size() != 0) {
				bins_in_classes[i] = b.algoNextFit(ele_of_class_i_double, 1.0);
			}
			else {
				bins_in_classes[i] = 0;
			}
			total_bins += bins_in_classes[i]; 
		}

		return total_bins;
	}
}
