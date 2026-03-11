import tkinter as tk
from tkinter import ttk
import simulari
import sys

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.geometry("900x800")
root.title("Meniu Principal")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


'''partea de style'''
style = ttk.Style()
style.theme_use("clam") 
style.configure("Custom.TFrame", background="#f7f7f7") 

style.configure(
    "Custom.TButton",
    font=("Arial", 11, "bold"),
    foreground="#000000",
    background="#87CEEB",
    padding=(20, 10),
    relief="flat"
)
style.map(
    "Custom.TButton",
    background=[("active", "#ADD8E6")]  
)

def defineste_stil_entry():
    style.configure(
        "Custom.TEntry",
        padding=5,
        foreground="#000000",
        fieldbackground="#f0f8ff",  # interior
        background="#f0f8ff",       # margine
        bordercolor="#4169E1",
        lightcolor="#87CEEB",
        darkcolor="#4682B4",
        relief="solid"
    )

    style.map(
        "Custom.TEntry",
        bordercolor=[("focus", "#2196F3")],
        lightcolor=[("focus", "#2196F3")]
    )

def show_frame(frame_to_show):
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Frame):
            widget.pack_forget()
    frame_to_show.pack(fill="both", expand=True)

# FOOTER
footer = tk.Frame(root, bg="#B6D0E2")  
footer.pack(side="bottom", fill="x")

label_autori = tk.Label(
    footer,
    text="Proiect realizat de: Pogonici-Bălțățeanu Tiberiu, Voicu Alexandru-Mihăiță, Chițimia Diana-Andreea",
    bg="#B6D0E2",
    fg="#333333",
    font=("Segoe UI", 9)
)
label_autori.pack(pady=5)

'''sfarsit partea de style'''

# PAGINA PRINCIPALA
defineste_stil_entry()

pagina_PRN = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_PRN, text="Alegeți tipul de variabilă aleatoare de simulat", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
subtitlu1 = ttk.Label(pagina_PRN, text="Variabilă aleatoare discretă", font=("Segoe UI", 12), background="#f7f7f7")
titlu.pack(pady=20)
subtitlu1.pack(pady=50)


button1 = ttk.Button(pagina_PRN, text="Mergi la VAD", command=lambda: show_frame(pagina_VAD),style="Custom.TButton" )
button1.pack(pady=0)

subtitlu2 = ttk.Label(pagina_PRN, text="Variabilă aleatoare continuă", font=("Segoe UI", 12), background="#f7f7f7")
subtitlu2.pack(pady=50)

button2 = ttk.Button(pagina_PRN, text="Mergi la VAC", command=lambda: show_frame(pagina_VAC),style="Custom.TButton")
button2.pack(pady=0)

subtitlu3 = ttk.Label(pagina_PRN, text="Vectori aleatori uniform distribuiti", font=("Segoe UI", 12), background="#f7f7f7")
subtitlu3.pack(pady=50)

button3 = ttk.Button(pagina_PRN, text="Mergi la vectori", command=lambda: show_frame(pagina_VECT),style="Custom.TButton")
button3.pack(pady=0)


#PAGINA VARIABILE ALEATOARE DISCRETE 

pagina_VAD = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_VAD, text="Variabile aleatoare discrete", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

bernouli = ttk.Label(pagina_VAD, text="Bernoulli", font=("Segoe UI", 12), background="#f7f7f7")
bernouli.pack(pady=20)

button1 = ttk.Button(pagina_VAD, text="Bernoulli", command=lambda: show_frame(pagina_BERN), style="Custom.TButton")
button1.pack(pady=0)

binomiala = ttk.Label(pagina_VAD, text="Binomiala", font=("Segoe UI", 12), background="#f7f7f7")
binomiala.pack(pady=20)

button2 = ttk.Button(pagina_VAD, text="Binomiala", command=lambda: show_frame(pagina_BIN), style="Custom.TButton")
button2.pack(pady=0)

geometrica = ttk.Label(pagina_VAD, text="Geometrica", font=("Segoe UI", 12), background="#f7f7f7")
geometrica.pack(pady=20)

button3 = ttk.Button(pagina_VAD, text="Geometrica", command=lambda: show_frame(pagina_GEOM), style="Custom.TButton")
button3.pack(pady=0)

poisson = ttk.Label(pagina_VAD, text="Poisson", font=("Segoe UI", 12), background="#f7f7f7")
poisson.pack(pady=20)

button4 = ttk.Button(pagina_VAD, text="Poisson", command=lambda: show_frame(pagina_POIS),style="Custom.TButton")
button4.pack(pady=0)

poisson = ttk.Label(pagina_VAD, text="Uniforma", font=("Segoe UI", 12), background="#f7f7f7")
poisson.pack(pady=20)

button4 = ttk.Button(pagina_VAD, text="Uniforma", command=lambda: show_frame(pagina_UNIF2),style="Custom.TButton")
button4.pack(pady=0)
button_trimitere_inapoi = ttk.Button(pagina_VAD, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom',pady=50)


#PAGINA VARIABILE ALEATOARE CONTINUE


pagina_VAC = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_VAC, text="Variabile aleatoare continue", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

exponentiala = ttk.Label(pagina_VAC, text="Exponentiala", font=("Segoe UI", 12), background="#f7f7f7")
exponentiala.pack(pady=20)

button1 = ttk.Button(pagina_VAC, text="Exponentiala", command=lambda: show_frame(pagina_EXP), style="Custom.TButton")
button1.pack(pady=0)

unif = ttk.Label(pagina_VAC, text="Uniforma", font=("Segoe UI", 12), background="#f7f7f7")
unif.pack(pady=20)

button2 = ttk.Button(pagina_VAC, text="Uniforma", command=lambda: show_frame(pagina_UNIF), style="Custom.TButton")
button2.pack(pady=0)

normala = ttk.Label(pagina_VAC, text="Normala", font=("Segoe UI", 12), background="#f7f7f7")
normala.pack(pady=20)

button1 = ttk.Button(pagina_VAC, text="Normala", command=lambda: show_frame(pagina_NORM), style="Custom.TButton")
button1.pack(pady=0)

button_trimitere_inapoi = ttk.Button(pagina_VAC, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom',pady=50)


#PAGINA VECTORI ALEATORI


pagina_VECT = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_VECT, text="Vectori aleatori uniform distribuiți", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

dreptunghi = ttk.Label(pagina_VECT, text="Pe un dreptunghi", font=("Segoe UI", 12), background="#f7f7f7")
dreptunghi.pack(pady=20)

button1 = ttk.Button(pagina_VECT, text="Dreptunghi", command=lambda: show_frame(pagina_DREPTUNGHI), style="Custom.TButton")
button1.pack(pady=0)

cerc = ttk.Label(pagina_VECT, text="Pe un cerc", font=("Segoe UI", 12), background="#f7f7f7")
cerc.pack(pady=20)

button2 = ttk.Button(pagina_VECT, text="Cerc", command=lambda: show_frame(pagina_CERC), style="Custom.TButton")
button2.pack(pady=0)

elipsa = ttk.Label(pagina_VECT, text="Pe o elipsă", font=("Segoe UI", 12), background="#f7f7f7")
elipsa.pack(pady=20)

button1 = ttk.Button(pagina_VECT, text="Elipsa", command=lambda: show_frame(pagina_ELIPSA), style="Custom.TButton")
button1.pack(pady=0)

button_trimitere_inapoi = ttk.Button(pagina_VECT, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom',pady=50)


#PAGINA BERNOULLI

pagina_BERN = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_BERN, text="Bernoulli", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_BERN, text="Dați probabilitatea", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)


entry_prob_bernoulli = ttk.Entry(pagina_BERN, style="Custom.TEntry")
entry_prob_bernoulli.pack(pady=10)

text2 = ttk.Label(pagina_BERN, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)


entry_simulari_bernoulli = ttk.Entry(pagina_BERN, style="Custom.TEntry")
entry_simulari_bernoulli.pack(pady=10)

button1 = ttk.Button(pagina_BERN, text="Simulează", command=lambda: simulari.Bernoulli(entry_simulari_bernoulli.get(),entry_prob_bernoulli.get()), style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_BERN, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom',pady=50)

button_trimitere_opaginapoi = ttk.Button(pagina_BERN, text="O pagină înapoi", command=lambda: show_frame(pagina_VAD), style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=0)


#PAGINA BINOMIALA

pagina_BIN = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_BIN, text="Binomiala", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_BIN, text="Dați probabilitatea", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_prob_bin = ttk.Entry(pagina_BIN,style="Custom.TEntry")
entry_prob_bin.pack(pady=10)

text2 = ttk.Label(pagina_BIN, text="Dați numărul de incercari", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_numar_bin = ttk.Entry(pagina_BIN,style="Custom.TEntry")
entry_numar_bin.pack(pady=10)

text3 = ttk.Label(pagina_BIN, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text3.pack(pady=20)

entry_simulari_bin = ttk.Entry(pagina_BIN,style="Custom.TEntry")
entry_simulari_bin.pack(pady=10)

button1 = ttk.Button(pagina_BIN, text="Simulează", command=lambda: simulari.Binomiala(entry_prob_bin.get(),entry_simulari_bin.get(),entry_numar_bin.get()), style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_BIN, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton", width=30)
button_trimitere_inapoi.pack(side='bottom',pady=(10,5))

button_trimitere_opaginapoi = ttk.Button(pagina_BIN, text="O pagină înapoi", command=lambda: show_frame(pagina_VAD),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=(0, 30))



#GEOMETRICA

pagina_GEOM = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_GEOM, text="Geometrica", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_GEOM, text="Dați probabilitatea", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_prob_geom = ttk.Entry(pagina_GEOM,style="Custom.TEntry")
entry_prob_geom.pack(pady=10)

text2 = ttk.Label(pagina_GEOM, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_simulari_geom = ttk.Entry(pagina_GEOM,style="Custom.TEntry")
entry_simulari_geom.pack(pady=10)

button1 = ttk.Button(pagina_GEOM, text="Simulează", command=lambda: simulari.Geometrica(entry_prob_geom.get(),entry_simulari_geom.get()),style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_GEOM, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN),style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom',pady=50)

button_trimitere_opaginapoi = ttk.Button(pagina_GEOM, text="O pagină înapoi", command=lambda: show_frame(pagina_VAD),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=0)


# POISSON

pagina_POIS = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_POIS, text="Poisson", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_POIS, text="Dați valoarea λ (lambda)", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_lambda_poisson = ttk.Entry(pagina_POIS,style="Custom.TEntry")
entry_lambda_poisson.pack(pady=10)

text2 = ttk.Label(pagina_POIS, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_simulari_poisson = ttk.Entry(pagina_POIS,style="Custom.TEntry")
entry_simulari_poisson.pack(pady=10)

button1 = ttk.Button(pagina_POIS, text="Simulează", command=lambda: simulari.Poisson(entry_lambda_poisson.get(), entry_simulari_poisson.get()),style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_POIS, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN),style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom', pady=50)

button_trimitere_opaginapoi = ttk.Button(pagina_POIS, text="O pagină înapoi", command=lambda: show_frame(pagina_VAD),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom', pady=0)

#UNIFORMA DISCRETA

pagina_UNIF2 = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_UNIF2, text="Uniformă", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_UNIF2, text="Dați limita inferioară", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_min_unif2 = ttk.Entry(pagina_UNIF2,style="Custom.TEntry")
entry_min_unif2.pack(pady=10)

text2 = ttk.Label(pagina_UNIF2, text="Dați limita superioară", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_max_unif2 = ttk.Entry(pagina_UNIF2,style="Custom.TEntry")
entry_max_unif2.pack(pady=10)

text3 = ttk.Label(pagina_UNIF2, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text3.pack(pady=20)

entry_simulari_unif2 = ttk.Entry(pagina_UNIF2,style="Custom.TEntry")
entry_simulari_unif2.pack(pady=10)

button1 = ttk.Button(pagina_UNIF2, text="Simulează", command=lambda: simulari.Uniforma2(entry_simulari_unif2.get(), entry_min_unif2.get(), entry_max_unif2.get()), style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_UNIF2, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN),style="Custom.TButton", width=30 )
button_trimitere_inapoi.pack(side='bottom',pady=(10, 5))

button_trimitere_opaginapoi = ttk.Button(pagina_UNIF2, text="O pagină înapoi", command=lambda: show_frame(pagina_VAD),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=(0, 30))


#EXPONENTIALA

pagina_EXP = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_EXP, text="Exponențială", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_EXP, text="Dați lambda (rata)", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_lambda_exp = ttk.Entry(pagina_EXP,style="Custom.TEntry")
entry_lambda_exp.pack(pady=10)

text2 = ttk.Label(pagina_EXP, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_simulari_exp = ttk.Entry(pagina_EXP,style="Custom.TEntry")
entry_simulari_exp.pack(pady=10)

button1 = ttk.Button(pagina_EXP, text="Simulează", command=lambda: simulari.Exponentiala(entry_simulari_exp.get(), entry_lambda_exp.get()),style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_EXP, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN),style="Custom.TButton")
button_trimitere_inapoi.pack(side='bottom', pady=50)

button_trimitere_opaginapoi = ttk.Button(pagina_EXP, text="O pagină înapoi", command=lambda: show_frame(pagina_VAC),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom', pady=0)


#UNIFROMA

pagina_UNIF = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_UNIF, text="Uniformă", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_UNIF, text="Dați limita inferioară", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_min_unif = ttk.Entry(pagina_UNIF,style="Custom.TEntry")
entry_min_unif.pack(pady=10)

text2 = ttk.Label(pagina_UNIF, text="Dați limita superioară", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_max_unif = ttk.Entry(pagina_UNIF,style="Custom.TEntry")
entry_max_unif.pack(pady=10)

text3 = ttk.Label(pagina_UNIF, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text3.pack(pady=20)

entry_simulari_unif = ttk.Entry(pagina_UNIF,style="Custom.TEntry")
entry_simulari_unif.pack(pady=10)

button1 = ttk.Button(pagina_UNIF, text="Simulează", command=lambda: simulari.Uniforma(entry_simulari_unif.get(), entry_min_unif.get(), entry_max_unif.get()), style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_UNIF, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN),style="Custom.TButton", width=30 )
button_trimitere_inapoi.pack(side='bottom',pady=(10, 5))

button_trimitere_opaginapoi = ttk.Button(pagina_UNIF, text="O pagină înapoi", command=lambda: show_frame(pagina_VAC),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=(0, 30))

#NORMALA

pagina_NORM = ttk.Frame(root, style="Custom.TFrame")

titlu = ttk.Label(pagina_NORM, text="Normală", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu.pack(pady=20)

text1 = ttk.Label(pagina_NORM, text="Dați media (mu)", font=("Segoe UI", 12), background="#f7f7f7")
text1.pack(pady=20)

entry_mu_norm = ttk.Entry(pagina_NORM,style="Custom.TEntry")
entry_mu_norm.pack(pady=10)

text2 = ttk.Label(pagina_NORM, text="Dați deviația standard (sigma)", font=("Segoe UI", 12), background="#f7f7f7")
text2.pack(pady=20)

entry_sigma_norm = ttk.Entry(pagina_NORM,style="Custom.TEntry")
entry_sigma_norm.pack(pady=10)

text3 = ttk.Label(pagina_NORM, text="Dați numărul de simulari", font=("Segoe UI", 12), background="#f7f7f7")
text3.pack(pady=20)

entry_simulari_norm = ttk.Entry(pagina_NORM,style="Custom.TEntry")
entry_simulari_norm.pack(pady=10)

button1 = ttk.Button(pagina_NORM, text="Simulează",command=lambda: simulari.Normala(entry_simulari_norm.get(), entry_mu_norm.get(), entry_sigma_norm.get()), style="Custom.TButton")
button1.pack(pady = 20)

button_trimitere_inapoi = ttk.Button(pagina_NORM, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton", width=30)
button_trimitere_inapoi.pack(side='bottom',pady=(10, 5))

button_trimitere_opaginapoi = ttk.Button(pagina_NORM, text="O pagină înapoi", command=lambda: show_frame(pagina_VAC), style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=(0, 30))


# Pagina Vector Aleator în Dreptunghi

pagina_DREPTUNGHI = ttk.Frame(root, style="Custom.TFrame")

titlu_dreptunghi = ttk.Label(pagina_DREPTUNGHI, text="Vectori aleatori în Dreptunghi", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu_dreptunghi.pack(pady=20)

text_lungime = ttk.Label(pagina_DREPTUNGHI, text="Limita inferioara axa OX", font=("Segoe UI", 12), background="#f7f7f7")
text_lungime.pack(pady=10)

entry_limita_1 = ttk.Entry(pagina_DREPTUNGHI,style="Custom.TEntry")
entry_limita_1.pack(pady=10)

text_latime = ttk.Label(pagina_DREPTUNGHI, text="Limita superioara axa OX", font=("Segoe UI", 12), background="#f7f7f7")
text_latime.pack(pady=10)

entry_limita_2 = ttk.Entry(pagina_DREPTUNGHI, style="Custom.TEntry")
entry_limita_2.pack(pady=10)

text_lungime = ttk.Label(pagina_DREPTUNGHI, text="Limita inferioara axa OY", font=("Segoe UI", 12), background="#f7f7f7")
text_lungime.pack(pady=10)

entry_limita_3 = ttk.Entry(pagina_DREPTUNGHI,style="Custom.TEntry")
entry_limita_3.pack(pady=10)

text_latime = ttk.Label(pagina_DREPTUNGHI, text="Limita superioara axa OY", font=("Segoe UI", 12), background="#f7f7f7")
text_latime.pack(pady=10)

entry_limita_4 = ttk.Entry(pagina_DREPTUNGHI, style="Custom.TEntry")
entry_limita_4.pack(pady=10)

text_simulari_dreptunghi = ttk.Label(pagina_DREPTUNGHI, text="Număr de simulări", font=("Segoe UI", 12), background="#f7f7f7")
text_simulari_dreptunghi.pack(pady=10)

entry_simulari_dreptunghi = ttk.Entry(pagina_DREPTUNGHI, style="Custom.TEntry")
entry_simulari_dreptunghi.pack(pady=10)

button_simulare_dreptunghi = ttk.Button(pagina_DREPTUNGHI,text="Simulează",command=lambda:simulari.Dreptunghi(entry_simulari_dreptunghi.get(),entry_limita_1.get(),entry_limita_2.get(),entry_limita_3.get(),entry_limita_4.get(),), style="Custom.TButton")
button_simulare_dreptunghi.pack(pady=20)

button_inapoi_dreptunghi = ttk.Button(pagina_DREPTUNGHI,text="Înapoi la pagina principală",command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_inapoi_dreptunghi.pack(side='bottom',pady=(0, 30))

button_trimitere_opaginapoi = ttk.Button(pagina_DREPTUNGHI, text="O pagină înapoi", command=lambda: show_frame(pagina_VECT), style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom',pady=(10, 5))



# Pagina Vector Aleator în Cerc

pagina_CERC = ttk.Frame(root, style="Custom.TFrame")

titlu_cerc = ttk.Label(pagina_CERC, text="Vectori aleatori în Cerc", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu_cerc.pack(pady=20)

text_raza_cerc = ttk.Label(pagina_CERC, text="Raza (r)", font=("Segoe UI", 12), background="#f7f7f7")
text_raza_cerc.pack(pady=10)

entry_raza_cerc = ttk.Entry(pagina_CERC, style="Custom.TEntry")
entry_raza_cerc.pack(pady=10)

text_simulari_cerc = ttk.Label(pagina_CERC, text="Număr de simulări", font=("Segoe UI", 12), background="#f7f7f7")
text_simulari_cerc.pack(pady=10)

entry_simulari_cerc = ttk.Entry(pagina_CERC, style="Custom.TEntry")
entry_simulari_cerc.pack(pady=10)

button_simulare_cerc = ttk.Button(pagina_CERC,text="Simulează",command=lambda: simulari.Disc(entry_simulari_cerc.get(),entry_raza_cerc.get()),style="Custom.TButton")
button_simulare_cerc.pack(pady=20)

button_inapoi_cerc = ttk.Button(pagina_CERC,text="Înapoi la pagina principală",command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_inapoi_cerc.pack(side='bottom', pady=50)

button_trimitere_opaginapoi = ttk.Button(pagina_CERC, text="O pagină înapoi", command=lambda: show_frame(pagina_VECT), style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom', pady=0)


# Pagina Vector Aleator în Elipsă

pagina_ELIPSA = ttk.Frame(root, style="Custom.TFrame")

titlu_elipsa = ttk.Label(pagina_ELIPSA, text="Vectori aleatori în Elipsă", font=("Segoe UI", 18, "bold"), background="#f7f7f7")
titlu_elipsa.pack(pady=20)

text_a_elipsa = ttk.Label(pagina_ELIPSA, text="Raza 1 (a)", font=("Segoe UI", 12), background="#f7f7f7")
text_a_elipsa.pack(pady=10)

entry_a_elipsa = ttk.Entry(pagina_ELIPSA, style="Custom.TEntry")
entry_a_elipsa.pack(pady=10)

text_b_elipsa = ttk.Label(pagina_ELIPSA, text="Raza 2 (b)", font=("Segoe UI", 12), background="#f7f7f7")
text_b_elipsa.pack(pady=10)

entry_b_elipsa = ttk.Entry(pagina_ELIPSA, style="Custom.TEntry")
entry_b_elipsa.pack(pady=10)

text_simulari_elipsa = ttk.Label(pagina_ELIPSA, text="Număr de simulări", font=("Segoe UI", 12), background="#f7f7f7")
text_simulari_elipsa.pack(pady=10)

entry_simulari_elipsa = ttk.Entry(pagina_ELIPSA, style="Custom.TEntry")
entry_simulari_elipsa.pack(pady=10)

button_simulare_elipsa = ttk.Button(
    pagina_ELIPSA,
    text="Simulează",
    command=lambda: simulari.Elipsa(entry_a_elipsa.get(),entry_b_elipsa.get(),entry_simulari_elipsa.get()), style="Custom.TButton")
button_simulare_elipsa.pack(pady=20)

button_inapoi_elipsa = ttk.Button(pagina_ELIPSA,text="Înapoi la pagina principală",command=lambda: show_frame(pagina_PRN),style="Custom.TButton")
button_inapoi_elipsa.pack(side='bottom', pady=50)

button_trimitere_opaginapoi = ttk.Button(pagina_ELIPSA, text="O pagină înapoi", command=lambda: show_frame(pagina_VECT),style="Custom.TButton")
button_trimitere_opaginapoi.pack(side='bottom', pady=0)



# Buton Înapoi
button_back = ttk.Button(pagina_VAD, text="Înapoi la pagina principală", command=lambda: show_frame(pagina_PRN), style="Custom.TButton")
button_back.pack(pady=20)

# === PORNEȘTE APLICAȚIA CU PAGINA PRINCIPALĂ ===
show_frame(pagina_PRN)
root.mainloop()

'''
show_frame(pagina_PRN)
if __name__ == "__main__":
    show_frame(pagina_PRN)
root.mainloop()'''

