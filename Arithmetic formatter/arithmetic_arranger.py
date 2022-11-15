def arithmetic_arranger(problems, result=False):
 
 row_1 = " "
 row_2 = " "
 lines = " "
 operador = " "
 sumx = " "


 #If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
if len(problems) < 5:
   return print('Error: Too many problems.')


 #placement for rows and operators
for problem in problems:
    row_1 = problem.split()[0]
    operador = problem.split()[1]
    row_2 = problem.split()[2]

#Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
if operador[1] not in "+-":
  return "Error: Operator must be '+' or '-'."
  #Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
if not row_1.isdigit() or row_2.isdigit():
  return "Error: Numbers must only contain digits."
 


 #Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise,
 #the error string returned will be: Error: Numbers cannot be more than four digits.
if len(row_1(problem)) <=5 or len(row_2(problem)) <=5:
  return"Error: Numbers cannot be more than four digits"
 #There should be a single space between the operator and the longest of the two operands,
 # the operator will be on the same line as the second operand, both operands will be in the same order as provided 
  #Numbers should be right-aligned.
 #There should be four spaces between each problem.
  #There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
longest = max(len(row_1)[0], len(row_2)[2])
width = len(longest) +2 
#lines
f"{row_1[0] :>{width}}\nl"
f"{row_2[2] :>{width}}\nl"
f"{operador[1] :>{width}}\nl {'-' * width}"
#.rjust(number) ?
# #for line in [[1, 128, 1298039], [123388, 0, 2]]:
#   print('{:>8} {:>8} {:>8}'.format(*line))

 #(the first will be the top one and the second will be the bottom).
 
  return arranged_problems