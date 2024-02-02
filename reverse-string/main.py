def reverse_string(n):
    stack=[]
    for ch in n:
          stack.append(ch)
    n=""
    print(stack)
    for ch in range(0,len(stack)):
        n += stack.pop()
    return n
    
string=input()
ans=reverse_string(string)
print(ans)