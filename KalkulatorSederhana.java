/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Akbar
 */
import javax.swing.*;
public class KalkulatorSederhana {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //deklarasi variabel
        int bil1,bil2,pil,hasil=0;
        String ulang ="1";
        //menampilkan menu pilihan
        while("1".equals(ulang)){
        String pilihan=JOptionPane.showInputDialog(null,"Menu Pilihan Operasi\n"
        +"1. Operasi Penjumlahan\n"
        +"2. Operasi Pengurangan\n"
        +"3. Operasi Perkalian\n"
        +"4. Operasi Pembagian\n"
        );
        pil=Integer.parseInt(pilihan);
        //input bil 1 dan 2
        String in1 = JOptionPane.showInputDialog("Masukkan angka ke-1 : ");
        bil1=Integer.parseInt(in1);
        String in2 = JOptionPane.showInputDialog("Masukkan Angka ke-2 : ");
        bil2=Integer.parseInt(in2);
        //proses menghitung di dalam switch
         switch (pil){
             case 1 : hasil=bil1+bil2;break;
             case 2 : hasil=bil1-bil2;break;
             case 3 : hasil=bil1*bil2;break;
             case 4 : hasil=bil1/bil2;break;
             default : JOptionPane.showMessageDialog(null,"Salah memasukan pilihan");
         }
        JOptionPane.showMessageDialog(null,"Maka Hasilnya  : "+hasil);
        
        ulang= JOptionPane.showInputDialog(null,"Apakah anda ingin menggunakan aplikasi lagi?\n "
        +"1.Iya\n"
        +"2.Tidak");
       
        }
        JOptionPane.showMessageDialog(null,"Terima Kasih atas kunjungannya....!!!!:):)");
        
        
        
    }
    
}
