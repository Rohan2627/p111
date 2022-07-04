import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv


df = pd.read_csv("studentScore.csv")

data = df["Math_score"].tolist()

graph =  ff.create_distplot([data], ["Math score"],  show_hist = False)

# graph.show()

meanOfP = st.mean(data)

stdevOfP = st.stdev(data)

print("--------------------------")
print("Mean of population : " , meanOfP)
print("Stdev of population : " , stdevOfP)


# --------------------------------------------------------------------

sampleMeanList = []

# sampleMeanList[ [mean of 100 random data SET 1] , [mean of 100 random data SET 2] , [mean of 100 random data SET 3] , .... , [mean of 100 random data SET 1000] ]

for i in range(1000):
    tempList = []
    for j in range(100):
        tempList.append(random.choice(data))
    
    sampleMeanList.append(st.mean(tempList))
        

meanOfS = st.mean(sampleMeanList)

stdevOfS = st.stdev(sampleMeanList)

print("------------------------------")
print("Mean of sample Data : " , meanOfS)
print("Stdev of Sample : " , stdevOfS)


# --------------------------------- exra classes ------------------------------------
df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()

meanOfS1 =  st.mean(data1)


# ---------------------------------- funsheets  -----------------------------------------

df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()

meanOfS2 =  st.mean(data2)



# ------------------------------------who got iPad ----------------------------------------

df3 = pd.read_csv("data3.csv")
data3 = df["Math_score"].tolist()

meanOfS3 =  st.mean(data3)



print("------------------------------")
print("Mean of sample Data 1 : " , meanOfS1)

print("------------------------------")
print("Mean of sample Data 2 : " , meanOfS2)

print("------------------------------")
print("Mean of sample Data  3 : " , meanOfS3)















