/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG 31
 */
//public class pegawai {
    public class pegawai extends Manusia{
    String nip;
    String bidangBagian;
    String gaji;
    
    
    public void setGaji(String gaji){
    this.gaji = gaji;
    }
    public pegawai(){}
    
    public pegawai(String nip,String bidangBagian){
    this.nip = nip;
    this.bidangBagian = bidangBagian;
            
    }
    public void status (String status){
        System.out.println(status);
    }
    
    
  }
