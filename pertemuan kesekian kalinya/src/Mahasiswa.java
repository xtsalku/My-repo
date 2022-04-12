/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG 31
 */
//public class Mahasiswa {
    public class Mahasiswa extends Manusia{
    private String nim;
    private String jurusan;
            
        public Mahasiswa(){  }
        
        public Mahasiswa(String nim,String jurusan){
        this.nim = nim;
        this.jurusan = jurusan;

        }
        
        public String getNim(){
        return nim;
        }
        public void setNim(String nim){
        this.nim = nim;
        }
        public String getjurusan(){
            return jurusan;
        }
        public void status(String status){
            System.out.println(status);
        }
  }
//}

