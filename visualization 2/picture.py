import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

input = ""

f = open("input1.txt")
line = f.readline()

while line:
    input = input + line
    line = f.readline()

f.close()

input = input.split("Fitting model")
input = input[1:]


dataset = []
for i in range(len(input)):
    raw_in = input[i]
    raw_out = []
    count_0 = raw_in.find("'n_estimators': ")
    count_1 = raw_in.find(",", count_0)
    raw_out.append(raw_in[count_0 + 16: count_1])

    count_0 = raw_in.find(": ", count_1)
    count_1 = raw_in.find("'}", count_0)
    if count_1 == -1:
        count_1 = raw_in.find("}", count_0)
    raw_out.append(raw_in[count_0 + 3: count_1])

    count_0 = raw_in.find(": [", count_1)
    count_1 = raw_in.find("]", count_0)
    raw_out.append(eval(raw_in[count_0 + 3: count_1]))

    dataset.append(raw_out)

y_list = [[], [], [], []]
for i in range(0, len(dataset), 4):
    for j in range(4):
        y_list[j].append(dataset[i + j][2])



plt.title('The Relationship between n_estimators And max_feature in RF')
x_axix = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
label_list = ['auto', 'sqrt', 'log2', 'None']
color_list = ['green', 'red', 'blue', 'orange']
marker_list = ['*', 's', 'p', '^']
for i in range(4):
    plt.plot(x_axix, y_list[i], color = color_list[i], label = label_list[i], marker = marker_list[i], linewidth=2)
plt.legend()
plt.xlabel('n_estimators')
plt.ylabel('computed_metrics')
plt.grid(True, linestyle = "-.", color = "r")

plt.show()
