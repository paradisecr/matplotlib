#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


def single_list():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()

def x_y():
    plt.plot([1,2,3,4], [1,4,9,16]) # x_list y_list
    plt.show()

def x_y_color():
    '''
        Third arg use format string that indicate the color and line type of the plot.
        The letters and symbols of the format string are from MATLAB
    '''
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # ro:red & circle, default is
    plt.axis([0, 6, 0, 20]) # The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
    plt.show()

def numpy():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()

if __name__ == '__main__':
    # single_list()
    # x_y()
    x_y_color()
    numpy()
    pass
