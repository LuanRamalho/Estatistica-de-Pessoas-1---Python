import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        # Captura os valores digitados
        valores = [int(entry.get()) for entry in entries]
        
        # Calcula o total de pessoas
        total = sum(valores)
        label_total.config(text=f"Total de pessoas pesquisadas: {total}")
        
        # Calcula as porcentagens e atualiza as barras
        if total > 0:
            porcentagens = [(valor / total) * 100 for valor in valores]

            for i, (pct, progress, label_pct) in enumerate(zip(porcentagens, progress_bars, labels_pct)):
                progress['value'] = pct
                label_pct.config(text=f"{pct:.1f}%")
    except ValueError:
        label_total.config(text="Por favor, insira valores válidos em todos os campos")

# Configuração da janela
root = tk.Tk()
root.title("Estatísticas de Preferência de Esportes")
root.configure(bg="#E8F6F3")

# Lista de esportes e seus respectivos rótulos
esportes = ["Futebol", "Basquete", "Vôlei", "Handebol"]
entries = []
progress_bars = []
labels_pct = []

# Estilos para cores e fontes
style = ttk.Style()
style.configure("TProgressbar", thickness=20, troughcolor="#E0E0E0")
label_font = ("Helvetica", 10, "bold")
entry_bg = "#FFFFFF"
entry_fg = "#2C3E50"
bg_color = "#AED6F1"
btn_bg = "#5DADE2"
btn_fg = "#FFFFFF"

# Criação dos campos de entrada e das barras de progresso
for i, esporte in enumerate(esportes):
    tk.Label(root, text=f"Pessoas que curtem {esporte}:", bg="#E8F6F3", font=label_font).grid(row=i, column=0, padx=5, pady=5, sticky='w')
    entry = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=("Helvetica", 10))
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

    tk.Label(root, text=esporte, bg="#E8F6F3", font=("Helvetica", 10, "bold")).grid(row=i, column=2, sticky='w', padx=5)
    progress = ttk.Progressbar(root, length=200, maximum=100, style="TProgressbar")
    progress.grid(row=i, column=3, padx=5, pady=5)
    progress_bars.append(progress)

    label_pct = tk.Label(root, text="0.0%", bg="#E8F6F3", font=("Helvetica", 10, "bold"))
    label_pct.grid(row=i, column=4, padx=5)
    labels_pct.append(label_pct)

# Botão para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular, bg=btn_bg, fg=btn_fg, font=("Helvetica", 12, "bold"))
btn_calcular.grid(row=len(esportes), column=0, columnspan=5, pady=10)

# Exibe o total de pessoas
label_total = tk.Label(root, text="Total de pessoas pesquisadas: ", bg="#E8F6F3", font=("Helvetica", 15, "bold"))
label_total.grid(row=len(esportes) + 1, column=0, columnspan=5, pady=5)

root.mainloop()
