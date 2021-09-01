def arithmetic_arranger(problem):
  # Ver 1: Explore the logic for the correct display of a single arithmetic
  
  # split the arithmatic based on space
  # there will be the first number, the operator, the second number
  # amount of maximum digit among the first and second number
  # that amount plus two will be the number of "working space"
  # first line: working space minus the length of first number
  # the difference in length is filled with space
  # second line: the beginning of "working space" print the operator
  # "working space" - 1 - length of second number
  # the differnce is filled with space
  # third line: the "-" symbol appears the same amount as "working space" 

    for a in problem:
        a_split = a.split(" ")
        num_1 = a_split[0]; num_2 = a_split[2]
        operator = a_split[1]

        max_length = 0
        for digit in a_split:
            length = len(digit)
            if max_length < length:
                max_length = length

        work_space = max_length + 2

        def first_line():
            empty_space = work_space - len(num_1)
            return " " * empty_space + num_1 + "\n"
        def second_line():
            empty_space = work_space - 1 - len(num_2)
            return operator + " " * empty_space + num_2 + "\n"
        def dash_line():
            return "-" * work_space
        
        print( first_line() + second_line() + dash_line() + "\n" )

  

res = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(res)
