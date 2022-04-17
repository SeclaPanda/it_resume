class Answer:
    def kidsWithCandies(candies, extraCandies):
        m = max(candies)
        return [candie + extraCandies >= m for candie in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(Answer.kidsWithCandies(candies, extraCandies))

'''
Unfortunately i forget about 'max' func in python,
so i check answer on it-resume 
'''