number = {'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def rearrange(x):
    x = x.upper()
    n = len(x)
    cur = number[x[0]]
    num = cur
    for i in range(1,n):
        new = number[x[i]]
        if new <= cur:
            num += new
        else:
            num = new - num

    print(num)

x = input()
rearrange(x)