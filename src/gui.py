from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

fig = Figure(figsize = (5, 5), dpi = 100)

def display_graph(fig):
    # Initializing the FigureCanvasTkAgg Class Object.
    canvas = FigureCanvasTkAgg(fig, master=window)
    # Getting the Figure canvas as a tkinter widget.
    tk_canvas = canvas.get_tk_widget().pack()
    # tk_canvas.pack(fill=BOTH, side=RIGHT)  # Packing it into it's master window.
    canvas.draw()  # Drawing the canvas onto the screen.

# plot function is created for
# plotting the graph in
# tkinter window


def plot():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    # list of squares
    y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)
    plot2 = fig.add_subplot(111)

    display_graph(fig)

    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    # list of squares
    y = [i for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)
    plot2 = fig.add_subplot(111)

    display_graph(fig)
    display_graph(fig)

    # # creating the Tkinter canvas
    # # containing the Matplotlib figure
    # canvas = FigureCanvasTkAgg(fig,
    #                            master = window)
    # canvas.draw()

    # # placing the canvas on the Tkinter window
    # canvas.get_tk_widget().pack()

    # # creating the Matplotlib toolbar
    # toolbar = NavigationToolbar2Tk(canvas,
    #                                window)
    # toolbar.update()

    # # placing the toolbar on the Tkinter window
    # canvas.get_tk_widget().pack()
# the main Tkinter window
window = Tk()
# setting the title
window.title('Plotting in Tkinter')
window.state("zoomed")
# window.attributes('-fullscreen', True)


# button that displays the plot
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui


window.mainloop()
