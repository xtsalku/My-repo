/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG 31
 */
public class Mainclass {
    public static void main(String[]args){
    Siswa siswaNabil = new Siswa();
    siswaNabil.setNama("Nabil");
    siswaNabil.setumur(15);
    siswaNabil.setJeniskelamin("Laki-laki");
    siswaNabil.setNis("11082011");
    siswaNabil.setKelas("11a");
    siswaNabil.setwalikelas("Bambang,Spd.Mpd");
    String infosiswa = " \t INFO SISWA \n"+
            "Nama          : "+siswaNabil.getNama()+"\n"+
            "umur          : " + siswaNabil.getUmur()+"\n"+
            "jenis kelamin : "+siswaNabil.getJeniskelamin()+"\n"+
            "Nis           : "+siswaNabil.getNis()+"\n"+
            "Kelas         : "+siswaNabil.getkelas()+"\n"+
            "Walikelas     : " + siswaNabil.getWalikelas() +" \n";
        System.out.println(infosiswa);
        siswaNabil.status();
    
    
    
    }
    
}
