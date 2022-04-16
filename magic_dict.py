class Answer:
    def magic_dict(self, str):
        k = list(str)
        dict1 = {}
        for char in k:
            cnt = 0
            for item in k:
                if char == item:
                    cnt=cnt+1
            dict1[char] = cnt
        return dict1
        
str = 'abcacdabcacdaaeee'
print(Answer.magic_dict(str))