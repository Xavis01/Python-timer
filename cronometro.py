#Código base:
# import time
# qtd_min = int(input("Quantos minutos deseja cronômetrar? "))
# qtd_min -= 1

# for min in range(qtd_min, -1, -1):
#     for sec in range(59, -1, -1):
#         print(f"{min:02d}:{sec:02d}", end="\r")
#         time.sleep(1)
# print("Tempo encerrado!")


import time
import tkinter as tk
from PIL import ImageTk, Image


def iniciar_timer():
    tempo_digitado = tempo_inicial.get() 
    if tempo_digitado.isdigit():
        tempo_min = int(tempo_digitado)
        tempo_restante = tempo_min * 60
        atualizar_tempo(tempo_restante)
    

def atualizar_tempo(tempo_restante):
    if tempo_restante > -1:
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60
        time_formatado = "{:02d}:{:02d}".format(minutos, segundos)
        rotulo_time.config(text=time_formatado)
        
        if tempo_restante == 0:
            mensagem.config(text="Tempo esgotado!")
            window1.after(5000, ocultar_mensagem)
        
        window1.after(1000, atualizar_tempo, tempo_restante -1)
        
def ocultar_mensagem():
    mensagem.config(text="")

#criando janela principal
window1 = tk.Tk()
window1.title("Cronômetro")
altura = 500
largura = 600
window1.geometry(f"{largura}x{altura}")
window1.configure(bg="#055e69")

tempo_inicial = tk.StringVar()

#criando escrita
fonte1 = ("Arial", 18, "bold")
text1 = tk.Label(window1,
                 text="Seja bem vindo!\nEste é um simulador de cronômetro.",
                 font=fonte1,
                 bg="#89dbe6",
                 width=30,
                 height=3,
                 relief="solid")
text1.place(relx=0.5, y=60, anchor="center")

#escrita 2
text2 = tk.Label(window1,
                 text="Digite abaixo quantos minutos\n deseja cronômetrar",
                 font=fonte1,
                 bg="#89dbe6",
                 width=25,
                 height=2,
                 relief="solid")
text2.place(relx=0.5, y=150, anchor="center")

#criando input
qtd_min = tk.Entry(window1,
                   textvariable=tempo_inicial,
                   width=2,
                   font=fonte1,
                   relief="solid",
                   borderwidth=2,
                   bg="#89dbe6")
qtd_min.place(relx=0.5, y=220, anchor="center")

#criando botao
fonte2 = ("Arial", 16, "bold")
iniciar = tk.Button(window1,
                    text="Iniciar",
                    font=fonte2,
                    relief="solid",
                    bd=0,
                    command=iniciar_timer)
iniciar.configure(borderwidth=2,
                  highlightthickness=2,
                  bg="#89dbe6")
iniciar.place(relx=0.5, y=275, anchor="center")

#mostrar tempo
rotulo_time = tk.Label(window1,
                       text="00:00",
                       font=("Arial", 40, "bold"),)
rotulo_time.place(relx=0.5, y=370, anchor="center")
rotulo_time.configure(bg="#055e69")

#mensagem de finalizado
mensagem = tk.Label(window1,
                    text="",
                    font=fonte2,
                    bg="#055e69",
                    fg="#89dbe6")
mensagem.place(relx=0.5, y=410, anchor="center")

#creditos finais
creditos = tk.Label(window1,
                    text="Feito por Lucas Xavier :)",
                    font=("Arial", 8),
                    fg="#89dbe6",
                    bg="#055e69")
creditos.place(x=5, y=480)

#colocando o perry :)
# image = Image.open(r"C:\Users\lucas\Pictures\perry.png")
# image = image.resize((100,100))
# photo = ImageTk.PhotoImage(image)

# imagem = tk.Label(window1, image = photo,)
# imagem.place(relx=0.5, rely=0.5)


#criando loop para janela se manter aberta
window1.mainloop()