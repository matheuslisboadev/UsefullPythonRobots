import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def mover_arquivos(raiz, log_area):
    arquivos_movidos = 0

    subpastas = [os.path.join(raiz, d) for d in os.listdir(raiz)
                 if os.path.isdir(os.path.join(raiz, d))]

    for subpasta in subpastas:
        for arquivo in os.listdir(subpasta):
            caminho_origem = os.path.join(subpasta, arquivo)
            if not os.path.isfile(caminho_origem):
                continue

            destino = os.path.join(raiz, arquivo)
            base, ext = os.path.splitext(arquivo)
            contador = 1

            while os.path.exists(destino):
                destino = os.path.join(raiz, f"{base}_{contador}{ext}")
                contador += 1

            try:
                shutil.move(caminho_origem, destino)
                arquivos_movidos += 1
                log_area.insert(tk.END, f"[✔] {arquivo} movido com sucesso.\n")
            except Exception as e:
                log_area.insert(tk.END, f"[✘] Erro ao mover {arquivo}: {e}\n")

        try:
            os.rmdir(subpasta)
            log_area.insert(tk.END, f"[ℹ] Pasta removida: {subpasta}\n")
        except OSError:
            log_area.insert(tk.END, f"[⚠] Pasta não está vazia: {subpasta}\n")

    log_area.insert(tk.END, f"\nTotal de arquivos movidos: {arquivos_movidos}\n")
    messagebox.showinfo("Concluído", f"Processo finalizado. {arquivos_movidos} arquivos movidos.")

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        log_area.delete(1.0, tk.END)
        mover_arquivos(pasta, log_area)

# GUI moderna com tema pastel
def criar_interface():
    janela = tk.Tk()
    janela.title("Organizador de Arquivos")
    janela.geometry("620x450")
    janela.configure(bg="#fef6f6")

    estilo = ttk.Style(janela)
    estilo.theme_use("clam")
    estilo.configure("TButton",
                     font=("Segoe UI", 10),
                     padding=10,
                     relief="flat",
                     background="#f7d9d9",
                     foreground="#444",
                     borderwidth=0)
    estilo.map("TButton",
               background=[("active", "#f2bfbf")],
               relief=[("pressed", "flat")])

    estilo.configure("TLabel", background="#fef6f6", foreground="#444")

    ttk.Label(janela, text="Mover arquivos das subpastas para a pasta principal").pack(pady=(20, 5))

    botao = ttk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
    botao.pack(pady=10)

    global log_area
    log_area = ScrolledText(janela, width=75, height=20, wrap=tk.WORD,
                            font=("Consolas", 9), bg="#fffafa", fg="#333",
                            borderwidth=2, relief="groove")
    log_area.pack(padx=15, pady=10)

    janela.mainloop()

criar_interface()
