def solution1(x):
        neg = False
        num = x
        rv = 0
        if x < 0:
            neg = True
            num *= -1
        
        temp = str(num)
        temp = temp[::-1]

        rv = int(temp)
        if neg:
            rv *= -1
        
        if rv > (2 ** 31 - 1) or rv < -(2 ** 31):
            return 0
        else:
            return rv
        
def solution2(x):
    rv = 0
    
    if x < 0:
        rv = int(str(x)[::-1].replace('-','')) * -1
    else:
        rv = int(str(x)[::-1])
    
    if rv > (2 ** 31 - 1) or rv < -(2 ** 31):
        return 0
    else:
        return rv

if __name__ == "__main__":
    print(solution1(1534236469))
    print(solution2(1534236469))