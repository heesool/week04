import argparse

import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True)
parser.add_argument("-o", "--output", required=True)
args = parser.parse_args()

x = []
y = []

with open(args.input, encoding="utf-8") as file:
    for line in file:
        x_value, y_value = map(float, line.split())
        x.append(x_value)
        y.append(y_value)

plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Data")
plt.grid()
plt.savefig(args.output)
