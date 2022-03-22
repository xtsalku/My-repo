/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG32
 */
public class operatorkondisi {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String Status = "";
        int grade = 80;
        
        Status = (grade >= 60) ? "passed" : "fail";
        System.out.println(Status);
    }
    
}
