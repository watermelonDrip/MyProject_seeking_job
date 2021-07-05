class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        vis = [0 for _ in range(len(word))]
        word = list(word)
        path = []
        self.res = 0
        res1 = []

        def backtrack(word, size, vis, start, dict_res):
            if len(path) != size:
                print(path)
                t_num = 0
                res1.append(path[:])
                for key, value in dict_res.items():
                    if value % 2:
                        t_num += 1
                    if t_num > 1:
                        return
                self.res += 1
                return res1
            for i in range(start, len(word)):

                if vis[i] == 1:
                    continue
                #if i > 0 and  not vis[i - 1] and size >1:
                 #   continue
                if i>0 and word[i-1] == word[i] and vis[i-1]== 0:
                    continue
                vis[i] = 1
                print('start',start)

                print(vis)
                #dict_res[word[i]] = dict_res.get(word[i], 0) + 1
                # print(dict_res)
                path.append(word[i])
                #print(path)
                backtrack(word, size, vis, start+1, dict_res)
                path.pop(-1)
                vis[i] = 0
               # dict_res[word[i]] = dict_res.get(word[i], 0) - 1

        #for size in range( len(word) + 1):
        backtrack(word, 4, vis, 0, {})
        #print(res1)

        return self.res
if __name__ == '__main__':
    my_solution = Solution()
    word = "abcd"

    print(my_solution.wonderfulSubstrings(word))