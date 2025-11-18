

''' LOOPS QUESTIONS : '''
'''5. ) A company is organizing a large-scale project and assigning teams sequential numbers (1, 2, 3, ... n). However, due to resource constraints, only even-numbered teams receive funding.
Each even-numbered team gets a budget equal to (team number × ₹100). The finance department wants to automate the calculation of the total allocated budget for all even-numbered teams up to n.
'''

n= int(input('enter no. of teams in a company: '))
total_budget = 0
for team_number in range(1, n+1):
  if(team_number % 2 == 0) :
    total_budget += (team_number * 100)

print(total_budget)
