from django.shortcuts import render
import pandas as pd
import datetime 
import pandas_datareader as pdr
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot, dates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def dollars(x, pos):
    return("${:,.2f}".format(x*1))
def twodec(x, pos):
    return("{:,.2f}".format(x*1))

formatter = FuncFormatter(dollars)
formatdec = FuncFormatter(twodec)

koch1 = ['401k (GP) 4/25/17']
koch2 = ['N/A'] #price / share
kochpos = 1498.75
koch3 = ["{:,.2f}".format(kochpos)]
kochcost = 1498.75
koch4 = "{:,.2f}".format(kochcost) #cost/basis
kochgain = kochpos - kochcost
koch5 = ["{:,.2f}".format(kochgain)] #gain/loss

csv_file = 'stocks.csv'
colnames = ['Ticker', 'Shares', 'Cash', 'Commission', 'Cost']
data = pd.read_csv(csv_file, names=colnames, header=0)
tickerlist = data.Ticker.tolist()
shareslist = data.Shares.tolist()
cashlist = data.Cash.tolist()
commlist = data.Commission.tolist()
costlist = data.Cost.tolist()

a = datetime.datetime.now().date() #todays date
b = 25 #number of days for range of table
c = a - datetime.timedelta(days=b) #collect range of days

d = [pdr.get_data_yahoo(symbols=i, start=c, end=a) for i in tickerlist] #get historical data from tickers
e = [(i['Adj Close']) for i in d] #parse out the adjusted close price from the historical data
f = [e[i] * shareslist[i] - commlist[i] + cashlist[i] for i in range(len(tickerlist))] #calculate the position from the stocks.csv file
g = sum(f) #sum all of the holdings

xaxis = [kochpos + g[i] for i in range(len(g))] #add in the 401k that is not included in the stocks.csv file
yaxis = list(range(len(xaxis))) #create a list of the range of the number of elements (0, 1, 2, 3...)
pyplot.xlabel('Day')
pyplot.plot(yaxis,xaxis) #plots data on axes
ax = plt.gca() #calls current axis
ax.grid(True)
ax.yaxis.set_major_formatter(formatter) #formats y-axis to $ and commas
pyplot.tight_layout() #creates padding on figure
pyplot.savefig('personal/static/personal/img/port.png') #saves figure

h = a - datetime.timedelta(days=1) #get yesterdays date
j = [pdr.get_data_yahoo(symbols=i, start=h, end=h) for i in tickerlist]

k = [(i['Adj Close']) for i in j]
k1 = [float(i) for i in k]
k2 = [formatdec(i) for i in k1]
k3 = k2 + koch2

l = [k[i] * shareslist[i] - commlist[i] + cashlist[i] for i in range(len(tickerlist))] #calculate the position from the stocks.csv file
l1 = [float(i) for i in l]
l2 = [formatdec(i) for i in l1]
l3 = l2 + koch3

m = [l[i] - costlist[i] for i in range(len(l))]
m1 = [float(i) for i in m]
m2 = [formatdec(i) for i in m1]
m3 = m2 + koch5

n = sum(l1) + kochpos
n1 = formatdec(n)

o = sum(m1) + kochgain
o1 = formatdec(o)

headers = ['Ticker', 'Price', 'Market Value', 'Gain/ Loss ($)']
col0 = tickerlist + koch1 #tickers
col1 = k3 #price / share
col2 = l3 #Market Value
col3 = m3 #Gain/Loss

totalvalue = n1
totalgain = o1

p = col0 + col1 + col2 + col3
q = list(chunk(p, 4))

r = [int(i) for i in range(len(q))]

def portlist():
	for i in r:
		s = r[i]
		t = [el[i] for el in q]
		yield(t)
u = portlist()
v = list(u) #list of lists containing n lists of rows
w = [['Total', '-', totalvalue, totalgain]]
x = v + w


def forecasttable(request):
	return render(request, 'personal/forecast.html', {'headers':headers, 'data':x})

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me at:','rfgranzow@gmail.com']})

def CV(request):
	return render(request, 'personal/cv.html')

def VBA(request):
	return render(request, 'personal/VBA.html')

def LaTeX(request):
	return render(request, 'personal/LaTeX.html')

def Pytuts(request):
	return render(request, 'personal/Pytuts.html')

def django(request):
	return render(request, 'personal/django.html')

def extra(request):
	return render(request, 'personal/extra.html')

def safety(request):
	return render(request, 'personal/safety.html')


def forecast(request):
	return render(request, 'personal/forecast.html')


