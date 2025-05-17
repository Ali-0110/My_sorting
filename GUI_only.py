### JUST THE GUI CODE ###
import tkinter as tk
from tkinter import ttk
import random

class Sorting_GUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry("1180x900")
        self.root.resizable(False, False)
        self.root.config(bg="#002b56")
        self.algorithms = ["Bubble Sort","Merge Sort","Selection Sort","Quick Sort"]
        self.selected_algorithm = tk.StringVar(value="Choose an algorithm...")

        self.speed = tk.DoubleVar(value=50)

        self.setup()

    def setup(self):

        title_label = tk.Label(self.root, text="Sorting Algorithm Visualizer", font=("Press Start 2P", 32, "bold"), fg="#000000")
        title_label.pack(padx=20,pady=30)

        tk.Label(root, text="Algorithm:", font=("Press Start 2P", 20)).place(x= 50, y=130)

        algo_menu = ttk.Combobox(root, textvariable=self.selected_algorithm, values=self.algorithms, state="readonly", font=("Arial", 13))
        algo_menu.place(x=50, y=170)

        tk.Label(root, text="Speed:", font=("Press Start 2P", 14)).place(x = 240, y=786)
        speed_slider = tk.Scale(root, from_=1, to=200, orient=tk.HORIZONTAL, variable=self.speed, length=548)
        speed_slider.place(x= 510 , y= 790)

        button_font = ("Arial", 13, "bold")

        generate_btn = tk.Button(root, text="Generate Array", command= self.generate_BTN, font=button_font, width=15, height=1, bg="#e0e0e0")
        generate_btn.place(x= 850 ,y=160)

        start_btn = tk.Button(root, text="Start", command=self.start_BTN, font=button_font, width=10, height=1, bg="#34c759", fg="white")
        start_btn.place(x=690 , y= 249)

        pause_btn = tk.Button(root, text="Pause", command=self.pause_BTN, font=button_font, width=10, height=1, bg="#ffd966", fg="#333")
        pause_btn.place(x=820, y= 249 )

        stop_btn = tk.Button(root, text="Stop", command=self.stop_BTN, font=button_font, width=10, height=1, bg="#ff3b30", fg="white")
        stop_btn.place(x=950, y=249 )

        self.canvas = tk.Canvas(self.root, width=900, height=500, bg="white")
        self.canvas.place(x=160,y=280)

    
    def _draw_bars(self, color="#000000"):
        self.canvas.delete("all")
        if not hasattr(self, 'data'):
            return
        c_height = 500 
        c_width = 900  
        x_width = c_width / len(self.data)
        offset = 5
        spacing = 2
        for i, height in enumerate(self.data):
            if self.data :
                O_height = (height / max(self.data)) * (c_height - 20) 
            else :
                O_height = 0
            x0 = i * x_width + offset
            y0 = c_height - O_height - 10 
            x1 = (i + 1) * x_width + offset - spacing
            y1 = c_height - 10 
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        self.root.update_idletasks()

    def generate_BTN(self):
        
        self.data = [random.randint(0, 300) for _ in range(20)]
        self._draw_bars(color="#000000")
        
        self.paused = False
        self.sorting = False


    def start_BTN(self):
        if not hasattr(self, 'data'):
            self.generate_BTN()
        self._draw_bars(color="#BB0000")
        self.Choosing_alg()
       
    def pause_BTN(self):
        if not hasattr(self, 'paused'):
            self.paused = False
        self.paused = not self.paused
        if self.paused:
            self.root.title("Sorting Paused")
        else:
            self.root.title("Sorting Resumed")

    def stop_BTN(self):
        if hasattr(self, 'data'):
            self._draw_bars(color="#000000")
        self.paused = False

    def Choosing_alg (self):
        self.sorting = True 
        if self.selected_algorithm.get() == "Bubble Sort":
            self.bubble_sort()
        elif self.selected_algorithm.get() == "Merge Sort":
            self.merge_sort()
        elif self.selected_algorithm.get() == "Selection Sort":
            self.selection_sort()
        elif self.selected_algorithm.get() == "Quick Sort":
            self.quick_sort()    

    


    

if __name__ == "__main__":
    root = tk.Tk()
    app = Sorting_GUI(root)
    root.mainloop()