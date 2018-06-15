package summer_internship_rgu;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;


class hello{
	Integer final_bins[][];
	BufferedReader reader;
	Integer examples = null;
	String line;
	Integer hb, nb, bb, fb;
	Integer nb1, bb1, fb1;
	Double items_length;
	Double item_new;
	Double cap;
	String details[];
	Double details_int[] = new Double[3];
		
	
	public Integer algoNextFit(Double items[], Double cap) {
		NextFit nf= new NextFit();
		Integer bins = nf.algoNextFit(items, cap);
		return bins;
	}
	
	public Integer algoHarm(Double items_norm[], Double cap, Integer k) {
		
		HarmonicAlgo ha= new HarmonicAlgo();
		Integer total_bins = ha.algoHarm(items_norm, cap, k);
		return total_bins;
	}

	public Integer algoFirstFit(Double items[], Double cap) {
		FirstFit ff= new FirstFit();
		Integer bins = ff.algoFirstFit(items, cap);
		return bins;
	}

	public Integer algoBestFit(Double items[], Double cap) {
		BestFit bf= new BestFit();
		bf.cap=cap;
 		Integer bins = bf.algoBestFit(items);
		return bins;
	}

	public Double normalize(Double a, Double cap) {
		
		Double result;
		result = a/cap;
		return result;
	}
	
	public void calculate() throws Exception
	{
		reader = new BufferedReader(new FileReader("C:\\Ashish\\Clustering-Bin-Packing\\src\\main\\resources\\binpack1.txt"));
		
		try {
			
			line = reader.readLine();
			examples = Integer.parseInt(line);
			final_bins = new Integer[4][examples];
		}
		catch(Exception e) {
			System.out.println("\nException\n");
		}
		for (int i = 0; i < examples; i++) {
			line = reader.readLine();
			line = reader.readLine();
			details = line.trim().split("\\s+");
			for(int k = 0; k < details.length; k++) {
				details_int[k] = Double.parseDouble(details[k]);
			}
			
			cap = details_int[0];
			items_length = details_int[1];
			Double array_new[] = new Double[items_length.intValue()];
			Double items_norm[] = new Double[items_length.intValue()];
			try {
				for (int j = 0; j < items_length; j++) {
					line = reader.readLine();
					item_new = Double.parseDouble(line);
					array_new[j] = item_new;
					items_norm[j] = normalize(array_new[j], cap);
				}
			}
			catch(Exception e) {
				System.out.println("\nException\n");
			}

			hb = algoHarm(items_norm, 1.0, 40);
			nb = algoNextFit(items_norm, 1.0);
			bb = algoBestFit(items_norm, 1.0);
			fb = algoFirstFit(items_norm, 1.0);
			
			System.out.print("With normalization \n");
			
			final_bins[0][i] = hb;
			System.out.print(hb + "\t");
			final_bins[1][i] = nb;
			System.out.print(nb + "\t");
			final_bins[2][i] = bb;
			System.out.print(bb + "\t");
			final_bins[3][i] = fb;
			System.out.print(fb + "\n");
			
			System.out.print("Without normalization \n");
			
			nb1 = algoNextFit(array_new, cap);
			bb1 = algoBestFit(array_new, cap);
			fb1 = algoFirstFit(array_new, cap);
			//final_bins[0][i] = hb;
			//System.out.print(hb + "\t");
			//final_bins[1][i] = nb;
			System.out.print(nb1 + "\t");
			//final_bins[2][i] = bb;
			System.out.print(bb1 + "\t");
			//final_bins[3][i] = fb;
			System.out.print(fb1 + "\n");
		}
		reader.close();
		
		for (int i = 0; i < 4; i++) {
			Arrays.sort(final_bins[i]);
			for (int j = 0; j < examples; j++) {
				//System.out.print(final_bins[i][j] + "\t");
			}
			//System.out.println();
		}
		
		
	}
	
	public void output(){
		try {
		PrintWriter writer = new PrintWriter(new File("C:\\Ashish\\Clustering-Bin-Packing\\src\\main\\output\\binpack1_output.txt"));
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < examples; j++) {
				writer.print(final_bins[i][j] + "\t");
			}
			writer.println("");
		}
		writer.close();
	}
	catch(Exception e) {
		System.out.println("\nException\n");
	}
	
	}
	
	
}
public class BinPacking {
	
	
	public static void main(String args[]) throws Exception {
		
		 hello b=new hello();
		 b.calculate();
		 b.output();
		
		}
	
}