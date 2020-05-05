import requests

res = requests.get('http://localhost:5000/?n=5')
if res:
    print('Response OK')
    if (res.text == '[0, 1, 1, 2, 3]'):
        print("Passed, Test: input = 5 and 1st 5 numbers in the fibonacci sequence is " + res.text)
    else:
        print("Failed " + res.text)
else:
    print('Response Failed')
