from flask import Flask, request
app = Flask(__name__)

#Fibonacci function
def fibo(n: int):
    l=[]
    a = 0
    b = 1
    """
    Calculating the fibonacci numbers
    """
    if n < 1:
        return 'Only numbers > 0 are accepted'
    elif n == 1:
        return a
    else:
        l.append(a)
        l.append(b)

        for i in range (2, n):
            c = a + b
            a = b
            b = c
            l.append(c)
        return(l)

#route
@app.route("/")
def send_fibo():
    """
    Sending the fibonacci list to the user or if
    user uses improper input
    """
    try:
        return str(fibo(int(request.args['n'])))
    except ValueError:
        return "Please use a number"

if __name__ == '__main__':
    app.run()
