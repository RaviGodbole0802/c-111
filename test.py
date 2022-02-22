from multiprocessing.sharedctypes import Value
import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as go
from scipy import rand 

df = pd.read_csv("math_scores.csv")

data = df["Math_score"].tolist()
print(data)


def random_set_of_mean (counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return(mean)


# Pass the number of time you want the mean of the data 
# points as a parameter in range function in for loop

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)


# calculating mean and standard_deviation of the sampling distribution

std_deviation=statistics.stdev(mean_list)

mean=statistics.mean(mean_list)
print("Mean of sampling distrubution ==> "+ str(mean))
        
# plotting the mean of the sampling

# fig = ff.create_distplot([mean_list],["Math_score"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
# fig.show()

# findig the standard deviation starting and ending values

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2 *std_deviation),mean+(2 *std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3 *std_deviation),mean+(3 *std_deviation)
print("STD1",first_std_deviation_start,first_std_deviation_end)
print("STD2",second_std_deviation_start,second_std_deviation_end)
print("STD3",third_std_deviation_start,third_std_deviation_end)

# plotting the graph with traces
fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

