/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG32
 */
import javax.swing.*;
public class jvaswing {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String nama ="";
        int angka=0,sisa=0;
        
        nama = JOptionPane.showInputDialog ("Benda apakah yang disukai anak anak dan mudah meletus ? : ");
        angka=Integer.parseInt(JOptionPane.showInputDialog("Berapakah Jumalh sila pancasila ? : "));
        sisa = Integer.parseInt(JOptionPane.showInputDialog("angka berapakah sebelum angka 5 ? : "));
        
        JOptionPane.showMessageDialog(null,"Selamat anda dapat mengisi missing lyric berikut :\n"+nama+"ku ada "+angka+" rupa-rupa warnanya merah kuning kelabu merah muda dan biru meletus balon hijau dorr...hatiku sangat kacau balonku tinggal "+sisa+" kuopegang erat-erat");
    
    }
    
}
