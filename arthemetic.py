def arithmetic_arranger(problems, args=True):
  # Deals with length of problem error
    if len(problems) >5:
        return 'Error: Too many problems.'
    arranged_problems = []
    for problem in problems:

      #to get each item in each problem
      first_operand = problem.split(' ')[0]
      second_operand = problem.split(' ')[2]
      operation = problem.split(' ')[1]
      # Dealing with errors
      if operation not in '+-':
          return "Error: Operator must be '+' or '-'."
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
      #print(width)
        
      # padding
      first =first_operand.rjust(width)
      second = operation + second_operand.rjust(width-1)
      d = '-'*width
      #solution = str(int(first_operand)+int(second_operand)).rjust(width)
      
      try:
          arranged_problems[0] += (' '*4) + first
      except IndexError:
          arranged_problems.append(first)
      try:
          arranged_problems[1] += (' '*4) + second
      except IndexError:
          arranged_problems.append(second)
      try:
          arranged_problems[2] += (' '*4) +d
      except IndexError:
          arranged_problems.append(d)
        
      if args:
        if operation == '+':
          solution = str(int(first_operand)+int(second_operand)).rjust(width)
        else:
          solution = str(int(first_operand)-int(second_operand)).rjust(width)
        try:
            arranged_problems[3] += (' '*4) + solution
        except IndexError:
            arranged_problems.append(solution)
      resulting = f'''{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}'''
      if args:
        resulting = resulting + f'''\n{arranged_problems[3]}'''
      else:
        resulting
      
    return resulting 

#print(arithmetic_arranger(''' enter problems here '''))