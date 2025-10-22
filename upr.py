import statistics
import streamlit as st
import matplotlib.pyplot as plt

grades = [2,6,6,5,5,2,3,4,3,5]
avg = statistics.mean(grades)
favg = statistics.fmean(grades)
median = statistics.median(grades)
lowmedian = statistics.median_low(grades)
highmedian = statistics.median_high(grades)
mode = statistics.mode(grades)

print(f"Mean: {avg}, Precise: {favg}")
print(f"Median: {median}, High: {highmedian}, Low: {lowmedian} ")
print(f"Mode: {mode}")

if(avg >= 5):
    print("Excellent!")
elif(avg >= 4 ):
    print("Good")
else:
    print("Bad!Needs more work!")

grade_counts = {}
for grade in grades:
    grade_counts[grade] = grade_counts.get(grade, 0) + 1

# Plot pie chart
fig, ax = plt.subplots()
ax.pie(grade_counts.values(), labels=grade_counts.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)