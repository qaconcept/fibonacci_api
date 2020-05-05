# fibonacci_api
fibonacci restful api (user inputs number for range and fibonacci list is displayed)

Setup (mac)
1. Install Python 3.8.2 (install pip is not included) https://www.python.org/downloads/
2. open Terminal on Mac and navigate to python directory
3. install Flask using command 'pip install Flask'
4. clone github repository https://github.com/qaconcept/fibonacci_api.git
5. in terminal navigate to python directory and enter 'python3 fib_api.py' and press enter to run
    -this will start a local host http://localhost:5000/
6. in a web browser on the same machine, enter url and fibonacci range number ex:http://localhost:5000/?n=5
    -?n is our range number
    -our example ex:http://localhost:5000/?n=5 will return list [0, 1, 1, 2, 3]

note: anything other than an int, negative numbers will return error.


