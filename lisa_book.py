class Answer:
    def CountSpecialProblems(self, n, k, arr):
        page = 1
        count = 0
        for a in arr:
            for i in range(1, a+1):
                if i == page: count += 1
                if i%k==0: page += 1
            if a%k != 0: page += 1        
        return count
arr = [4, 2]
print(Answer().CountSpecialProblems(2, 3, arr))

'''
Answer from IT_resume
for a in arr:
    i = 1
    while i <= a:
        if i == page: count += 1
        if i%k==0: page += 1
        i += 1
    if a%k != 0: page += 1
'''