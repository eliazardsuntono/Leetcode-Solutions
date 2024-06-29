def solution(a, b):
        la = [int(i) for i in a]
        lb = [int(i) for i in b]

        ind_a = len(la) - 1
        ind_b = len(lb) - 1
        base_a = 0
        base_b = 0

        for i in range(len(la)):
            val = la[i] * (2 ** ind_a)
            base_a += val
            ind_a -= 1
        for i in range(len(lb)):
            val = lb[i] * (2 ** ind_b)
            base_b += val
            ind_b -= 1  


        num = base_a + base_b

        rv = bin(num).replace("0b", "")
        return str(rv)
        
if __name__ == "__main__":
    print(solution("11", "1"))