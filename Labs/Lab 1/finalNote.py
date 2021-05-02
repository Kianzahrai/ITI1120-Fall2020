def compute(hwAver, midterm, final):
  "Compute the average of a student."
  total = hwAverage*25/100 + midterm*25/100 + final*50/100
  return total

hwAverage = float(input('Please enter the average of your hws: '))
midterm = float(input('Please enter your midterm: '))
final = float(input('Please enter the final: '))

total_pts = compute(hwAverage, midterm, final)
print(total_pts)
