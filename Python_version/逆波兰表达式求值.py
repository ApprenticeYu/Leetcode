class Solution:
    def find_value(self,tokens):
        sign_dict = {
        '+':add,
        '-':sub,
        '*':mul,
        '/':lambda x,y:int(x/y),
        }
        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = sign_dict[token](num1,num2)
            finally:
                stack.append(num)
        return stack[0]
