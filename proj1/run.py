def arithmetic_arranger(problems):

 #dictornary 
 row_1 = ''
 row_2 = ''
 lines = ''
 operador = ''
 sumx = ''


 #If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
if len(problems) < 5:
    return ('Error: Too many problems.')



for problem in problems:
    row_1 = problem.split()[0]
    operador = problem.split()[1]
    row_2 = problem.split()[2]

#Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
if operador[1] not in "+-":
  return "Error: Operator must be '+' or '-'."
  #Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
if not row_1.isdigit() or not row_2.isdigit():
  return "Error: Numbers must only contain digits."
 


 #Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise,
 #the error string returned will be: Error: Numbers cannot be more than four digits.
if len(row_1(problem)) <=5 or len(row_2(problem)) <=5:
  return('Error: Numbers cannot be more than four digits')


    return arranged_problems