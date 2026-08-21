import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import random
from datetime import datetime, timedelta

class EventFlowAnomalyStudio:
    def __init__(self, root):
        self.root = root
        self.root.title('EventFlow Anomaly Studio')
        self.root.geometry('1200x800')
        self.root.configure(bg='#1e1e1e')
        self.setup_ui()

    def setup_ui(self):
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Flow Diagram Tab
        self.flow_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.flow_frame, text='Flow Diagram')
        self.setup_flow_diagram()

        # Anomaly Detection Tab
        self.anomaly_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.anomaly_frame, text='Anomaly Detection')
        self.setup_anomaly_detection()

        # Time Series Tab
        self.time_series_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.time_series_frame, text='Time Series')
        self.setup_time_series()

    def setup_flow_diagram(self):
        self.canvas = tk.Canvas(self.flow_frame, bg='#2d2d2d', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.draw_flow_diagram()

    def draw_flow_diagram(self):
        self.canvas.delete('all')
        nodes = ['Kafka', 'Logs', 'APIs', 'Processor', 'Storage']
        positions = [(200, 100), (500, 100), (800, 100), (350, 300), (650, 300)]
        for i, node in enumerate(nodes):
            self.canvas.create_oval(positions[i][0]-50, positions[i][1]-50, positions[i][0]+50, positions[i][1]+50, fill='#3e3e3e', outline='#00ff00')
            self.canvas.create_text(positions[i][0], positions[i][1], text=node, fill='#ffffff')
        for i in range(len(nodes)-1):
            self.canvas.create_line(positions[i][0]+50, positions[i][1], positions[i+1][0]-50, positions[i+1][1], fill='#00ff00', width=2)

    def setup_anomaly_detection(self):
        self.anomaly_label = ttk.Label(self.anomaly_frame, text='Anomaly Detection Rules', background='#1e1e1e', foreground='#ffffff')
        self.anomaly_label.pack(pady=10)

        self.rule_text = tk.Text(self.anomaly_frame, bg='#2d2d2d', fg='#ffffff', insertbackground='#ffffff')
        self.rule_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.add_rule_button = ttk.Button(self.anomaly_frame, text='Add Rule', command=self.add_rule)
        self.add_rule_button.pack(pady=10)

    def add_rule(self):
        self.rule_text.insert(tk.END, 'New Rule:\n')

    def setup_time_series(self):
        self.figure = plt.figure(figsize=(10, 5), facecolor='#1e1e1e')
        self.plot = self.figure.add_subplot(111)
        self.plot.set_facecolor('#2d2d2d')
        self.plot.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.plot.spines['bottom'].set_color('#ffffff')
        self.plot.spines['top'].set_color('#ffffff')
        self.plot.spines['left'].set_color('#ffffff')
        self.plot.spines['right'].set_color('#ffffff')
        self.plot.tick_params(axis='x', colors='#ffffff')
        self.plot.tick_params(axis='y', colors='#ffffff')

        self.canvas_figure = FigureCanvasTkAgg(self.figure, self.time_series_frame)
        self.canvas_figure.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.update_time_series()

    def update_time_series(self):
        self.plot.clear()
        dates = [datetime.now() - timedelta(minutes=i) for i in range(10)][::-1]
        values = [random.randint(0, 100) for _ in range(10)]
        self.plot.plot(dates, values, color='#00ff00')
        self.plot.set_xlabel('Time', color='#ffffff')
        self.plot.set_ylabel('Events', color='#ffffff')
        self.canvas_figure.draw()
        self.root.after(5000, self.update_time_series)

if __name__ == '__main__':
    root = tk.Tk()
    app = EventFlowAnomalyStudio(root)
    root.mainloop()