public class BioTool{

  public static void main(String[] args) {

    System.out.println("BioTool currently takes no arguments");

	if (args.length >= 1){
           System.out.println("However it was called with the following:");
		for (String s: args) {

		System.out.println(s);
		}
	}
    	
	/* Insert bioinformatics here!*/
  }

}

