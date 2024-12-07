
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class TriNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.middle = None
        self.left = None 

class solver1:
    def __init__(self, input_lists):
        self.input = input_lists

    def bfs(self, result, l):
        height = len(l)
        root = TreeNode(l[0])
        q = []
        q.append((root, 0))
        while q:
            current, level = q.pop()

            if level == height - 1 and current.val == result:
                return True


            if level + 1 < height:
                level += 1
                current.right = TreeNode(current.val + l[level])
                current.left = TreeNode(current.val * l[level])
                q.append((current.left, level))
                q.append((current.right , level))
    
    def solve(self):
        ans = 0
        for l in self.input:
            result = l[0]
            test = l[1:]
            if self.bfs(result,test):
                ans += result
        return ans

class solver2:
    def __init__(self, input_lists):
        self.input = input_lists

    def bfs(self, result, l):
        height = len(l)
        root = TreeNode(l[0])
        q = []
        q.append((root, 0))
        while q:
            current, level = q.pop()

            if level == height - 1 and current.val == result:
                return True

            if level + 1 < height:
                level += 1
                current.right = TriNode(current.val + l[level])
                current.middle = TriNode(int(str(current.val)+str(l[level])))
                current.left = TriNode(current.val * l[level])
                q.append((current.left, level))
                q.append((current.middle, level))
                q.append((current.right , level))
    
    def solve(self):
        ans = 0
        for l in self.input:
            result = l[0]
            test = l[1:]
            if self.bfs(result,test):
                ans += result
        return ans


def get_lists():
    # Open the file in read mode
    with open("input.txt", "r") as f:
        res = []  
        for line in f:
            l = list(map(int,list(line.strip().split())))
            res.append(l)
    return res

res = get_lists()

solver = solver1(res)
solution1 = solver.solve()
print("Solution1: " + f"{solution1}")
solver2 = solver2(res)
solution2 = solver2.solve()
print("Solution2: " + f"{solution2}")
