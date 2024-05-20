            
def precedence(s):
    if(s=='^'):
        return 3
    elif(s=='*' or s=='/'):
        return 2
    elif(s=='+' or s=='-'):
        return 1
    else:
        return -1
def associativity(s):
    if(s=='^'):
        return 'R'
    return 'L'
def infix_to_postifx(string):
    result=[]
    stack=[]
    for i in range(len(string)):
        c=string[i]
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            result.append(string[i])
        elif c=='(':
            stack.append(c)
        elif c==')':
            while stack and stack[-1]!='(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and (precedence(c) < precedence(stack[-1]) or (precedence(c) == precedence(stack[-1]) and associativity(c) == 'L')):
                result.append(stack.pop())
            stack.append(c)
    while stack:
        result.append(stack.pop())
    print(''.join(result))
inexp=str(input("Enter the expression: "))
inexp=list(inexp)
print("Infix: ",inexp)
infix_to_postifx(list(inexp))

