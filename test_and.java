/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG32
 */
public class test_and {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       int i = 5;
    int j = 6;
    int k = 7;
    boolean test = false;

      System.out.println ("coba &&");
      test = (i > 10) && (j++ > 9);
      System.out.println (i);
      System.out.println (j);
      System.out.println (test);
      System.out.println();
      
      System.out.println ("coba &");
      test = (i > 10) & (j++ > 9);
      System.out.println (i);
      System.out.println (j);
      System.out.println (test);
      System.out.println();
      
    }
    
}
