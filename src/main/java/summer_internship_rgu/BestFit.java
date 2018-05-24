package summer_internship_rgu;


import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collections;
import java.io.*;

public class BestFit {
	
	Integer items_length, current_best;
	Double cap;
	Integer i = null;
	Integer item_new;
	Integer array_new[];
	Integer array_sorted[];
	
    
	
	
	
	public Integer algoBestFit(Double items[])
	{
		Double rem[] = new Double[Array.getLength(items)];
		Integer bins = 0;
		for(i=0;i<Array.getLength(items);i++)
		{
			Integer j;
			Double min = cap + 1;
			Integer bi = 0;
					  
			for (j=0; j < bins; j++)
			{
				if (rem[j] >= items[i] && (rem[j] - items[i]) < min)
				{
					bi = j;
					min = rem[j] - items[i];
				}
			}
			if (min == cap+1)
			{
				rem[bins] = cap - items[i];
				bins++;
			}
			else
			{
				rem[bi] -= items[i];
			}
		}
		return bins;
	}
	
	
	}
