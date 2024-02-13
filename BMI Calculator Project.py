#!/usr/bin/env python
# coding: utf-8

# In[ ]:


BMI Calculator Referencing Mercer-Health.com formula
#BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[20]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))


height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if (BMI < 18.5):
        print(name + ", You are Underweight. Eat nutrient-rich foods and consult a professional if underweight. ")
    elif (BMI <= 24.9):
        print(name + ", You are Normal Weight. Stay active and eat well to maintain a normal weight.")
    elif (BMI < 29.9):
        print(name + ", You are Overweight. Prioritize healthy habits for weight management if you are overweight.")
    elif (BMI < 34.9):
        print(name + ", You are Obese. Seek professional guidance for a sustainable plan if you are obese.")
    elif (BMI < 39.9):
        print(name + ", You are Severely Obese. Urgently address severe health risks associated with severe obesity.")
    else:
        print(name + ", You are Morbidly Obese. Immediate medical intervention and lifestyle changes are critical for morbid obesity.")
else:
    print("Enter valid input")


# In[ ]:





# if BMI > 0:
#     if (BMI < 18.5):
#         print(name + ", You are Underweight.")
#     elif (BMI <= 24.9):
#         print(name + ", You are Normal Weight.")
#     elif (BMI < 29.9):
#         print(name + ", You are Overweight.")
#     elif (BMI < 34.9):
#         print(name + ", You are Obese.")
#     elif (BMI < 39.9):
#         print(name + ", You are Severely Obese.")
#     else:
#         print(name + ", You are Morbidly Obese.")
# else:
#     print("Enter valid input")

# In[ ]:





# Under 18.5 -> Underweight - Minimal
# 18.5 - 24.9 -> Normal weight - Minimal
# 25 - 29.9 -> Overweight - Increased
# 30 - 34.9 -> Obese - High
# 35 - 39.9 -> Severely Obese - Very High
# 40 and Over -> Morbidly Obese - Extremely High

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




