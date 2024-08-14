# Matplotlib is a data visualization package for python. Below is the code for different types of plot for data
# visualization. In a way we get data explore data, display data in a more comprehensive and readable form for the
# user using plots (graphs), in short graphical representation of the evaluated data

import numpy as np
import matplotlib.pyplot as mtp
from matplotlib import style
import random


def DataVisualization():
    print("!", "*" * 47, "!")
    print("! Data \t \t \t Visualization \t \t \t Formats  !")
    print("!", "*" * 47, "!")


# Scatter Plots (Different Data points plotted as Dots)
def scatter_plots():
    def wc_a():
        X_data = np.random.random(50) * 100
        Y_data = np.random.random(50) * 100
        # print(X_data)
        # print(Y_data)
        mtp.scatter(X_data, Y_data, c="#f0f", marker="+", s=100)
        mtp.show()

    def w_a():
        X_data = np.random.random(1000) * 100
        Y_data = np.random.random(1000) * 100
        # print(X_data)
        # print(Y_data)
        mtp.scatter(X_data, Y_data, c="#f0f", marker="+", s=100, alpha=0.3)
        mtp.show()

    while True:
        print("1. Without Alpha Property  2. With Alpha Property 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wc_a()
        elif select == 2:
            w_a()
        else:
            break


#==============================================================
# Line Plots (Plot data points between two attributes to show connection/interrelation)
def line_plots():
    def wc_d():
        years = [2007 + x for x in range(20)]
        weight = [70, 72, 78, 77, 76, 80, 82, 81, 79, 80,
                  82, 83, 84, 85, 83, 81, 79, 84, 83, 82]
        #supported values for linesyle are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
        mtp.plot(years, weight, c="r", lw=3)
        mtp.show()

    def w_d():
        years = [2007 + x for x in range(20)]
        weight = [70, 72, 78, 77, 76, 80, 82, 81, 79, 80,
                  82, 83, 84, 85, 83, 81, 79, 84, 83, 82]
        mtp.plot(years, weight, "r:", lw=2)  # Linestyle = ":" or "r:"
        mtp.show()

    while True:
        print("1. Without Line Style  2. With Line Style 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wc_d()
        elif select == 2:
            w_d()
        else:
            break


#==============================================================
# Bar Plots (To visualize the data categorically, making polls)
def bar_plots():
    def wc_e():
        x = ["C++", "C#", "Python", "Java", "Go"]
        y = [40, 50, 100, 1, 35]
        mtp.bar(x, y, color="r", align="edge", width=0.1)
        mtp.show()

    def w_e():
        x = ["C++", "C#", "Python", "Java", "Go"]
        y = [40, 50, 100, 1, 35]
        mtp.bar(x, y, color="r", align="edge", width=0.3, edgecolor="blue", lw=6)
        mtp.show()

    while True:
        print("1. Without Edge  2. With Edge 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wc_e()
        elif select == 2:
            w_e()
        else:
            break


#==============================================================
# Histograms (to visualize the data on basis of distribution of quantitative data), to make intervals of the data
def histograms():
    ages = np.random.normal(25, 2.5, 1000)

    def wt_cu():
        mtp.hist(ages, bins=[ages.min(), 18, 21, ages.max()])
        mtp.show()

    def w_c():
        mtp.hist(ages, bins=35, cumulative=True)
        mtp.show()

    while True:
        print("1. Without Cumulative  2. With Cumulative 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wt_cu()
        elif select == 2:
            w_c()
        else:
            break


#===============================================================
# Pie Charts (Visualization of data that is represented independently)
def pie_charts():
    def wc_ex():
        langs = ["Python", "C#", "C++", "Go", "Java", "R-lang"]
        votes = [40, 15, 10, 20, 5, 27]
        mtp.pie(votes, labels=langs)
        mtp.show()

    def w_ex():
        langs = ["Python", "C#", "C++", "Go", "Java", "R-lang"]
        votes = [40, 15, 10, 20, 5, 27]
        explodes = [0.15, 0, 0, 0, 0.5, 0]
        mtp.pie(votes, labels=langs, explode=explodes,
                autopct="%.2f%%", pctdistance=1.3, startangle=90)
        mtp.show()

    while True:
        print("1. Without Explode Property  2. With Explode Property 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wc_ex()
        elif select == 2:
            w_ex()
        else:
            break


#=================================================================
# Box Plots (Data visualization for maximum and minimum values, median of data, statistically providing data etc)
def box_plots():
    def wc_r():
        heights = np.random.normal(172, 8, 300)
        mtp.boxplot(heights)
        mtp.show()

    def w_r():
        first = np.linspace(0, 10, 25)
        second = np.linspace(10, 200, 25)
        third = np.linspace(200, 210, 25)
        fourth = np.linspace(210, 230, 25)
        data = np.concatenate((first, second, third, fourth))
        mtp.boxplot(data)
        mtp.show()

    while True:
        print("1. Without Range  2. With Range 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wc_r()
        elif select == 2:
            w_r()
        else:
            break


#========================================================================
# Plot Customization
def plot_customization():
    def wc_l():
        years = [2014, 2015, 2016, 2017,
                 2018, 2019, 2020, 2021]
        income = [55, 56, 62, 61,
                  72, 72, 73, 75]
        income_ticks = list(range(50, 81, 2))
        mtp.plot(years, income)
        mtp.show()

    def w_l():
        years = [2014, 2015, 2016, 2017,
                 2018, 2019, 2020, 2021]
        income = [55, 56, 62, 61,
                  72, 72, 73, 75]
        income_ticks = list(range(50, 81, 2))
        mtp.plot(years, income)
        mtp.title("Income of Sohaib (in EURO)", fontsize=30, fontname="Times New Roman")
        mtp.xlabel("Years")
        mtp.ylabel("Yearly Income in EURO")
        mtp.yticks(income_ticks, [f"€{x}k" for x in income_ticks])
        mtp.show()

    while True:
        print("1. Without Labels  2. With Labels 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            wc_l()
        elif select == 2:
            w_l()
        else:
            break


#===============================================================================
# Legends and multiple plots
def legends_plots():
    def leg_plot_r():
        stock_a = [100, 102, 99, 101, 101, 100, 102]
        stock_b = [90, 95, 102, 104, 105, 103, 109]
        stock_c = [110, 115, 100, 105, 100, 98, 95]

        mtp.plot(stock_a, label="Tesla")
        mtp.plot(stock_b, label="Microsoft")
        mtp.plot(stock_c, label="Apple")
        # mtp.legend()
        mtp.legend(loc="lower left")
        mtp.show()

    def leg_plot_pie():
        #For pie chart
        votes = [10, 2, 5, 16, 22]
        people = ["A", "B", "C", "D", "E"]
        mtp.pie(votes, labels=None)
        mtp.legend(labels=people)
        mtp.show()

    while True:
        print("1. Legend property use in chart  2. Legend property use in Pie Chart 3. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            leg_plot_r()
        elif select == 2:
            leg_plot_pie()
        else:
            break


#========================================================
# Plot Styling
def plot_styling():
    style.use("dark_background")
    # style.use("grayscale")
    votes = [10, 2, 5, 16, 22]
    people = ["A", "B", "C", "D", "E"]

    mtp.pie(votes, labels=None)
    mtp.legend(labels=people)

    mtp.show()


#==========================================================
# Multiple Figures (Plot different graphs in different windows)
def multiple_figures():
    x1, y1 = np.random.random(100), np.random.random(100)
    x2, y2 = np.arange(100), np.random.random(100)

    mtp.figure(1)
    mtp.scatter(x1, y2)

    mtp.figure(2)
    mtp.plot(x2, y2)

    mtp.show()


#============================================================
# Subplots (Showing different graphs of same values or different values in same window)
def sub_plots():
    x = np.arange(100)

    fig, axs = mtp.subplots(2, 2)

    axs[0, 0].plot(x, np.sin(x))
    axs[0, 0].set_title("Sine Wave")
    axs[0, 0].set_xlabel("Testing")

    axs[0, 1].plot(x, np.cos(x))
    axs[0, 1].set_title("Cosine Wave")

    axs[1, 0].plot(x, np.random.random(100))
    axs[1, 0].set_title("Random Function")

    axs[1, 1].plot(x, np.log(x))
    axs[1, 1].set_title("Log Function")
    fig.suptitle("Four Plots")
    # mtp.show()
    mtp.tight_layout()
    mtp.savefig("FourPlots.png", dpi=300,
                transparent=False, bbox_inches="tight")


#========================================================================
# 3D Plotting
def third_dimension_plotting():
    ax = mtp.axes(projection="3d")

    def scatter_3d():
        x = np.random.random(100)
        y = np.random.random(100)
        z = np.random.random(100)
        ax.scatter(x, y, z)
        ax.set_title("3D Plot")
        ax.set_xlabel("Test")
        ax.set_ylabel("Test1")
        mtp.show()

    def plot_3d():
        x = np.arange(0, 50, 0.1)
        y = np.arange(0, 50, 0.1)
        z = np.sin(x + y)
        ax.plot(x, y, z)
        ax.set_title("3D Plot")
        ax.set_xlabel("Test")
        ax.set_ylabel("Test1")
        mtp.show()

    def three_dimensional_sur():
        #3D Surface Functionality
        x = np.arange(-5, 5, 0.1)
        y = np.arange(-5, 5, 0.1)

        X, Y = np.meshgrid(x, y)
        Z = np.sin(X) * np.cos(Y)

        ax.plot_surface(X, Y, Z)
        ax.plot_surface(X, Y, Z, cmap="Spectral")
        ax.set_title("3D Plot")
        ax.view_init(azim=0, elev=90)
        mtp.show()

    while True:
        print("1. Scatter 3D  2. Plot 3D 3. 3D Surface Property 4. Exit Function")
        select = int(input("Enter Your Choice: "))
        if select == 1:
            scatter_3d()
        elif select == 2:
            plot_3d()
        elif select == 3:
            three_dimensional_sur()
        else:
            break

#==========================================================
# Animating Plots
def animating_plots():
    heads_tails = [0, 0]

    for _ in range(100000):
        heads_tails[random.randint(0, 1)] += 1
        mtp.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
        mtp.pause(0.001)
    #mtp.show()


DataVisualization()
while True:

    print("1. Scatter Plots   2. Line Plots   3. Bar Plots   4. Histograms   "
          "5. Pie Charts   6. Box Plots   7. Plot Customization   8. Legend Plots  "
          "9. Plot Styling \n10. Multiple Figures   11. Sub Plots   12. Third Dimension Plotting   "
          "13. Animations of Plots   14. Exit Program")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        scatter_plots()
    elif choice == 2:
        line_plots()
    elif choice == 3:
        bar_plots()
    elif choice == 4:
        histograms()
    elif choice == 5:
        pie_charts()
    elif choice == 6:
        box_plots()
    elif choice == 7:
        plot_customization()
    elif choice == 8:
        legends_plots()
    elif choice == 9:
        plot_styling()
    elif choice == 10:
        multiple_figures()
    elif choice == 11:
        sub_plots()
    elif choice == 12:
        third_dimension_plotting()
    elif choice == 13:
        animating_plots()
    else:
        exit()
