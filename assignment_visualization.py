#!/usr/bin/env python3
"""
NTU Assignment - Data Visualisation (Matplotlib + Seaborn)

Questions:
1) Create a 2x2 subplot grid and select first subplot
2) Plot a red dashed line
3) Plot a histogram with 30 bins
4) Set x and y axis labels
5) Seaborn barplot: average tip per day (tips dataset)
6) Seaborn boxplot: total_bill by day (tips dataset)
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Question 1
def q1_subplots_first_ax():
    fig, axes = plt.subplots(2, 2)  # 2x2 grid
    ax = axes[0, 0]                 # first subplot (top-left)
    return fig, axes, ax


# Question 2
def q2_red_dashed_line():
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    plt.figure()
    plt.plot(x, y, color="red", linestyle="--")
    plt.title("Red Dashed Line Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()


# Question 3
def q3_hist_30_bins():
    data = np.random.randn(1000)

    plt.figure()
    plt.hist(data, bins=30)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of data")
    plt.tight_layout()
    plt.show()


# Question 4
def q4_set_axis_labels():
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.xlabel("X axis label")
    plt.ylabel("Y axis label")
    plt.title("Example Plot")
    plt.tight_layout()
    plt.show()


# Question 5
def q5_seaborn_barplot_avg_tip_per_day():
    tips = sns.load_dataset("tips")

    plt.figure()
    sns.barplot(data=tips, x="day", y="tip")  # default estimator is mean
    plt.xlabel("Day")
    plt.ylabel("Average Tip")
    plt.title("Average Tip Amount per Day")
    plt.tight_layout()
    plt.show()


# Question 6
def q6_seaborn_boxplot_total_bill_by_day():
    tips = sns.load_dataset("tips")

    plt.figure()
    sns.boxplot(data=tips, x="day", y="total_bill")
    plt.xlabel("Day")
    plt.ylabel("Total Bill")
    plt.title("Total Bill by Day")
    plt.tight_layout()
    plt.show()


def main():
    # Q1 returns objects, does not show plot automatically
    fig, axes, ax = q1_subplots_first_ax()
    ax.set_title("Q1: First subplot (0,0)")
    fig.suptitle("Q1: 2x2 Subplots")
    fig.tight_layout()
    plt.show()

    # Q2-Q6 show plots
    q2_red_dashed_line()
    q3_hist_30_bins()
    q4_set_axis_labels()
    q5_seaborn_barplot_avg_tip_per_day()
    q6_seaborn_boxplot_total_bill_by_day()


if __name__ == "__main__":
    main()
