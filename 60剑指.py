class Solution:
    def dicesProbability(self, n):
        dp = [ [ 0 for _ in range(n*6)] for _ in range(n)]
        for i in range(6):
            dp[0][i] = 1/6

        for i in range(n-1):
            for j in range(i,i*6+6):   #set dp matrix

                tmp_i = 0
                for k in range(6):
                    dp[i+1][j+k+1] += dp[i][j]/6
                print(dp[i])

        print(dp[-1][n-1:])
        return(dp[-1])

if __name__ == '__main__':
    my_solution = Solution()
    n = 2
    print("result is".format(my_solution.dicesProbability(n)))