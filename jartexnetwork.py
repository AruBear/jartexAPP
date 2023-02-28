import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

class App:
    def __init__(self, master):
        self.master = master
        master.title("JartexNetwork")

        style = ttk.Style()
        style.configure('TButton', foreground='black', background="blue", font=('Arial', 12), width=20)

        self.vote_button = ttk.Button(master, text="Vote", command=self.vote, style='TButton')
        self.vote_button.pack(pady=10)

        self.greport_button = ttk.Button(master, text="Gameplay Report", command=self.greport, style='TButton')
        self.greport_button.pack(pady=10)

        self.creport_button = ttk.Button(master, text="Chat Report", command=self.creport, style='TButton')
        self.creport_button.pack(pady=10)

    def greport(self):
        webbrowser.open_new_tab("https://jartexnetwork.com/form/10/select")

    def creport(self):
        webbrowser.open_new_tab("https://jartexnetwork.com/form/9/select")

    def vote(self):
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/1")
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/2")
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/3")
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/4")
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/5")
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/6")
        webbrowser.open_new_tab("https://vote.jartexnetwork.com/7")

root = tk.Tk()
root.geometry("400x150")
root.configure(bg='#ff9900')
app = App(root)
root.mainloop()
