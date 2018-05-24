package summer_internship_rgu;

public class CheckClass {

	public Integer checkClass(Double a, Integer k) {
		Integer clas = 0;
		for(int i = k; i > 1; i--) {
			if (a > (1.0/i) && a <= 1.0/(i-1)) {
				clas = i-1;
				break;
			}
			else {
				clas = k;
			}
		}
		return (clas-1);
	}
}
