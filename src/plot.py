import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Plot(FigureCanvas):
    """ Class for creating the Plot """
    def __init__(self, parent, x, y):
        self.parent = parent
        # Creating figure and axes
        self.fig, self.ax = plt.subplots(figsize=(5.7, 2.3), tight_layout=True, dpi=100)
        # make a color the same as the background
        self.fig.patch.set_facecolor('#F0F0F0')
        # make data
        self.x = x
        self.y = y
        self.z = 3*np.sin(self.x + np.pi*2/3) + 5
        self.b = 3 * np.sin(self.x + np.pi * 4 / 3) + 5

        # Make plots a bit more beautiful
        self.ax.set(xlim=(0, 10), ylim=(0, 10), xticks=np.arange(0, 20), yticks=np.arange(0, 10))
        self.ax.set_xlabel("Increment", fontsize=8)
        self.ax.set_ylabel("Angle, [deg]", fontsize=8)
        self.ax.set_title("Joint's Position", fontsize=10)
        self.ax.tick_params(axis='both', which='major', labelsize=6)
        self.ax.grid(True, linestyle=':', linewidth=0.6)
        super().__init__(self.fig)
        self.setParent(self.parent)
        self.update_plot()

    def update_plot(self):
        # plot
        self.ax.plot(self.x, self.y, linewidth=1.0, label='Sin', color='#03dfd5')
        self.ax.plot(self.x, self.z, linewidth=1.0, label='Sin+120', color='#ffb90f')
        self.ax.plot(self.x, self.b, linewidth=1.0, label='Sin+240', color='#ff00ff')
        # add legent
        self.ax.legend(loc=1, fontsize=8)
        self.show()
