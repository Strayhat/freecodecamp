def arithmetic_arranger(problems, result=False):
    # Error: Too many problems.
    if len(problems) > 5:
        return('Error: Too many problems.')

    row_1 = []
    row_2 = []
    line = []
    sums = []
    sum_strs = []
  
    for problem in problems:
        alpha, op, bravo = problem.split(" ")

        #The error returned will be: Error: Operator must be '+' or '-'.
        if op not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        #Each number (operand) should only contain digits. return: Error: Numbers   
        if not (alpha.isdigit() and bravo.isdigit()):
            return "Error: Numbers must only contain digits."

        #has a max of four digits in width. Error: Numbers cannot be more than four   
        if len(alpha) > 4 or len(bravo) > 4:
            return "Error: Numbers cannot be more than four digits."

        #calculating the rows +/- to get sumx
        if op == "+":
            sums.append(int(alpha) + int(bravo))
        else:
            sums.append(int(alpha) - int(bravo))


      
        #calculate the width
        width = max(len(alpha), len(bravo)) + 2

        #building the rows with width,whitespaces and -1 for operator
        if problem != problems[-1]:
            row_1.append(f"{alpha:>{width}}    ")
            row_2.append(f"{op}{bravo:>{width-1}}    ")
            line.append('-' * width + "    ")
            # Store the string representation of the sum
            sum_str = f"{sums[-1]:>{width}}    "
            sum_strs.append(sum_str)
           
        else:
            row_1.append(f"{alpha:>{width}}")
            row_2.append(f"{op}{bravo:>{width-1}}")
            line.append('-' * width)
            sum_str = f"{sums[-1]:>{width}}"
            sum_strs.append(sum_str)
            

    if result:
        output = "".join(row_1)  + "\n" + "".join(row_2) + "\n" + "".join(line) + "\n" + "".join(sum_strs)
    else:
        output = "".join(row_1)  + "\n" + "".join(row_2) + "\n" + "".join(line)
    return output
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))