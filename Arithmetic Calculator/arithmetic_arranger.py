def arithmetic_arranger(problems,trigger=False): #Optional argument trigger defaults to False
    ##Information
    #arithmetic_arranger is a function that puts horizontal equations into vertical form
    #Limit of 5 problems
    #Only addition and subtraction operators only
    #Each number must only contain digits
    #Each Number must only contain four digits at max
    #integers only
    #trigger = true means the problems should be solved when returned
    #trigger != true means the problems will comeback unsolved
    #Example call: arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    ##Error calls
    #If longer than 5 problems, will put out an error
    if len(problems) > 5: #if length of problems is more than 5
        print('Error: Too many problems.')
        return
    #Addition and subtraction operators
    #Numbers are numbers with only 4 digits max
    #Numbers must only contain digts
    for i in range(0,len(problems)):
        conditionMinus = '-' in problems[i] #is there a minus sign?
        conditionPlus = '+' in problems[i] #is there a plus sign?
        if conditionMinus == conditionPlus: #if there's both a plus and a minus or not a minus or plus sign
            print('Error: Operator must be "+" or "-".')
            return
        problem = problems[i].split()
        for k in range(0,2,2): #For first and third terms, the numbers
            if len(problem[k]) > 4: #If numbers are longer than 4 digits
                print('Error: Numbers cannot be more than four digits.')
                return
            try: #try converting number to integer
                int(problem[k])
            except: #if cannot be converted into integer
                print('Error: Numbers must only contain digits.')
                return
    ##Function
       for i in range(0,len(problems)): #goes through each problem one at a time
           problem = problems[i].split() #creates a list of all the terms of the problem
           max_length = len(max(problem, key = len)) #gets max lengt of number, used for number of dashes at bottom
           dashes = max_length+2 #amount of dashes under the equation
           

    return arranged_problems
