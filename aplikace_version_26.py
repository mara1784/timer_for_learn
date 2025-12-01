import threading
from tkinter import font
import tkinter as tk
from plyer import notification
import ttkbootstrap as ttk
import time
import tkinter
from functools import partial
from tkinter.scrolledtext import ScrolledText
class MainWindow(ttk.Frame):
    def __init__(self,parent):
        self.parent = parent
        super().__init__(parent)
        hromadny_styl = "Custom.TLabel"
        ttk.Style().configure("Custom.TRadiobutton", font=("Arial", 14),foreground='black')
        ttk.Style().configure("Hromadny.TCheckbutton",foreground="blue",background="lightgrey",font=("Arial", 14))
        ttk.Style().configure(hromadny_styl, font=("Arial", 14))
        my_font = font.Font(family="Helvetica", size=14)
        parent.title("Notifikace")
        parent.geometry("900x550")
        seskup1 = ttk.Frame(parent,width=90, height=200, borderwidth=2)
        seskup2 = ttk.Frame(parent, relief=tk.GROOVE,width=245, height=290, borderwidth=2,padding=3)
        seskup21 = ttk.Frame(seskup2)
        self.boolspustitprestavku = tkinter.BooleanVar(value=False)
        self.stringvar = tkinter.StringVar(value="vteřiny")
        self.stop = threading.Event()
        self.label03 = ttk.Label(seskup2,text="zadej čas, po ktrém chceš dostat notifikaci:",
                                     wraplength=230,justify="center",style=hromadny_styl)
        self.entry03 = ttk.Entry(seskup21,font=my_font,width=15)
        self.entry03.bind("<KeyPress>",partial(self.vypis_vsech_vepsanych_hodnot_do_entry,jmeno_promenne = self.entry03))
        self.entry03.insert(0, int(10))
        self.entry04 = ttk.Entry(seskup2,font=my_font)
        self.entry04.bind("<KeyPress>",partial(self.vypis_vsech_vepsanych_hodnot_do_entry,jmeno_promenne = self.entry04))
        self.entry04.insert(0, int(3))
        self.label04 = ttk.Label(seskup2,font=my_font,text="Napiš kolikrát chceš toto připomenutí opakovat:",
                                     wraplength=230, justify="center",style=hromadny_styl)
        self.prestavky = ttk.Checkbutton(seskup2, text="zařadit přestávky", style="Hromadny.TCheckbutton",
                                         command= self.prestavka, variable=self.boolspustitprestavku)
        self.entry05 = ttk.Entry(seskup2, font=my_font)
        self.entry05.bind("<KeyPress>", partial(self.vypis_vsech_vepsanych_hodnot_do_entry, jmeno_promenne=self.entry05))
        self.pokracovat = ttk.Button(parent, text="pokračovat", command=self.pokracujdále, style="Custom.TButton")
        hodnota_radioButton = ttk.Label(seskup21,textvariable=self.stringvar,style=hromadny_styl)
        vteriny = ttk.Radiobutton(seskup1,text="vteřiny",value="vteřiny",variable=self.stringvar, style = "Custom.TRadiobutton")
        minuty = ttk.Radiobutton(seskup1,text="minuty",value="minuty",variable=self.stringvar, style = "Custom.TRadiobutton")
        gifimage2 = tk.PhotoImage(file="gifimage5.gif")
        tlacitko = ttk.Label(seskup1,text="nastav čas", image=gifimage2,style=hromadny_styl)
        tlacitko.bind("<Button-1>",lambda event:self.zobraz(self.entry03.get(),self.entry04.get(), str(1) if not self.boolspustitprestavku.get() else self.entry05.get()))
        tlacitko.gifimage2 = gifimage2
        ohraniceni,odestup_ve_2 = 20,5
        seskup2.grid(row=0,column=0, padx=ohraniceni, pady=ohraniceni)
        umis_row,umis_column,i = 0,0,1
        self.label03.grid(row=umis_row,column=umis_column,pady = odestup_ve_2)
        self.entry04.grid(row=umis_row + i + 3, column=umis_column,pady = odestup_ve_2)
        self.label04.grid(row=umis_row + i + 2, column=umis_column,pady = odestup_ve_2)
        self.prestavky.grid(row=umis_row + i + 4, column=umis_column,pady = odestup_ve_2)
        self.row_index, self.col_index = umis_row + i + 5, umis_column
        self.entry05.grid(row=self.row_index, column=self.col_index,pady = odestup_ve_2)
        self.entry05.grid_remove()
        seskup21.grid(row=umis_row+i,column=umis_column,pady = odestup_ve_2)
        hodnota_radioButton.grid(row=0,column=1)
        self.entry03.grid(row=0,column=0)
        seskup1.grid(row=0,column=99,sticky='ne', padx=ohraniceni, pady=ohraniceni)
        nachazisenaradku,sloupec = 5,88
        tlacitko.grid(row=nachazisenaradku-1,column=sloupec)
        vteriny.grid(row=nachazisenaradku,column=sloupec)
        minuty.grid(row=nachazisenaradku+1,column=sloupec)
        self.text = ScrolledText(self.parent,width=30,height=4,wrap="word",font=("Arial",16,"bold"))
        self.text.insert(tk.END,"Zadej, co chceš udělat po přestávce.")
        self.text.grid(column=10,row=100)
        self.text.grid_remove()
        self.pokracovat.grid(row=100,column=99)
        self.pokracovat.grid_remove()
        for radek in range(0,100):
            for sloupec in range(0,100):
                parent.grid_rowconfigure(radek,weight=1)
                parent.grid_columnconfigure(sloupec,weight=1)
        seskup2.grid_propagate(False)
        seskup1.grid_propagate(False)
    def prestavka(self):
        if self.boolspustitprestavku.get():
            print("ano")
            self.entry05.grid()
            self.entry05.insert(0,"nahraď za trvání v (sec)")
        else:
            print("ne")
            self.entry05.grid_remove()
            self.entry05.delete(0,tk.END)
    def zobraz(self,cas_ukazatel,pocet_opakovani,prestavky):
        if all (v.isdigit() and int(v) != 0 for v in (cas_ukazatel,pocet_opakovani,prestavky)):
            self.opakovani = int(self.entry04.get())
            vteriny_minuty = self.stringvar.get()
            cas_ukazatel = int(cas_ukazatel)
            cas_zobrazeni = cas_ukazatel
            if vteriny_minuty == "minuty":
                cas_zobrazeni = cas_ukazatel * 60
            self.notifikace(cas_ukazatel, vteriny_minuty, cas_zobrazeni)
        else:
            print("Zadej číselnou hodnotu, ve celých číslech.")
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
                            for jj in range(0, int(self.entry05.get())):
                                if not self.stop.is_set():
                                    time.sleep(1)
                            self.pokracovat.grid()
                            while self.booll:
                                if not self.stop.is_set():
                                    time.sleep(1)
                            self.pokracovat.grid_remove()
        if threading.main_thread().is_alive():
            self.storno1.grid_forget()
        if self.stop.is_set():
            self.stop.clear()
    def vypis_vsech_vepsanych_hodnot_do_entry(self,hodnota_vstupu,jmeno_promenne):
        self.hodnota_vstupu = hodnota_vstupu
        print(f"toto je hodnota vstupu:{hodnota_vstupu}")
        print(f"Toto je hodnota posledniho vstupu:{self.hodnota_vstupu}")
        text = str(jmeno_promenne.get())
        pozice = jmeno_promenne.index(tk.INSERT)
        self.format_casu = str(self.stringvar.get())
        if self.format_casu.strip() in text:
            jmeno_promenne.insert(pozice,self.hodnota_vstupu.char)
        elif self.hodnota_vstupu.keysym == "BackSpace":
            self.hodnota_vstupu = jmeno_promenne.delete(pozice)
        elif self.hodnota_vstupu.keysym.isalpha():
            self.parent.after(0, lambda: jmeno_promenne.delete(jmeno_promenne.index(tk.INSERT)-1))
    def ukonci(self):
        (ttk.Style()).configure(
            "Custom.TButton",
            font=("Arial", 14, "bold"),
            foreground="black",         #"#007ACC"
            background="red",
            padding=10,
            relief="flat")
        self.storno1 = ttk.Button(self.parent, text="Storno časovače", style="Custom.TButton", command=lambda :(self.stop.set(), self.pokracujdále(), print(f"vlákno stornováno:{self.stop.is_set()}", print(f"{print(self.stop.set())}"))))
        self.storno1.grid(column=0,row=100)
    def obnov_GUI(self):
        self.parent.deiconify()
        self.text.grid()
    def pokracujdále(self):
        print("probehlo")
        self.booll = False
    def nove_okno(self):
        podrazene_okno = tk.Toplevel(self.parent)
run = True
root = tkinter.Tk()
root.configure(background="#d9d9d5")
s = (ttk.Style())
s.theme_use("flatly")
s.configure("Cervene.TButton",
    foreground='black',
    background='white',
    padding=0, relief="flat",font=("Helvetica",14))
app1 = MainWindow(root)
app1.mainloop()
