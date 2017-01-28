print("input x: ", end = "")
x = int(input())
print("input n: ", end = "")
n = int(input())

var = 1
y = 9

while 1:
    ans = x - y ** n
    if ans > 0:
        y = y + 9 * (10 ** var)
        var += 1
    else:
        print(y)
        print("go")
        var -= 1
        break

while 1:
        ans = x - y ** n
        if var < 0:
            print("No answer")
            break
        if ans == 0:
            print(y)
            break
        elif ans > 0:
            y = y + 10 ** var
            print(y)
            var -= 1
        elif ans < 0:
            y = y - 10 ** var

        

