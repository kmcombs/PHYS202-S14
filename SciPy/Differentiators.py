
import numpy as np

def twoPtForwardDiff(x,y):
    """Input an array of x values and and y(x) equation"""
    """returns the forward derivative between two points"""
    dydx = np.zeros(y.shape, float)
    dydx[0:-1] = (y[1:] - y[0:-1])/(x[1:] - x[0:-1])
    dydx[-1] = (y[-2] - y[-1])/(x[-2] - x[-1])
    return dydx

def twoPtCenteredDiff(x,y):
    """Input an array of x values and and y(x) equation"""
    """returns the derivative at a center point using the points in front and in back"""
    dydx1 = np.zeros(y.shape, float)
    dydx1[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx1[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx1[-1] = (y[-2] - y[-1])/(x[-2] - x[-1])
    return dydx1

def fourPtCenteredDiff(x,y, spacing):
    """Input and array of x values, the equation y(x), and the spacing between the x values"""
    """Returns the Four Point Center Derivative at these points"""
    dydx = np.zeros(y.shape, float)
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[1] = (y[2] - y[1])/(x[2] - x[1])
    dydx[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*spacing)
    dydx[-2] = (y[-3] - y[-2])/(x[-3] - x[-2])
    dydx[-1] = (y[-2] - y[-1])/(x[-2] - x[-1])
    return dydx