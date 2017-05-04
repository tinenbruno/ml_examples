import csv
import math

def euclideanDistance(x, y):
  distance = 0
  for i in range(len(x)):
    distance += math.pow(x[i] - y[i], 2)
  return distance

training_dataset = []
training_labels = []

test_dataset = []
test_labels = []

# Populate training and test sets
with open('iris_training.csv', 'rU') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', dialect=csv.excel_tab)
  for row in spamreader:
    training_dataset.append([ float(row[3]), float(row[2]), float(row[1]), float(row[0]) ])
    training_labels.append(row[4])

with open('iris_test.csv', 'rU') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', dialect=csv.excel_tab)
  for row in spamreader:
    test_dataset.append([ float(row[3]), float(row[2]), float(row[1]), float(row[0]) ])
    test_labels.append(row[4])


print('1 NN Label Actual Label')

# Classify and compare with actual label
for i in range(len(test_dataset)):
  test_instance = test_dataset[i]
  distances = []
  for j in range(len(training_dataset)):
    distances.append(euclideanDistance(test_instance, training_dataset[j]))

  print(training_labels[distances.index(min(distances))], test_labels[i])