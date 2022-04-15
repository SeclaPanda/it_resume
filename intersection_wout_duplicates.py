class Answer:
    def PureIntersection(self, arr1, arr2):
        # введите свой код ниже
        res = []
        for i in range (len(arr1)):
            for j in range (len(arr2)):
                if arr1[i] == arr2[j]:
                    res.append(arr1[i])    
        result = []
        for i in range(len(res)):
            for j in range(len(res)):
                if res[i] == res[j]:
                    if res[i] in result:
                        continue
                    else:
                        result.append(res[i])
        return result

arr1 = [1, 2, 3]
arr2 = [1, 1, 5]
print(Answer().PureIntersection(arr1, arr2))