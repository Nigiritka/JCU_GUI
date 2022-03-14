import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Plot(FigureCanvas):
    """ Class for creating the Plot """
    def __init__(self, parent):
        self.parent = parent
        # Creating figure and axes
        self.fig, self.ax = plt.subplots(figsize=(5.7, 2.3), tight_layout=True, dpi=100)
        # make a color the same as the background
        self.fig.patch.set_facecolor('#F0F0F0')
        # make data


        self.plot_begin_point = 0
        self.plot_end_point = 20
        self.x = np.linspace(self.plot_begin_point, self.plot_end_point, 100)
        self.y = 3 * np.sin(self.x/3) + 5
        # Make plots a bit more beautiful
        self.ax.set(xlim=(self.plot_begin_point, self.plot_end_point), ylim=(0, 10), xticks=np.arange(self.plot_begin_point, self.plot_end_point+1), yticks=np.arange(0, 11))
        self.ax.set_xlabel("Increment", fontsize=8)
        self.ax.set_ylabel("Angle, [deg]", fontsize=8)
        self.ax.set_title("Joint's Position", fontsize=10)
        self.ax.tick_params(axis='both', which='major', labelsize=6)
        self.ax.grid(True, linestyle=':', linewidth=0.6)
        self.ax.plot(self.x, self.y, linewidth=1.0, label='Sin', color='#03dfd5')
        self.ax.legend(loc=3, fontsize=8)
        super().__init__(self.fig)
        self.setParent(self.parent)
        # self.update_plot()

    def update_plot(self):
        # plot
        self.ax.cla()
        self.x += 1
        self.plot_begin_point += 1
        self.plot_end_point += 1
        self.x = np.linspace(self.plot_begin_point, self.plot_end_point, 100)
        self.y = 3 * np.sin(self.x/3) + 5
        self.ax.set(xlim=(self.plot_begin_point, self.plot_end_point), ylim=(0, 10), xticks=np.arange(self.plot_begin_point, self.plot_end_point+1), yticks=np.arange(0, 11))
        self.ax.set_xlabel("Increment", fontsize=8)
        self.ax.set_ylabel("Angle, [deg]", fontsize=8)
        self.ax.set_title("Joint's Position", fontsize=10)
        self.ax.tick_params(axis='both', which='major', labelsize=6)
        self.ax.grid(True, linestyle=':', linewidth=0.6)
        self.ax.plot(self.x, self.y, linewidth=1.0, label='Sin', color='#03dfd5')
        self.ax.legend(loc=3, fontsize=8)

        self.fig.canvas.draw()
        # self.fig.canvas.draw_idle()
