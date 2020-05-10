# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census=np.concatenate((data,new_record))
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=round(age.mean(),2)
age_std=round(np.std(age),2)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
race=census[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
li=[]
li.append(len_0)
li.append(len_1)
li.append(len_2)
li.append(len_3)
li.append(len_4)
k=min(li)
i=li.index(k)
minority_race=i
senior_citizens=census[age>60]
working_hours=senior_citizens[:,6]
working_hours_sum=sum(working_hours)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(working_hours_sum)
print(round(avg_working_hours,2))

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
k=high[:,7]
k1=low[:,7]
avg_pay_high=round(k.mean(),2)
avg_pay_low=round(k1.mean(),2)
print(avg_pay_high)
print(avg_pay_low)


