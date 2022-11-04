from input import inpt

inpt = inpt.splitlines()

data = []

for i in inpt:
  data.append(int(i))

result = 0

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] == 2020:
            result = data[i] * data[j]
            break

print(result)