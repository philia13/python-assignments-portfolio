x= float(input("Enter a number: "))
def math_function(x):
        if 0<=x<=1:
            a= 0
            n= 0
            error_current = 1
            max_error = 0.001

        def error(j,k):
                return j ** ((2*k)+1))/((2*k)+1)
        while:
            max_error < error(x,n)
                term = (((-1) ** n) * (x ** ((2 * n) + 1))) / ((2 * n) + 1)
                a += term
                n += 1

            error_current= error(x,n+1)

            if error_current < max_error:
                break
            return a, n, error_current
        else:
            return "error"

        print(math_function(x))


