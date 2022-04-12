/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG 31
 */
//public class Siswa {
     public class Siswa extends Manusia{
        private String nis;
        private String kelas;
        private String walikelas;
        
        public Siswa(){  }
        public Siswa(String nis,String kelas,String walikelas){
        this.nis = nis;
        this.kelas = kelas;
        this.walikelas = walikelas;
        }
        
        public String getNis(){
        return nis;
        }
        public void setNis(String nis){
        this.nis = nis;
        }
        public String getkelas(){
            return kelas;
        }
        public void setKelas(String kelas){
        this.kelas = kelas;
        }
        public String getWalikelas(){
            return walikelas;
        }
        public void setwalikelas(String walikelas){
        this.walikelas = walikelas;
        }
        public void status(){
            System.out.println("sedang belajar");
        }
        
    }
//}
    
    
    
    
    
    
    
    
    
   

