import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["math scores"],show_hist = False)
fig.show()
mean  = statistics.mean(data) 
std_deviation = statistics.stdev(data)
print("mean of population",mean)
print("deviation of population",std_deviation)


def random_set_of_mean(counter):
  dataset = []
  for i in range(0, counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

    mean_list = []
    for i in range(0,1000):
      set_of_means = random_set_of_mean(100)
      mean_list.append(set_of_means)


      std_deviation = statistics.stdev(mean_list)

first_std_deviation_start,first_std_deviation_end = mean -std_deviation, mean +std_deviation
second_std_deviation_start,second_std_deviation_end = mean -(2*std_deviation), mean +(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean -(3*std_deviation), mean +(3*std_deviation)

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:-"mean_of_sample_3)
fig = ff.create_distplot([mean_list], ["Student marks"], show_hist = False)
fig.add_trace(go.Scatter(x =[mean,mean], y = [0,0.17], mode = "lines" ,name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample_3,mean_of_sample_3], y = [0,0.17], mode =  "stodent who go fullsheets"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17], mode =  "standard derivation 1"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17], mode =  "standard derivation 2"))
fig.show()

