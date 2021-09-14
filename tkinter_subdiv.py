import Tkinter as tk
from subdiv_document import SubdivDocument


class SubdivTkapp(tk.Frame):
    """Subdiv toy tk application"""
    def load(self):
        print "Loading"

    def save(self):
        print "Saving"

    def new_doc(self):
        print "Making new doc"
        
    def makeMenu(self):
        #Menu with: New, Load, Save
        #New -> Clear
        self.mb = tk.Menubutton(self, text="File")
        self.mb.grid()
        self.mb.menu = tk.Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu
        menu = self.mb.menu
        menu.add_command(label="New", command=self.new_doc)
        menu.add_command(label="Save", command=self.save)
        menu.add_command(label="Load", command=self.load)
        menu.add_command(label="Quit")
        self.mb.pack()
        
    def createWidgets(self):
        """Make default display"""
        #we want a main canvas to display the current doc
        #A menu 
        #resize min = 200
        self.makeMenu()
        
        self.canvas = tk.Canvas(self)
        self.canvas.pack()
        w, h = 400, 400
        hh = h / 2
        print w, h
        self.l1 = self.canvas.create_line(0, hh, w, hh)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.master.minsize(400, 400)
        self.master.title("Subdivision Toy")
        self.doc = SubdivDocument.make_test()
        self.line_id_list = []
        self.canvas_from_doc()

    def canvas_from_doc(self):
        """Draw all the canvas lines from a loaded doc"""
        #Delete/clear
        for line in self.line_id_list:
            self.canvas.delete(line)
        self.line_id_list = []
        #Get the lines
        new_lines = self.doc.get_lines(400, 400)
        #Draw them
        for line in new_lines:
            line_id = self.canvas.create_line(*line)
            self.line_id_list.append(line_id)
            
            
if __name__ == '__main__':
    root = tk.Tk()
    app = SubdivTkapp(master=root)
    app.mainloop()
    #root.destroy()
