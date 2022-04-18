class Answer:
    def tuple_creator(arr, n):
        return list(enumerate(arr, start = n))

arr = ['aaa', 125, 'bbb']
n = 3
print(Answer.tuple_creator(arr, n))
