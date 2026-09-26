import numpy as np

marks=np.array([75,82,68,90,55,73,88,61,79,95])

mean=np.mean(marks)
median=np.median(marks)
standard_deviation=np.std(marks)
maximum=np.max(marks)
minimum=np.min(marks)

print("Internal Marks: ",marks)
print("Mean: ",mean)
print("Median: ",median)
print("Standard Deviation: ",standard_deviation)
print("Maximum: ",maximum)
print("Minimum: ",minimum)
