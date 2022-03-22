/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG32
 */
import java.io.*;
public class bufredreader {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String nama = "";
        int angka=0,sisa=0;
        BufferedReader inpt = new BufferedReader(new InputStreamReader (System.in));
        try{
            System.out.print("Apa nama mainan kesukaan anak kecil ? : ");
            nama=inpt.readLine();
            System.out.print("Berapa jumlah sila pada pancasila ? : ");
            angka = Integer.parseInt(inpt.readLine());
            System.out.print("Angka berapakah sebelum angka 5? :");
            sisa = Integer.parseInt(inpt.readLine());   
        
        }catch(IOException e){
            System.out.println("Jawaban Anda Salah");
            
        }
        System.out.println(nama+"ku ada "+angka+" rupa-rupa warnanya merah kuning kelabu merah muda dan biru meletus balon hijau dorr...hatiku sangat kacau balonku tinggal "+sisa+" kuopegang erat-erat");
    }
    
}
