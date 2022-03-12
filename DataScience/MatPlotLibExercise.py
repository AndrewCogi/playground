# MatplotLib Coding Exercise
import numpy as np
import matplotlib.pyplot as plt

# create a wt array with 100 random float numbers between 40.0 and 90.0
wt=np.round(np.random.uniform(40,90,100),1)

# create a ht array with 100 random integer numbers between 140 and 200
ht=np.array(np.random.randint(140,201,100))

# compute the BMI for the 100 students, store them in a bmi array
bmi=wt/((ht/100)*(ht/100))

# to prevent data loss, use round([bmi_data],1)
bmi=np.round(bmi,1)


# Bar chart
bmi_level=['Underweight','Healthy','Overweight','Obese']
students=[0,0,0,0]

for student_bmi in bmi:
    if student_bmi < 18.5:
        students[0] += 1
    elif 18.5 <= student_bmi <= 24.9:
        students[1] += 1
    elif 25.0 <= student_bmi <= 29.9:
        students[2] += 1
    elif 30.0 <= student_bmi:
        students[3] += 1

plt.bar(bmi_level, students)
plt.show()


# Histogram
plt.hist(bmi, bins = [bmi.min(), 18.5, 25.0, 30.0, bmi.max()])
plt.title("histogram of result")
plt.xticks([bmi.min(), 18.5, 25.0, 30.0, bmi.max()])
plt.xlabel('BMI')
plt.ylabel('number of students')
plt.show()


# Pie chart
bmi_level=['Underweight','Healthy','Overweight','Obese']
students=[0,0,0,0]

for student_bmi in bmi:
    if student_bmi < 18.5:
        students[0] += 1
    elif 18.5 <= student_bmi <= 24.9:
        students[1] += 1
    elif 25.0 <= student_bmi <= 29.9:
        students[2] += 1
    elif 30.0 <= student_bmi:
        students[3] += 1

plt.pie(students, labels=bmi_level, autopct='%1.2f%%')
plt.show()


# Scatter plot
plt.scatter(wt, ht, color='b')
plt.xlabel('weight(kg)')
plt.ylabel('height(cm)')
plt.show()
