class Answer:
    def scoreOfParentheses(self, S):
        stack = [0]

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

S = "((()(()))())"
print(Answer.scoreOfParentheses(Answer, S))