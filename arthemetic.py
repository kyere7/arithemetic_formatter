def arithemtic_arranger(problems, solve = True):
    # Deals with length of problem error
    if len(problems) >5:
        return 'Error: Too many problems.'
    arranged_problems = ''
    for problem in problems:

        #to get each item in each problem
        first_operand = problem.split(' ')[0]
        second_operand = problem.split(' ')[2]
        operation = problem.split(' ')[1]

        # Dealing with errors
        if operation not in '+-':
            return 'Error: Operator must be '+' or '-'.'
        if len(first_operand)>4 or len(second_operand)>4:
            return 'Error: Numbers cannot be more than four digits.'
        try:
            int(first_operand)
            int(second_operand)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        # get longest operand
        longest_value = max(len(first_operand), len(second_operand))
        width = longest_value + 2
        print(width)
        
        # setting space between longest operand and the operator
        first = first_operand.rjust(width)
        second = operation + second_operand.rjust(width-1)
        output = f'''{first}\n{second}\n{'-'*width}'''
        print(output)

        return arranged_problems 
        
            
            
            
       

    



        

