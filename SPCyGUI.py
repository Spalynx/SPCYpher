import tkinter as tk
import time
import SPCypher

class SPCyGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.pack()
        self.createWidgets()

    def createWidgets(self):
        instr = tk.Label(self, text = "Enter A, B, and Text, and hit the button.")
        bottom_fr = tk.Frame(self, width=50)
        self.compute = tk.Button(bottom_fr)
        self.QUIT = tk.Button(bottom_fr)

        #setting attributes of compute and quit buttons
        self.compute["text"] = "Convert"
        self.compute["command"] = self.cypher
        self.QUIT["text"] ="QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = root.destroy

        #mainly an output block
        self.cypher = tk.Entry(self,width=45)
        cypher_label = tk.Label(self,text = "The plaintext converted:")
        self.cypher.pack(side="bottom")        
        cypher_label.pack(side="bottom")
        
        #packing everything
        instr.pack();
        bottom_fr.pack(side="bottom")
        self.inputWidgets();
        self.compute.pack(side="left")
        self.QUIT.pack(side="right")


    def inputWidgets(self):
        input_fr = tk.Frame(self,width=30)

        #The items for the input block, A,B,Text
        self.spac = tk.Label(input_fr,text="= A \t\t B = ")
        self.v = tk.IntVar(input_fr)
        self.B = tk.Entry(input_fr,width = 10)
        A = tk.OptionMenu(input_fr,self.v, 2, 13, 26)
        self.text = tk.Entry(self,width=45)

        #default values of A and B
        self.v.set(3);
        self.B.insert(0,"3")

        #packing all of the input block
        input_fr.pack()
        self.B.pack(side = "right")
        A.pack(side = "left")
        self.spac.pack(side="left")

        self.text.pack()
        return;
        
    def cypher(self):
        try:
            #does the base cypher conversion
            sp = SPCypher.SPCypher()
            sp.setA(self.v.get())
            sp.setB(int(self.B.get()))

            #exception handling is relatively minimal
            self.cypher.delete(0, tk.END);
            self.cypher.insert(0, sp.toCypher(self.text.get()))
        except(Exception):
            #this sucks, fix it later
            print("You goofed. B must be an int.")
            self.spac["fg"] = "red"

root = tk.Tk()
root.title("SPiCY")
root.resizable(width=0, height=0)
root.geometry('{}x{}'.format(300,200))
app = SPCyGui(master=root)
app.mainloop()
time.sleep(2)
