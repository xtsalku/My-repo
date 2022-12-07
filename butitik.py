#|================================== dibuat oleh =====================================|#
#|                >> 1. Atsal Maulana Akbar Saputra (2110651129)                      |#
#|                >> 2. Oscar Wildan Akmal          (2110651123)                      |#
#|                >> 3. M. Agil Fatoni              (2110651138)                      |#
#|                >> 4. Eygin Suswanto Omar         (2110651101)                      |#
#|=============================== Selamat Berbelanja =================================|#
#|====================================================================================|#


#=========== memasukkan library yang dipakai =========================
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
#=================== akhir dari import library ===========================================


         #==================== cocde dikaliai disini ======================

# ==========================  tombol total bayar ==========================
def tot_bay():

        # ============ list harga minuman ===============
        es_jeruk_harga = 5000
        kopi_harga = 3000
        es_teh_harga = 3000
        jus_buah_harga = 8000
        soda_gembira_harga = 10000
        es_coklat_harga = 7000
        milo_harga = 5000
        sprite_harga = 12000
        # ============== list harga makanan ==================
        roti_harga = 1000
        nasi_goreng_harga = 13000
        bakso_harga = 15000
        soto_harga = 15000
        rawon_harga = 15000
        nasi_campur_harga = 13000
        nasi_pecel_harga = 9000
        nasi_lalapan_harga = 13000


        # ============ proses jumlah beli input ===================
        es_jeruk_q = es_jeruk_qty.get()
        kopi_q = kopi_qty.get()
        es_teh_q = es_teh_qty.get()
        jus_buah_q = jus_buah_qty.get()
        soda_gembira_q = soda_gembira_qty.get()
        es_coklat_q = es_coklat_qty.get()
        milo_q = milo_qty.get()
        sprite_q = sprite_qty.get()

        # ============= proses jumlah beli ======================
        roti_q = roti_qty.get()
        nasi_goreng_q = nasi_goreng_qty.get()
        bakso_q = bakso_qty.get()
        soto_q = soto_qty.get()
        rawon_q = rawon_qty.get()
        nasi_campur_q = nasi_campur_qty.get()
        nasi_pecel_q = nasi_pecel_qty.get()
        nasi_lalapan_q = nasi_lalapan_qty.get()


        # ================ cek jika jumlah pesanan tidak di isi ====================
        if es_jeruk_var.get() == 0:
                es_jeruk_q = 0
        elif es_jeruk_var.get() == 1 and es_jeruk_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan es_jeruk anda")
                es_jeruk_q = 0

        if kopi_var.get() == 0:
                kopi_q = 0
        elif kopi_var.get() == 1 and kopi_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan kopi anda")
                kopi_q = 0

        if es_teh_var.get() == 0:
                es_teh_q = 0
        elif es_teh_var.get() == 1 and es_teh_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan es_teh anda")
                es_teh_q = 0

        if jus_buah_var.get() == 0:
                jus_buah_q = 0
        elif jus_buah_var.get() == 1 and jus_buah_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan jus_buah anda")
                jus_buah_q = 0

        if soda_gembira_var.get() == 0:
                soda_gembira_q = 0
        elif soda_gembira_var.get() == 1 and soda_gembira_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan soda_gembira anda")
                soda_gembira_q = 0

        if es_coklat_var.get() == 0:
                es_coklat_q = 0
        elif es_coklat_var.get() == 1 and es_coklat_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan es_coklat anda")
                es_coklat_q = 0

        if milo_var.get() == 0:
                milo_q = 0
        elif milo_var.get() == 1 and milo_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan milo anda")
                milo_q = 0

        if sprite_var.get() == 0:
                sprite_q = 0
        elif sprite_var.get() == 1 and sprite_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan sprite anda")
                sprite_q = 0

        
        # ================ cek jika jumlah pesanan tidak di isi ====================
        if roti_var.get() == 0:
                roti_q = 0
        elif roti_var.get() == 1 and roti_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Roti anda")
                roti_q = 0

        if nasi_goreng_var.get() == 0:
                nasi_goreng_q = 0
        elif nasi_goreng_var.get() == 1 and nasi_goreng_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Nasi Goreng anda")
                kopi_q = 0

        if bakso_var.get() == 0:
                bakso_q = 0
        elif bakso_var.get() == 1 and bakso_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Bakso anda")
                bakso_q = 0

        if soto_var.get() == 0:
                soto_q = 0
        elif soto_var.get() == 1 and soto_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan soto anda")
                soto_q = 0

        if rawon_var.get() == 0:
                rawon_q = 0
        elif rawon_var.get() == 1 and rawon_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Rawon anda")
                rawon_q = 0

        if nasi_campur_var.get() == 0:
               nasi_campur_q = 0
        elif nasi_campur_var.get() == 1 and nasi_campur_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Nasi Campur anda")
                nasi_campur_q = 0

        if nasi_pecel_var.get() == 0:
                nasi_pecel_q = 0
        elif nasi_pecel_var.get() == 1 and nasi_pecel_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Nasi Pecel anda")
                nasi_pecel_q = 0

        if nasi_lalapan_var.get() == 0:
                nasi_lalapan_q = 0
        elif nasi_lalapan_var.get() == 1 and nasi_lalapan_qty.get() == "":
                messagebox.showerror("error","silahkan isi jumlah pesanan Nasi Lalapan anda")
                nasi_lalapan_q = 0
        
        
        # ============ Proses Total Hitung Minuman ===================
        total_es_jeruk_harga = es_jeruk_harga * int(es_jeruk_q)
        total_kopi_harga = kopi_harga * int(kopi_q)
        total_es_teh_harga = es_teh_harga * int(es_teh_q)
        total_jus_buah_harga = jus_buah_harga * int(jus_buah_q)
        total_soda_gembira_harga = soda_gembira_harga * int(soda_gembira_q)
        total_es_coklat_harga = es_coklat_harga * int(es_coklat_q)
        total_milo_harga = milo_harga * int(milo_q)
        total_sprite_harga = sprite_harga * int(sprite_q)

        # ============ Proses Total Harga Minuman ===================
        total_bay_minuman = total_es_jeruk_harga + total_kopi_harga + total_es_teh_harga + total_jus_buah_harga + total_soda_gembira_harga + total_es_coklat_harga + total_milo_harga + total_sprite_harga

        if harga_bay_minuman.get() != "":
                harga_bay_minuman.delete(0,"end")
                harga_bay_minuman.insert("end",total_bay_minuman)
        else:
                harga_bay_minuman.insert("end",total_bay_minuman)

        
        # ============ Proses Hitung Total Makanan ===================
        total_roti_harga = roti_harga * int(roti_q)
        total_nasi_goreng_harga = nasi_goreng_harga * int(nasi_goreng_q)
        total_bakso_harga = bakso_harga * int(bakso_q)
        total_soto_harga = soto_harga * int(soto_q)
        total_rawon_harga = rawon_harga * int(rawon_q)
        total_nasi_campur_harga = nasi_campur_harga * int(nasi_campur_q)
        total_nasi_pecel_harga = nasi_pecel_harga * int(nasi_pecel_q)
        total_nasi_lalapan_harga = nasi_lalapan_harga * int(nasi_lalapan_q)

         # ============ Proses Total Harga Makanan ===================
        total_bay_makanan = total_roti_harga + total_nasi_goreng_harga + total_bakso_harga + total_soto_harga + total_rawon_harga + total_nasi_campur_harga + total_nasi_pecel_harga + total_nasi_lalapan_harga

        if harga_bay_makanan.get() != "":
                harga_bay_makanan.delete(0,"end")
                harga_bay_makanan.insert("end",total_bay_makanan)
        else:
                harga_bay_makanan.insert("end",total_bay_makanan)

        
        if pajak.get() != "":
                pajak.delete(0,"end")
                pajak.insert(0,"2")
        else:
                pajak.insert(0,"2")
        
        hby =  int(harga_bay_makanan.get())
        hbx = int(harga_bay_minuman.get())

        tot_bay = hby+hbx
        tot_bay = tot_bay * 8 / 100


        if jumlah_bayar != "":
                jumlah_bayar.delete(0,"end")
                jumlah_bayar.insert(0,tot_bay)
        else:
                jumlah_bayar.insert(0,tot_bay)

        
        PPN = hby+hbx+int(pajak.get())

        if sub_total.get() != "":
                sub_total.delete(0,"end")
                sub_total.insert(0,PPN)
        else:
                sub_total.insert(0,PPN)


        if total_bay.get() != "":
                total_bay.delete(0,"end")
                total_bay.insert(0,float(PPN + tot_bay))
        else:
                total_bay.insert(0,float(PPN + tot_bay))

        

         # =====================  Struck Pesanan ===========================
        waktu = datetime.now().time()
        if bill_details.get(1.0,"end") != "":
                bill_details.delete(1.0,"end")
                bill_details.insert(1.0,f" Billno-{random.randint(100,1000)}\t{waktu}\n Items(q) \t \tqty \n{'es_jeruk ('+str(es_jeruk_q) + ')' + '         ' + str(int(es_jeruk_q) * es_jeruk_harga) + '   '  if es_jeruk_var.get() == 1 else''}{'kopi ('+str(kopi_q) + ')' + '        ' + str(int(kopi_q) * kopi_harga) + '  '  if kopi_var.get() == 1 else ''}{ 'es_teh ('+str(es_teh_q) + ')' + '           ' + str(int(es_teh_q) * es_teh_harga) + '  '  if es_teh_var.get() == 1 else''}{'jus_buah ('+str(jus_buah_q) + ')' + '         ' + str(int(jus_buah_q) * jus_buah_harga) + '   '  if jus_buah_var.get() == 1 else''}{'Jhosua('+str(soda_gembira_q) + ')' + '         ' + str(int(soda_gembira_q) * soda_gembira_harga) + '   '  if soda_gembira_var.get() == 1 else''}{'es_coklat('+str(es_coklat_q) + ')' + '           ' + str(int(es_coklat_q) * es_coklat_harga) + '   '  if es_coklat_var.get() == 1 else''}{'milo('+str(milo_q) + ')' + '     ' + str(int(milo_q) * milo_harga) + '     '  if milo_var.get() == 1 else''}{'sprite('+str(sprite_q) + ')' + '     ' + str(int(sprite_q) * sprite_harga) + '     '  if sprite_var.get() == 1 else''}{'roti('+str(roti_q) + ')' + '          ' + str(int(roti_q) * roti_harga) + '     '  if roti_var.get() == 1 else''}{'nasi goreng('+str(nasi_goreng_q) + ')' + '     ' + str(int(nasi_goreng_q) * nasi_goreng_harga) + '  '  if nasi_goreng_var.get() == 1 else''}{'bakso('+str(bakso_q) + ')' + '  ' + str(int(bakso_q) * bakso_harga) + '  '  if bakso_var.get() == 1 else''}{'soto('+str(soto_q) + ')' + '        ' + str(int(soto_q) * soto_harga) + '   '  if soto_var.get() == 1 else''}{'rawon('+str(rawon_q) + ')' + '        ' + str(int(rawon_q) * rawon_harga) + '   '  if rawon_var.get() == 1 else''}{'nasi_campur('+str(nasi_campur_q) + ')' + '        ' + str(int(nasi_campur_q) * nasi_campur_harga) + '   '  if nasi_campur_var.get() == 1 else''}{'nasi pecel('+str(nasi_pecel_q) + ')' + '    ' + str(int(nasi_pecel_q) * nasi_pecel_harga) + '  '  if nasi_pecel_var.get() == 1 else''}{'nasi_lalapan('+str(nasi_lalapan_q) + ')' + '          ' + str(int(nasi_lalapan_q) * nasi_lalapan_harga) + '    '  if nasi_lalapan_var.get() == 1 else''}\nPPN    {pajak.get()}\n         {jumlah_bayar.get()} \n total          {total_bay.get()}\n ")
        
                # ================== End  =============================
        

# ========= tombol save ================

def save():
        layar.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        if layar.filename is Nsatu:
                return
        file_save =  str(bill_details.get(1.0,END))
        layar.filename.write(file_save)
        layar.filename.close()
        
# =========== End =====================


# ============= Tombol Checklist Minuman =================
def es_jeruk_chk():
        if es_jeruk_var.get() == 1:
                es_jeruk_qty['state'] = "normal"
                es_jeruk_qty['bg'] = '#248aa2'
                es_jeruk_qty['fg'] = "white"
                
        else:
                es_jeruk_qty['state'] = "disabled"


def kopi_chk():
        if kopi_var.get() == 1:
                kopi_qty['state'] = "normal"
                kopi_qty['bg'] = '#248aa2'
                kopi_qty['fg'] = "white"
        else:
                kopi_qty['state'] = "disabled"

def es_teh_chk():
        if es_teh_var.get() == 1:
                es_teh_qty['state'] = "normal"
                es_teh_qty['bg'] = '#248aa2'
                es_teh_qty['fg'] = "white"
        else:
                es_teh_qty['state'] = "disabled"

def jus_buah_chk():
        if jus_buah_var.get() == 1:
                jus_buah_qty['state'] = "normal"
                jus_buah_qty['bg'] = '#248aa2'
                jus_buah_qty['fg'] = "white"
        else:
                jus_buah_qty['state'] = "disabled"

def soda_gembira_chk():
        if soda_gembira_var.get() == 1:
                soda_gembira_qty['state'] = "normal"
                soda_gembira_qty['bg'] = '#248aa2'
                soda_gembira_qty['fg'] = "white"
        else:
                soda_gembira_qty['state'] = "disabled"

def es_coklat_chk():
        if es_coklat_var.get() == 1:
                es_coklat_qty['state'] = "normal"
                es_coklat_qty['bg'] = '#248aa2'
                es_coklat_qty['fg'] = "white"
        else:
                es_coklat_qty['state'] = "disabled"

def milo_chk():
        if milo_var.get() == 1:
                milo_qty['state'] = "normal"
                milo_qty['bg'] = '#248aa2'
                milo_qty['fg'] = "white"
        else:
                milo_qty['state'] = "disabled"

def sprite_chk():
        if sprite_var.get() == 1:
                sprite_qty['state'] = "normal"
                sprite_qty['bg'] = '#248aa2'
                sprite_qty['fg'] = "white"
        else:
                sprite_qty['state'] = "disabled"
# ================== end==================



# === Tombol Checklist Makanan ================

def roti_chk():
        if roti_var.get() == 1:
                roti_qty['state'] = "normal"
                roti_qty['bg'] = '#248aa2'
                roti_qty['fg'] = "white"
                
        else:
                roti_qty['state'] = "disabled"

def nasi_goreng_chk():
        if nasi_goreng_var.get() == 1:
                nasi_goreng_qty['state'] = "normal"
                nasi_goreng_qty['bg'] = '#248aa2'
                nasi_goreng_qty['fg'] = "white"
        else:
               nasi_goreng_qty['state'] = "disabled"

def bakso_chk():
        if bakso_var.get() == 1:
                bakso_qty['state'] = "normal"
                bakso_qty['bg'] = '#248aa2'
                bakso_qty['fg'] = "white"
        else:
                bakso_qty['state'] = "disabled"

def soto_chk():
        if soto_var.get() == 1:
                soto_qty['state'] = "normal"
                soto_qty['bg'] = '#248aa2'
                soto_qty['fg'] = "white"
        else:
                soto_qty['state'] = "disabled"

def rawon_chk():
        if rawon_var.get() == 1:
                rawon_qty['state'] = "normal"
                rawon_qty['bg'] = '#248aa2'
                rawon_qty['fg'] = "white"
        else:
                rawon_qty['state'] = "disabled"

def nasi_campur_chk():
        if nasi_campur_var.get() == 1:
                nasi_campur_qty['state'] = "normal"
                nasi_campur_qty['bg'] = '#248aa2'
                nasi_campur_qty['fg'] = "white"
        else:
                nasi_campur_qty['state'] = "disabled"

def nasi_pecel_chk():
        if nasi_pecel_var.get() == 1:
                nasi_pecel_qty['state'] = "normal"
                nasi_pecel_qty['bg'] = '#248aa2'
                nasi_pecel_qty['fg'] = "white"
        else:
                nasi_pecel_qty['state'] = "disabled"

def nasi_lalapan_chk():
        if nasi_lalapan_var.get() == 1:
                nasi_lalapan_qty['state'] = "normal"
                nasi_lalapan_qty['bg'] = '#248aa2'
                nasi_lalapan_qty['fg'] = "white"
        else:
                nasi_lalapan_qty['state'] = "disabled"
#============== end ==========================


# ===== Kalkulator Sederhana disini ================

def sembilan():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","9")
        else:
                result.insert("end","9")
                
            

def delapan():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","8")
        else:
                result.insert("end","8")

def tujuh():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","7")
        else:
                result.insert("end","7")

def enam():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","6")
        else:
                result.insert("end","6")

def lima():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","5")
        else:
                result.insert("end","5")

def empat():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","4")
        else:
                result.insert("end","4")

def tiga():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","3")
        else:
                result.insert("end","3")

def dua():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","2")
        else:
                result.insert("end","2")

def satu():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","1")
        else:
                result.insert("end","1")

def nol():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","0")
        else:
                result.insert("end","0")

def tambah():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","+")
        else:
                result.insert("end","+")

def kurang():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","-")
        else:
                result.insert("end","-")

def kali():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","*")
        else:
                result.insert("end","*")

def bagi():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","/")
        else:
                result.insert("end","/")

def sama_dengan():


        if result.get() == "":
                result.insert("end","error")
        elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0] == "*" or result.get()[0] == "/":
                result.delete(0,"end")
                result.insert("end","error")
        elif 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")


        else:
                res = result.get()
                res = eval(res)
                result.insert("end"," = ")
                result.insert("end",res)

def clear():
        result.delete(0,"end")

#========== end ========================

# ====== tombol kirim ====================
def kirim():
        layar = tk.Tk()
        layar.geometry('300x400')
        layar['bg']="white"

        frame4 = Frame(layar,width=300,height=60,relief=RIDGE,borderwidth=5,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
        frame4.place(x=0,y=0)
                
        l2 = Label(frame4,text="kirim Bill",font=('roboto',22,'bold'),bg='#248aa2',fg="#ffffff")
        l2.place(x=85,y=1)

        frame5 = Frame(layar,width=300,height=340,relief=RIDGE,borderwidth=5,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
        frame5.place(x=0,y=55)

        innerframe5 = Frame(frame5,width=285,height=325,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
        innerframe5.place(x=0,y=0)

        l3 = LabelFrame(innerframe5,text="kirim Bill Melalui SMS",width=270,height=310,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
        l3.place(x=2,y=2)

        l4 = Label(innerframe5,text="Nomor",font=('verdana',10,'bold'))
        l4.place(x=40,y=40)

        number = Entry(innerframe5,width=30,borderwidth=2)
        number.place(x=40,y=70)
        
        l5 = Label(innerframe5,text="Detail Pembayaran",font=('verdana',10,'bold'))
        l5.place(x=40,y=100)

        b_detail = ScrolledText(innerframe5,width=23,height=7,relief=RIDGE,borderwidth=3)
        b_detail.place(x=40,y=130) 

        b_detail.insert(1.0,bill_details.get(1.0,END))



        def kirim_bill():
                ph_number = number.get()
                messages = b_detail.get("1.0","end-1c")

                if ph_number == "":
                        messagebox.showerror("Error",'silahkan isi nomor hp')
                elif messages == "":
                        messagebox.showerror("Error",'Detail Pembayaran kosong')
                else:
                        url = "https://www.fast2sms.com/dev/bulk"
                        api="" #go to fast2sms.com signup to get the free api and put it into here in api variable
                        querystring = {"authorization":api,"sender_id":"FSTSMS","message":messages,"language":"english","route":"p","numbers":ph_number}

                        headers = {
                                'cache-control': "no-cache"
                                }
                        requests.request("GET", url, headers=headers, params=querystring)
                        
                
                        messagebox.showinfo("kirim SMS",'Detail Pembayaran Telah Terkirim')

                
        kirim_msg = Button(innerframe5,text="kirim Bill",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",padx=20,command=kirim_bill)
        kirim_msg.place(x=100,y=255)

        layar.mainloop()

# ============ end =====================


# ==== Tombol exit =================
def exit():
        message = messagebox.askquestion('Notepad',"Ingin Keluar aplikasi ? ")
        if message == "yes":
                layar.destroy()
        else:
                "return"
# ======== end =======================


# ==== Tombol hapus(C) ============
def hapus():
        # ========== Minuman ===========
        es_jeruk_qty.delete(0,'end')
        es_jeruk.deselect()
        es_jeruk_qty['state'] = "disabled"
        kopi_qty.delete(0,'end')
        kopi.deselect()
        kopi_qty['state'] = "disabled"
        es_teh_qty.delete(0,'end')
        es_teh.deselect()
        es_teh_qty['state'] = "disabled"
        jus_buah_qty.delete(0,'end')
        jus_buah.deselect()
        jus_buah_qty['state'] = "disabled"
        soda_gembira_qty.delete(0,'end')
        soda_gembira.deselect()
        soda_gembira_qty['state'] = "disabled"
        es_coklat_qty.delete(0,'end')
        es_coklat.deselect()
        es_coklat_qty['state'] = "disabled"
        milo_qty.delete(0,'end')
        milo.deselect()
        milo_qty['state'] = "disabled"
        sprite_qty.delete(0,'end')
        sprite.deselect()
        sprite_qty['state'] = "disabled"
        # ========== Makanan ===========
        roti_qty.delete(0,'end')
        roti.deselect()
        roti_qty['state'] = "disabled"
        nasi_goreng_qty.delete(0,'end')
        nasi_goreng.deselect()
        nasi_goreng_qty['state'] = "disabled"
        bakso_qty.delete(0,'end')
        bakso.deselect()
        bakso_qty['state'] = "disabled"
        soto_qty.delete(0,'end')
        soto.deselect()
        soto_qty['state'] = "disabled"
        rawon_qty.delete(0,'end')
        rawon.deselect()
        rawon_qty['state'] = "disabled"
        nasi_campur_qty.delete(0,'end')
        nasi_campur.deselect()
        nasi_campur_qty['state'] = "disabled"
        nasi_pecel_qty.delete(0,'end')
        nasi_pecel.deselect()
        nasi_pecel_qty['state'] = "disabled"
        nasi_lalapan_qty.delete(0,'end')
        nasi_lalapan.deselect()
        nasi_lalapan_qty['state'] = "disabled"
        # ========== Total Bayar ===========
        harga_bay_minuman.delete(0,'end')
        harga_bay_makanan.delete(0,'end')
        pajak.delete(0,'end')
        jumlah_bayar.delete(0,'end')
        sub_total.delete(0,'end')
        total_bay.delete(0,'end')
        # ========== Struct ============
        bill_details.delete(1.0,'end')

#======== End =============





# ===== Ukuran jendela GUI =================
layar = tk.Tk()
#layar.attributes('-fullscreen',True)
layar.geometry('800x500')
layar.maxsize(800,390)
layar.minsize(800,390)
layar.title("Kasir Warung Bu titik")

frame = Frame(layar,width=800,height=70,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame.place(x=0,y=0)

l1 = Label(frame,text="Warung Bu Titik",font=('roboto',30,'bold'),bg='#248aa2',fg="#ffffff")
l1.place(x=10,y=4)


# ======================================================================

frame1= Frame(layar,width=450,height=230,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame1.place(x=0,y=70)

innerframe1 = Frame(frame1,width=300,height=220,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe1.place(x=0,y=0)

Minuman  = LabelFrame(innerframe1,text="Aneka Minuman",width=155,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
Minuman.place(x=2,y=2)



es_jeruk_var = IntVar()
es_jeruk = Checkbutton(Minuman,text="esjeruk",variable=es_jeruk_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=es_jeruk_chk)
es_jeruk.place(x=2,y=2)

es_jeruk_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
es_jeruk_qty.place(x=74,y=2)
es_jeruk_qty.insert(0,"0")

kopi_var = IntVar()
kopi = Checkbutton(Minuman,text="kopi",variable=kopi_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=kopi_chk)
kopi.place(x=2,y=22)

kopi_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
kopi_qty.place(x=74,y=22)

es_teh_var = IntVar()
es_teh = Checkbutton(Minuman,text="esteh",variable=es_teh_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=es_teh_chk)
es_teh.place(x=2,y=44)
es_teh_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
es_teh_qty.place(x=74,y=44)

jus_buah_var = IntVar()
jus_buah = Checkbutton(Minuman,text="jus",variable=jus_buah_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=jus_buah_chk)
jus_buah.place(x=2,y=66)
jus_buah_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
jus_buah_qty.place(x=74,y=66)

soda_gembira_var = IntVar()
soda_gembira = Checkbutton(Minuman,text="Jhosua",variable=soda_gembira_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=soda_gembira_chk)
soda_gembira.place(x=2,y=88)
soda_gembira_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
soda_gembira_qty.place(x=74,y=88)

es_coklat_var = IntVar()
es_coklat = Checkbutton(Minuman,text="nyoklat",variable=es_coklat_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=es_coklat_chk)
es_coklat.place(x=2,y=110)
es_coklat_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
es_coklat_qty.place(x=74,y=110)

milo_var = IntVar()
milo = Checkbutton(Minuman,text="milo",variable=milo_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=milo_chk)
milo.place(x=2,y=132)
milo_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
milo_qty.place(x=74,y=132)

sprite_var = IntVar()
sprite = Checkbutton(Minuman,text="sprite",variable=sprite_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=sprite_chk)
sprite.place(x=2,y=154)
sprite_qty = Entry(Minuman,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
sprite_qty.place(x=74,y=154)


innerframe2 = Frame(frame1,width=290,height=220,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe2.place(x=151,y=0)


foods  = LabelFrame(innerframe2,text="Menu Makanan",width=275,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
foods.place(x=2,y=2)

roti_var = IntVar()
roti = Checkbutton(foods,text="Roti",variable=roti_var,font=('verdana',8,'bold'),command=roti_chk)
roti.place(x=2,y=2)
roti_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
roti_qty.place(x=140,y=2)

nasi_goreng_var = IntVar()
nasi_goreng = Checkbutton(foods,text="Nasgor Special",variable=nasi_goreng_var,font=('verdana',8,'bold'),command=nasi_goreng_chk)
nasi_goreng.place(x=2,y=22)
nasi_goreng_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
nasi_goreng_qty.place(x=140,y=22)

bakso_var = IntVar()
bakso = Checkbutton(foods,text="Bakso Mercon",variable=bakso_var,font=('verdana',8,'bold'),command=bakso_chk)
bakso.place(x=2,y=44)
bakso_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
bakso_qty.place(x=140,y=44)

soto_var = IntVar()
soto = Checkbutton(foods,text="soto babat",variable=soto_var,font=('verdana',8,'bold'),command=soto_chk)
soto.place(x=2,y=66)
soto_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
soto_qty.place(x=140,y=66)

rawon_var = IntVar()
rawon = Checkbutton(foods,text="Nasi Rawon",variable=rawon_var,font=('verdana',8,'bold'),command=rawon_chk)
rawon.place(x=2,y=88)
rawon_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
rawon_qty.place(x=140,y=88)

nasi_campur_var = IntVar()
nasi_campur = Checkbutton(foods,text="Nasi Campur",variable=nasi_campur_var,font=('verdana',8,'bold'),command=nasi_campur_chk)
nasi_campur.place(x=2,y=110)
nasi_campur_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
nasi_campur_qty.place(x=140,y=110)

nasi_pecel_var = IntVar()
nasi_pecel = Checkbutton(foods,text="nasi pecel",variable=nasi_pecel_var,font=('verdana',8,'bold'),command=nasi_pecel_chk)
nasi_pecel.place(x=2,y=132)
nasi_pecel_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
nasi_pecel_qty.place(x=140,y=132)

nasi_lalapan_var = IntVar()
nasi_lalapan = Checkbutton(foods,text="Lalapan Ayam",variable=nasi_lalapan_var,font=('verdana',8,'bold'),command=nasi_lalapan_chk)
nasi_lalapan.place(x=2,y=154)
nasi_lalapan_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
nasi_lalapan_qty.place(x=140,y=154)





# =================================================================

frame2= Frame(layar,width=450,height=90,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame2.place(x=0,y=300)

innerframe3 = Frame(frame2,width=440,height=80,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe3.place(x=0,y=0)


total_harga_minuman = Label(innerframe3,text="Harga Minuman",font=('verdana',8,'bold'))
total_harga_minuman.place(x=2,y=2)
harga_bay_minuman = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
harga_bay_minuman.place(x=130,y=0)

total_harga_makanan = Label(innerframe3,text="Harga Makanan",font=('verdana',8,'bold'))
total_harga_makanan.place(x=2,y=24)
harga_bay_makanan = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
harga_bay_makanan.place(x=130,y=22)

pajak = Label(innerframe3,text="PPN",font=('verdana',8,'bold'))
pajak.place(x=2,y=46)
pajak = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
pajak.place(x=130,y=44)


bay_pajak = Label(innerframe3,text="PPN",font=('verdana',8,'bold'))
bay_pajak.place(x=250,y=2)
jumlah_bayar = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
jumlah_bayar.place(x=330,y=0)

sub_total = Label(innerframe3,text="Sub Total",font=('verdana',8,'bold'))
sub_total.place(x=250,y=24)
sub_total = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
sub_total.place(x=330,y=22)

ttl_bayar = Label(innerframe3,text="Total Bayar",font=('verdana',8,'bold'))
ttl_bayar.place(x=250,y=46)
total_bay = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
total_bay.place(x=330,y=44)


#============================================================================
frame3= Frame(layar,width=350,height=320,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame3.place(x=450,y=70)

innerframe4 = Frame(frame3,width=340,height=310,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe4.place(x=0,y=0)


result = Entry(innerframe4,width=28,relief=SUNKEN,borderwidth=3)
result.place(x=2,y=0)

# =============== code kalkulator jika ingin di tambahkan ===============
# sembilan = Button(innerframe4,text="9",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=sembilan)
# sembilan.place(x=0,y=24)
# delapan = Button(innerframe4,text="8",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=delapan)
# delapan.place(x=48,y=24)
# tujuh = Button(innerframe4,text="7",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=tujuh)
# tujuh.place(x=96,y=24)
# tambah = Button(innerframe4,text="+",padx=6,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=tambah)
# tambah.place(x=144,y=24)


# enam = Button(innerframe4,text="6",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=enam)
# enam.place(x=0,y=50)
# lima = Button(innerframe4,text="5",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=lima)
# lima.place(x=48,y=50)
# empat = Button(innerframe4,text="4",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=empat)
# empat.place(x=96,y=50)
# kurang = Button(innerframe4,text="-",padx=8,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=kurang)
# kurang.place(x=144,y=50)

# tiga = Button(innerframe4,text="3",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=tiga)
# tiga.place(x=0,y=76)
# dua = Button(innerframe4,text="2",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=dua)
# dua.place(x=48,y=76)
# satu = Button(innerframe4,text="1",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=satu)
# satu.place(x=96,y=76)
# kalitiply = Button(innerframe4,text="*",padx=7,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=kali)
# kalitiply.place(x=144,y=76)

# nol = Button(innerframe4,text="0",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=nol)
# nol.place(x=0,y=102)
# clear = Button(innerframe4,text="C",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=clear)
# clear.place(x=48,y=102)
# sama_dengan = Button(innerframe4,text="=",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=sama_dengan)
# sama_dengan.place(x=96,y=102)
# bagi = Button(innerframe4,text="/",padx=7,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=bagi)
# bagi.place(x=144,y=102)
# ========================= End kalkulator ====================

bill_details = ScrolledText(innerframe4,width=44,height=18,relief=SUNKEN,borderwidth=3,font=('courier',9,''))
bill_details.place(x=0,y=-1)


total = Button(innerframe4,text="Total",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=tot_bay)
total.place(x=0,y=275)

save = Button(innerframe4,text="Save",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=save)
save.place(x=43,y=275)

kirim = Button(innerframe4,text="kirim",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=kirim)
kirim.place(x=82,y=275)

clr = Button(innerframe4,text="Clear",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=exit)
clr.place(x=124,y=275)

exit = Button(innerframe4,text="exit",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=hapus)
exit.place(x=280,y=275)

layar.mainloop()


# ==============xxxxxxxxxxxxxxxxxxxx==== End code Here =======xxxxxxxxxxxxxxxx========== 
