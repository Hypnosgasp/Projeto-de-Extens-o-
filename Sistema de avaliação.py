import tkinter as tk
from tkinter import messagebox

class Avaliacao:
    def __init__(self, estabelecimento, qualidade_comida, atendimento, ambiente, musica, comentario=None):
        self.estabelecimento = estabelecimento
        self.qualidade_comida = qualidade_comida
        self.atendimento = atendimento
        self.ambiente = ambiente
        self.musica = musica
        self.comentario = comentario

    def __str__(self):
        return (f'Estabelecimento: {self.estabelecimento}\n'
                f'Qualidade da Comida: {self.qualidade_comida}\n'
                f'Atendimento: {self.atendimento}\n'
                f'Ambiente: {self.ambiente}\n'
                f'Música: {self.musica}\n'
                f'Comentário: {self.comentario if self.comentario else "Nenhum"}\n')

avaliacoes = []

def registrar_avaliacao():
    estabelecimento = entry_estabelecimento.get()
    qualidade_comida = scale_comida.get()
    atendimento = scale_atendimento.get()
    ambiente = scale_ambiente.get()
    musica = scale_musica.get()
    comentario = text_comentario.get("1.0", "end-1c")

    avaliacao = Avaliacao(estabelecimento, qualidade_comida, atendimento, ambiente, musica, comentario)
    avaliacoes.append(avaliacao)
    
    messagebox.showinfo("Sucesso", "Avaliação registrada com sucesso!")
    limpar_formulario()

def exibir_avaliacoes():
    texto_avaliacoes.delete("1.0", tk.END)
    if not avaliacoes:
        texto_avaliacoes.insert(tk.END, "Nenhuma avaliação registrada ainda.\n")
    else:
        for avaliacao in avaliacoes:
            texto_avaliacoes.insert(tk.END, str(avaliacao) + "\n" + "-" * 30 + "\n")

def limpar_formulario():
    entry_estabelecimento.delete(0, tk.END)
    scale_comida.set(1)
    scale_atendimento.set(1)
    scale_ambiente.set(1)
    scale_musica.set(1)
    text_comentario.delete("1.0", tk.END)

root = tk.Tk()
root.title("Avaliação de Estabelecimentos")

tk.Label(root, text="Nome do Estabelecimento:").grid(row=0, column=0)
entry_estabelecimento = tk.Entry(root)
entry_estabelecimento.grid(row=0, column=1)

tk.Label(root, text="Qualidade da Comida (1-5):").grid(row=1, column=0)
scale_comida = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL)
scale_comida.grid(row=1, column=1)

tk.Label(root, text="Atendimento (1-5):").grid(row=2, column=0)
scale_atendimento = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL)
scale_atendimento.grid(row=2, column=1)

tk.Label(root, text="Ambiente (1-5):").grid(row=3, column=0)
scale_ambiente = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL)
scale_ambiente.grid(row=3, column=1)

tk.Label(root, text="Música (1-5):").grid(row=4, column=0)
scale_musica = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL)
scale_musica.grid(row=4, column=1)

tk.Label(root, text="Comentário:").grid(row=5, column=0)
text_comentario = tk.Text(root, height=4, width=30)
text_comentario.grid(row=5, column=1)

tk.Button(root, text="Registrar Avaliação", command=registrar_avaliacao).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Exibir Avaliações", command=exibir_avaliacoes).grid(row=7, column=0, columnspan=2)

texto_avaliacoes = tk.Text(root, height=10, width=50)
texto_avaliacoes.grid(row=8, column=0, columnspan=2)

root.mainloop()
