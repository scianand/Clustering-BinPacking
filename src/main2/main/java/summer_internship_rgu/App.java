package summer_internship_rgu;

import static spark.Spark.*;

import com.google.gson.Gson;



class Request {
	public Double items[];
	public Double cap;
}
class Response {
	public Integer result;
}
public class App {
    public static void main(String[] args) {
    	Gson gson = new Gson(); 
        post("/binpacking/firstfit", (req, res) -> {
        	System.out.println("hello");
        	System.out.println(req.body());
        	Request request = gson.fromJson(req.body(), Request.class);
        	Response solution = new Response();
    		FirstFit ff= new FirstFit();
        	solution.result = ff.algoFirstFit(request.items, request.cap);
        	return solution;
        }, gson::toJson);
        post("/binpacking/bestfit", (req, res) -> {
        	System.out.println("hello");
        	System.out.println(req.body());
        	Request request = gson.fromJson(req.body(), Request.class);
        	Response solution = new Response();
    		BestFit bf= new BestFit();
        	solution.result = bf.algoBestFit(request.items, request.cap);
        	return solution;
        }, gson::toJson);
    }
}