def solution(digits):
        exp = len(digits) - 1
        num = 0
        for i in range(len(digits)):
            dig = digits[i] * (10 ** exp)
            exp -= 1
            num += dig
        
        num += 1
        rv = [int(i) for i in str(num)]
        
        return rv

if __name__ == '__main__':
    digits = [1,2,3]
    print(solution(digits))