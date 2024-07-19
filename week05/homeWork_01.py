class CalculateStackNumber():
    def __init__(self, size_data=2):
        self.top_index = -1
        self.postfix_data = ""
        self.size_data = size_data
        self.stack_data = [None]*size_data

    def push(self, x):
        if self.top_index >= self.size_data-1:
            print("stack overflow")
        else:
            self.top_index += 1
            self.stack_data[self.top_index] = x

    def pop(self):
        if self.top_index == -1:
            print("stack underflow")
        else:
            return_data = self.stack_data[self.top_index]
            self.stack_data[self.top_index] = None
            self.top_index -= 1
            return return_data

    def calculate_postfix(self):
        if self.postfix_data == "":
            print("postfix data is empty")
            return
        print("\npostfix data is", self.postfix_data)
        postfix_data = self.postfix_data.split(",")
        for i in range(len(postfix_data)):
            try:
                postfix_data[i] = float(postfix_data[i])
            except:
                pass
            if i>1:
                if not (type(postfix_data[0]) == float and type(postfix_data[1]) == float):
                    print("input wrong format")
                    return
                elif (i % 2 == 0) and (type(postfix_data[i]) != str):
                    print("input wrong format")
                    return
            if type(postfix_data[i]) == float:
                print("step",i+1,"push",postfix_data[i],"into stack")
                self.push(postfix_data[i])
            elif type(postfix_data[i]) == str:
                operand_2 = self.pop()
                operand_1 = self.pop()
                
                if postfix_data[i] == "+":
                    result = operand_1 + operand_2
                    print("step",i+1,"calculate and push result into stack with :",operand_1,"+",operand_2,"=",result)
                    self.push(result)
                elif postfix_data[i] == "-":
                    result = operand_1 - operand_2
                    print("step",i+1,"calculate and push result into stack with :",operand_1,"-",operand_2,"=",result)
                    self.push(result)
                elif postfix_data[i] == "*":
                    result = operand_1 * operand_2
                    print("step",i+1,"calculate and push result into stack with :",operand_1,"*",operand_2,"=",result)
                    self.push(result)
                elif postfix_data[i] == "/":
                    result = operand_1 / operand_2
                    print("step",i+1,"calculate and push result into stack with :",operand_1,"/",operand_2,"=",result)
                    self.push(result)
                else:
                    print("invalid operator")
                    return
        print("final result is", self.pop())


calStack = CalculateStackNumber()
input_data = input("input postfix data sep with comma \nlike 10,6,+,6,-,2,+ : ")
calStack.postfix_data = input_data
calStack.calculate_postfix()