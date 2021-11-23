# * Loop

height = input(
    'What are the height of the student that you wanna to calculate ? :').split()


for i in range(0, len(height)):
    height[i] = int(height[i])
sum = 0
for n in height:
    sum = sum + n

average = sum/len(height)
rounded_avg = round(average)

print(f'The average height is {rounded_avg}')
