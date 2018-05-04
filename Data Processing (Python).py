# Author: Anshul Verma

# Data Processing 

# EM624 - Exercise 05

# to import matplotlib
import matplotlib.pyplot as plt

# to define function for returning index to update counts
def get_index(parts):
    
    lower = [1, 2, 3]
    middle = [4, 5, 6]
    upper = [7, 8, 9]

    for i in parts:
    
        if float(i[1]) == 1 and float(i[0]) in lower:
            yield 0
    
        if float(i[1]) == 2 and float(i[0]) in lower:
            yield 1
            
        if float(i[1]) == 1 and float(i[0]) in middle:
            yield 2 
    
        if float(i[1]) == 2 and float(i[0]) in middle:
            yield 3
            
        if float(i[1]) == 1 and float(i[0]) in upper:
            yield 4
    
        if float(i[1]) == 2 and float(i[0]) in upper:
            yield 5

# to create a list of counts 
counts = [0, 0, 0, 0, 0, 0]

# to open file 'marketingdata.txt'
file = open("marketingdata.txt","r")

# to create a list of parts from the file, for input to the function
parts = []
for line in file:
    if "NA" in line:
        continue
    data = line.strip().split()
    parts.append(data)

print parts
# to call the function for getting appropriate index            
index = get_index(parts)

# to update the list of counts 
for i in index:
    counts[i] += 1

# to print the results
print "\nWho is at the mall?"
print "Lower Income Men: ", counts[0]
print "Lower Income Women: ", counts[1]
print "Middle Income Men: ", counts[2]
print "Middle Income Women: ", counts[3]
print "Upper Income Men: ", counts[4]
print "Upper Income Women: ", counts[5]

# to be used in charts
x = [0, 1, 2, 3, 4, 5]
names = ["Lower Income Men", "Lower Income Women", "Middle Income Men", "Middle Income Women", "Upper Income Men", "Upper Income Women"]
colors = ['lightblue', 'pink', 'lightblue', 'pink', 'lightblue', 'pink']
explode = (0.1, 0, 0.1, 0, 0.1, 0)

# to create bar chart
plt.subplot(2, 2, 1)
plt.bar(x, counts, color=colors)
plt.xticks(x, names, rotation='vertical')
plt.ylabel("Count of People")

# to create pie chart
plt.subplot(2, 2, 2)
plt.pie(counts, explode=explode, labels=names, colors=colors, autopct='%1.0f%%')

# to assign title and display the charts
plt.suptitle("Count of People at the Mall, by Income and Gender")
plt.show()