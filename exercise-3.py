# exercise-03 Calculate Dog Years

dog_h_age = int(input("Input a dog's age in human years:"))
if dog_h_age < 3:
    dog_age =(dog_h_age-1)*10 + 10
else:
    dog_age = dog_age =(dog_h_age-2)*7 + 20
print(f"The dog's age in dog years is {dog_age}")