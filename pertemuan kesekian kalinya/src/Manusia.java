/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PROG 31
 */
public class Manusia {
    private String nama;
    private int umur;
    private String Jeniskelamin;
    
    public Manusia(){ }
    
    public Manusia(String nama,int umur,String jk){
        this.nama = nama;
        this.umur = umur;
        this.Jeniskelamin = jk;
    }
    
    
    public String getNama(){
        return nama;
    }
    
    public void setNama(String nama){
    this.nama = nama;
    }
    
    public int getUmur(){
         return umur;
    }
    
    public void setumur(int umur){
    this.umur = umur;
    }
    
    public String getJeniskelamin(){
    return Jeniskelamin;
    }
    
    public void setJeniskelamin(String nama){
    this.Jeniskelamin = Jeniskelamin;
    }
    
    public static void tertawa(String tawa){
        System.out.println(tawa);
    }
    
    public void status(){
    }
   
    
    
    
}
