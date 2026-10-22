#How we built the algorithm for the function, normally this will go away
numbers = [5,2,3,10]
total = sum(numbers)
count = len(numbers)
print(total)
print(count)

average = total / count
print(average)

#And gets replaced with the function below
def average(numbers: list) -> float:
    '''
    This function takes a list of numbers and returns the average of those numbers.
    '''
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

grades = [100,100,100,0]
result = average(grades)
print(result)

average