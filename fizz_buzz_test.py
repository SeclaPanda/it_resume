class Answer:
    def fizzbuzztest(self):
        arr = [0] * 100
        for i in range(100):
            arr[i] = i+1
        for i in range(len(arr)):
            if (arr[i] % 3 == 0) and (arr[i] % 5 == 0):
                arr[i] = 'FizzBuzz'
            elif (arr[i] % 3 == 0):
                arr[i] = 'Fizz'
            elif (arr[i] % 5 == 0):
                arr[i] = 'Buzz'
        return arr
print(Answer().fizzbuzztest())    

'''
my time: 0.042991
short solution: 0.047464
long solution: 0.047247

Solution from it resume:
class Answer:
    def fizzbuzztest(self):
      return ["Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n for n in range(1, 101)]

Another version from it resume:
res = []
        for x in range(1, 101):
            s = ''
            if x%3 == 0:
                 s += 'Fizz'
            if x%5 == 0:
                 s += 'Buzz'
            if s == '':
                 s = x
            res.append(s)
        return res
'''