class Solution:
    def print_num(self,a,num):
        a+=1
        num.append('1')
        return
    def sumNums(self, n):
        num = [0] * n
        res = []
        a = 0
        res = self.print_num(a,num)
        print(num)
        print(a)
        print(res)

        return res

if __name__ == '__main__':
    my_solution = Solution()
    n = 1
    print(my_solution.sumNums(n))