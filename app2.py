import threading
from tkinter import font
import tkinter as tk
from plyer import notification
import ttkbootstrap as ttk
import time
import tkinter
import os
from functools import partial
import csv
from tkinter.scrolledtext import ScrolledText
class MainWindow(ttk.Frame):
    def __init__(self,parent):
        self.parent = parent
        super().__init__(parent)
        hromadny_styl = "Custom.TLabel"
        ttk.Style().configure("Custom.TRadiobutton", font=("Arial", 14),foreground='black')
        ttk.Style().configure("TCheckbutton",foreground="blue",background="lightgrey",font=("Arial", 14))
        ttk.Style().configure(hromadny_styl, font=("Arial", 14))
        ttk.Style().configure("Custom.TButton",font=("Arial", 14, "bold"),foreground="black",background="red",padding=10,relief="flat")
        my_font = font.Font(family="Helvetica", size=14)
        parent.title("Notifikace")
        parent.geometry("900x550")
        seskup1 = ttk.Frame(parent,width=90, height=200, borderwidth=2)
        seskup2 = ttk.Frame(parent, relief=tk.GROOVE,width=245, height=290, borderwidth=2,padding=3)
        seskup21 = ttk.Frame(seskup2)
        self.seskup3 = ttk.Frame(parent, height=200)
        for radek2 in range(0,1):
            for sloupec2 in range(0,4):
                self.seskup3.grid_rowconfigure(radek2,weight=1)
                self.seskup3.grid_columnconfigure(sloupec2,weight=1)
        self.boolspustitprestavku = tkinter.BooleanVar(value=False)
        self.stop = threading.Event()
        self.label03 = ttk.Label(seskup2,text="zadej čas, po ktrém chceš dostat notifikaci:",
                                     wraplength=230,justify="center",style=hromadny_styl)
        self.cas_pripomenuti = ttk.Entry(seskup21, font=my_font, width=15)
        self.cas_pripomenuti.bind("<KeyPress>", partial(self.vypis_vsech_vepsanych_hodnot_do_entry, jmeno_promenne = self.cas_pripomenuti))
        self.opakovani_cas = ttk.Entry(seskup2, font=my_font)
        self.opakovani_cas.bind("<KeyPress>", partial(self.vypis_vsech_vepsanych_hodnot_do_entry, jmeno_promenne = self.opakovani_cas))
        self.label04 = ttk.Label(seskup2,font=my_font,text="Napiš kolikrát chceš toto připomenutí opakovat:",
                                     wraplength=230, justify="center",style=hromadny_styl)
        self.prestavky = ttk.Checkbutton(seskup2, text="zařadit přestávky", style="TCheckbutton",
                                         variable=self.boolspustitprestavku)
        self.boolspustitprestavku.trace_add("write", self.prestavka)
        self.cas_prestavky = ttk.Entry(seskup2, font=my_font)
        self.cas_prestavky.bind("<KeyPress>", partial(self.vypis_vsech_vepsanych_hodnot_do_entry, jmeno_promenne=self.cas_prestavky))
        self.pokracovat = ttk.Button(self.seskup3, text="pokračovat", command=self.pokracujdále, style="Custom.TButton")
        self.var_m_x_v = tkinter.StringVar(value="vteřiny")
        hodnota_radioButton = ttk.Label(seskup21, textvariable=self.var_m_x_v, style=hromadny_styl)
        vteriny = ttk.Radiobutton(seskup1,text= "vteřiny",value="vteřiny", variable=self.var_m_x_v, style ="Custom.TRadiobutton")
        minuty = ttk.Radiobutton(seskup1, text="minuty", value="minuty", variable=self.var_m_x_v, style ="Custom.TRadiobutton")
        cesta_slozka_obrazku = os.path.join(os.path.dirname(__file__), "app_images")
        cesta_obrazek_gifimage5 = os.path.join(cesta_slozka_obrazku, "gifimage5.gif")
        gifimage5 = tk.PhotoImage(file=cesta_obrazek_gifimage5)
        tlacitko = ttk.Label(seskup1,text="nastav čas", image=gifimage5,style=hromadny_styl)
        self.poprve = True
        tlacitko.bind("<Button-1>", lambda event:self.zobraz(self.cas_pripomenuti.get(), self.opakovani_cas.get(), str(1) if not self.boolspustitprestavku.get() else self.cas_prestavky.get()))
        tlacitko.gifimage5 = gifimage5
        cesta_obrazek_3dots = os.path.join(cesta_slozka_obrazku, "3dots.png")
        tlacitko_menu = tk.PhotoImage(file=cesta_obrazek_3dots)
        tritecky = ttk.Label(self.parent, image=tlacitko_menu)
        tritecky.bind("<Button-1>",self.vyber_moznosti)
        self.seskup3.grid_columnconfigure(3, weight=0)
        tritecky.grid(row=0, column=98,sticky="ne")
        tlacitko.dots = tlacitko_menu

        self.seznam_vsech_vstupu = [self.cas_pripomenuti, self.opakovani_cas, self.cas_prestavky,
                                    self.var_m_x_v,self.boolspustitprestavku]
        self.pri_spusteni()

        umis_row,umis_column,i = 0,0,1
        ohraniceni,odestup_ve_2 = 20,5
        self.row_index, self.col_index = umis_row + i + 5, umis_column
        self.cas_prestavky.grid(row=self.row_index, column=self.col_index, pady = odestup_ve_2)
        self.cas_prestavky.grid_remove()
        if self.boolspustitprestavku.get():
            self.prestavka()
        print(self.boolspustitprestavku.get(),"toto je bool")
        seskup2.grid(row=0,column=0, padx=ohraniceni, pady=ohraniceni)
        self.label03.grid(row=umis_row,column=umis_column,pady = odestup_ve_2)
        self.opakovani_cas.grid(row=umis_row + i + 3, column=umis_column, pady = odestup_ve_2)
        self.label04.grid(row=umis_row + i + 2, column=umis_column,pady = odestup_ve_2)
        self.prestavky.grid(row=umis_row + i + 4, column=umis_column,pady = odestup_ve_2)
        self.seskup3.grid(row=100,column=0,columnspan=100,sticky='ew')
        seskup21.grid(row=umis_row+i,column=umis_column,pady = odestup_ve_2)
        hodnota_radioButton.grid(row=0,column=1)
        self.cas_pripomenuti.grid(row=0, column=0)
        seskup1.grid(row=0,column=99,sticky='ne', padx=ohraniceni, pady=ohraniceni)
        nachazisenaradku,sloupec = 5,88
        tlacitko.grid(row=nachazisenaradku-1,column=sloupec)
        vteriny.grid(row=nachazisenaradku,column=sloupec)
        minuty.grid(row=nachazisenaradku+1,column=sloupec)
        self.text = ScrolledText(self.seskup3,wrap="word",font=("Arial",16,"bold"))
        self.text.insert(tk.END,"Zadej, co chceš udělat po přestávce.")
        self.text.grid(row=0,column=1,sticky='nsew',columnspan=2)
        self.text.grid_remove()
        self.pokracovat.grid(row=0,column=7,sticky='nsew')
        self.pokracovat.grid_remove()
        for radek in range(0,100):
            for sloupec in range(0,100):
                parent.grid_rowconfigure(radek,weight=1)
                parent.grid_columnconfigure(sloupec,weight=1)
        self.seskup3.grid_propagate(False)
        seskup2.grid_propagate(False)
        seskup1.grid_propagate(False)
    def vyber_moznosti(self,event):
        menu = ttk.Menu(self.parent, tearoff=0)
        menu.add_command(label="Uložit nastavení",command=self.uloz_hodnoty)
        menu.tk_popup(event.x_root, event.y_root)
    def prestavka(self,*args):
        if self.boolspustitprestavku.get():
            print("ano")
            self.cas_prestavky.grid()
        else:
            print("ne")
            self.cas_prestavky.grid_remove()
            self.cas_prestavky.delete(0, tk.END)
    def zobraz(self,cas_ukazatel,pocet_opakovani,prestavky):
        if not threading.current_thread().is_alive() or self.poprve == True:
            if all (v.isdigit() and int(v) != 0 for v in (cas_ukazatel,pocet_opakovani,prestavky)):
                self.opakovani = int(self.opakovani_cas.get())
                vteriny_minuty = self.var_m_x_v.get()
                cas_ukazatel = int(cas_ukazatel)
                cas_zobrazeni = cas_ukazatel
                if vteriny_minuty == "minuty":
                    cas_zobrazeni = cas_ukazatel * 60
                self.notifikace(cas_ukazatel, vteriny_minuty, cas_zobrazeni)
                self.poprve = False
            else:
                print("Zadej číselnou hodnotu, ve celých číslech.")
        else:
            print("skipuju")
    def notifikace(self, cas_ukazatel, vteriny_minuty,cas_zobrazeni):
        notification.notify(message=f"cas nastavny na: {cas_ukazatel}{vteriny_minuty}",app_name="Produktivní časovač", timeout=4)
        self.t = threading.Thread(target=lambda:self.odpocet(cas_ukazatel, vteriny_minuty,cas_zobrazeni), daemon=False)
        self.t.start()
        self.ukonci()
    def odpocet(self, cas_ukazatel, vteriny_minuty, cas_zobrazeni):
        si = 1
        for i in range(0, self.opakovani):
            self.booll = True
            if not self.stop.is_set():
                for j in range(0,cas_zobrazeni):
                    if not self.stop.is_set():
                        time.sleep(1)
                        print(f"spalo {si} sekundu")
                        si += 1
                if not self.stop.is_set():
                    notification.notify(title="Zpráva z aplikace upozorni", app_name="Produktivní časovač",
                                        message=f"právě uplynulo:{cas_ukazatel}{vteriny_minuty}", timeout=4)
                    if self.boolspustitprestavku.get():
                        self.parent.after(0, self.obnov_GUI())
                        if not i == self.opakovani - 1:
                            notification.notify(title="Následuje přestávka", app_name="Produktivní časovač",
                                                message="dej si přestávku", timeout=8)
                            for jj in range(0, int(self.cas_prestavky.get())):
                                if not self.stop.is_set():
                                    time.sleep(1)
                            self.pokracovat.grid()
                            while self.booll:
                                if not self.stop.is_set():
                                    time.sleep(1)
                            self.pokracovat.grid_remove()
        if threading.main_thread().is_alive():
            self.storno1.grid_remove()
        if self.stop.is_set():
            self.stop.clear()
    def vypis_vsech_vepsanych_hodnot_do_entry(self,hodnota_vstupu,jmeno_promenne):
        self.hodnota_vstupu = hodnota_vstupu
        print(f"toto je hodnota vstupu:{hodnota_vstupu}")
        print(f"Toto je hodnota posledniho vstupu:{self.hodnota_vstupu}")
        text = str(jmeno_promenne.get())
        pozice = jmeno_promenne.index(tk.INSERT)
        self.format_casu = str(self.var_m_x_v.get())
        if self.format_casu.strip() in text:
            jmeno_promenne.insert(pozice,self.hodnota_vstupu.char)
        elif self.hodnota_vstupu.keysym == "BackSpace":
            self.hodnota_vstupu = jmeno_promenne.delete(pozice)
        elif self.hodnota_vstupu.keysym.isalpha():
            self.parent.after(0, lambda: jmeno_promenne.delete(jmeno_promenne.index(tk.INSERT)-1))
    def ukonci(self):
        self.storno1 = ttk.Button(self.seskup3, text="Storno časovače", style="Custom.TButton", command=lambda :(self.stop.set(), self.pokracujdále(), print(f"vlákno stornováno:{self.stop.is_set()}", print(f"{print(self.stop.set())}"))))
        self.storno1.grid(column=0,row=0,sticky='nsew')
        self.seskup3.columnconfigure(0,weight=0)
    def obnov_GUI(self):
        self.parent.deiconify()
        self.text.grid()
    def pokracujdále(self):
        print("probehlo")
        self.booll = False
    def nove_okno(self):
        podrazene_okno = tk.Toplevel(self.parent)
    def uloz_hodnoty(self):
        self.ziskani_hodnot_vstupu()
        with open(self.cesta,"w",newline="",encoding="utf-8") as zapis:
            writer = csv.writer(zapis)
            for hodnoty_ze_self_seznam_hodnot in self.seznam_hodnot:
                writer.writerow([hodnoty_ze_self_seznam_hodnot])
                print("toto je zapis:",hodnoty_ze_self_seznam_hodnot)
    def pri_spusteni(self):
        print("spustilo se spusteni")
        nadrazeny_adresar = os.path.dirname(os.path.abspath(__file__))
        soubor_k_nastaveni = "settings while start app.csv"
        self.cesta = os.path.join(nadrazeny_adresar, soubor_k_nastaveni)
        if os.path.isfile(self.cesta):
            print("proslo to")
            seznam_hodnot = []
            with open(self.cesta,"r",newline="",encoding="utf-8") as zapis:
                reader = csv.reader(zapis)
                for row in reader:
                    seznam_hodnot.append(row)
            x = 0
            for prirazeni_hodnot in self.seznam_vsech_vstupu:
                if isinstance(prirazeni_hodnot,tkinter.Entry):
                    prirazeni_hodnot.delete(0, "end")
                    prirazeni_hodnot.insert(0,seznam_hodnot[x][0])
                    print(seznam_hodnot[x])
                elif isinstance(prirazeni_hodnot, (tkinter.StringVar,tkinter.BooleanVar)):
                    print("toto je prirazeni hodnot: ",prirazeni_hodnot," TOHLE JE STRINGVAR HODNOTA DO :", (seznam_hodnot[x]), "extrahovano ze ", seznam_hodnot)
                    prirazeni_hodnot.set(seznam_hodnot[x][0])
                    print("stringVar je nastaven na :",self.var_m_x_v.get())
                else:
                    print(type(prirazeni_hodnot))
                    print("neco je spatne")
                x+=1
        else:
            self.cas_pripomenuti.insert(0, int(10))
            self.opakovani_cas.insert(0, int(3))
            self.cas_prestavky.insert(0, "nahraď za trvání v (sec)")
            with open(self.cesta,"a",newline="",encoding="utf-8"):
                pass
    def ziskani_hodnot_vstupu(self):
        self.seznam_hodnot = []
        print(self.seznam_vsech_vstupu)
        for hodnota in self.seznam_vsech_vstupu:
            hodnota = hodnota.get()
            print(hodnota,"hodnota")
            self.seznam_hodnot.append(hodnota)
        print(self.seznam_hodnot)
        print("toto je self.self.var_m_x_v",self.var_m_x_v.get())
run = True
root = tkinter.Tk()
root.configure(background="#d9d9d5")
s = ttk.Style()
s.theme_use("flatly")
s.configure("Cervene.TButton",
    foreground='black',
    background='white',
    padding=0, relief="flat",font=("Helvetica",14))
app1 = MainWindow(root)
app1.mainloop()
