import tkinter as tk
from tkinter import *
from banco import *
from tkinter import messagebox

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")

        self.janela39 = tk.Frame(master)
        self.janela39["padx"] = 20
        self.janela39.pack()

        self.img = PhotoImage(file="imagem/image.png")
        self.lbimg = Label(self.janela39, image=self.img)
        self.lbimg.pack()

        self.janela40 = tk.Frame(master)
        self.janela40["padx"] = 20
        self.janela40.pack()

        self.usuario_label = tk.Label(self.janela40, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela40, width=20)
        self.usuario.pack(side="left")

        self.janela41 = tk.Frame(master)
        self.janela41["padx"] = 20
        self.janela41.pack()

        self.senha_label = tk.Label(self.janela41, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela41, width=20, show="*")  # Oculta o texto da senha
        self.senha.pack(side="left")

        self.janela42 = tk.Frame(master)
        self.janela42["padx"] = 20
        self.janela42.pack()

        self.botao10 = tk.Button(self.janela42, width=10, text="Login", command=self.entrar)
        self.botao10.pack(side="left")

    def entrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        banco = banco()
        cursor = banco.conexao.cursor()

        # Verificando se o usuário e a senha estão corretos
        cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario=? AND senha=?", (usuario, senha))
        engual = cursor.fetchone()

        if engual:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.abrir()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        cursor.close()

    def abrir(self):
        self.new_window = tk.Toplevel(self.master)
 #       self.app = Mainform(self.new_window)

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = Login(master=root)
    root.mainloop()