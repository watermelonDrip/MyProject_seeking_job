class Solution:
    def permutation(self, s):
        res = []
        print(len(s))
        def backtrack(num):
            if len(stack) == len(s):
                tmp = ''.join(stack[:])
                #if tmp in res:
                 #    return
                res.append(''.join(stack[:]))
                return
            for i in range(len(s)):
                #if s[i] in stack:
                #    continue
                if i>0 and s[i] == s[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    used[i] = 1
                    stack.append(s[i])
                    backtrack( s[1:])
                    stack.pop(-1)
                    used[i] = 0
        used = [0] * len(s)
        res = []
        stack = []
        backtrack(s)
        print(res)
if __name__ == '__main__':
    my_solution = Solution()
    s = "ss"
    my_solution.permutation(s)
    print("result is".format(my_solution.permutation(s)))
