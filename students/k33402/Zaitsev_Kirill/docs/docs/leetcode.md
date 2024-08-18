# Leetcode

## 3sum
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))
        if len(z) >= 3:
            res.add((0,0,0))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
```
![3sum.png](..%2Fimg%2F3sum.png)

## Group Anagrams
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sorted_s = {}
        i = 0
        for s in strs:
            if not result:
                sorted_s[''.join(sorted(s))] = i
                i += 1
                result.append([s])
                continue
            for j in range(len(result)):
                if (''.join(sorted(s))) in sorted_s:
                    result[sorted_s[''.join(sorted(s))]].append(s)
                    break
                else:
                    sorted_s[''.join(sorted(s))] = i
                    i += 1
                    result.append([s])
                    break
        return result
```
![Group Anagrams.png](..%2Fimg%2FGroup%20Anagrams.png)

## Longest Substring Without Repeating Characters
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charIndex = [-1] * 128
        left = 0
        
        for right in range(n):
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            charIndex[ord(s[right])] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
```
![Longest Substring Without Repeating Characters.png](..%2Fimg%2FLongest%20Substring%20Without%20Repeating%20Characters.png)

## Longest Palindromic Substring
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1


        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end+1]
```
![Longest Palindromic Substring.png](..%2Fimg%2FLongest%20Palindromic%20Substring.png)

## Increasing Triplet Subsequence
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```
![Increasing Triplet Subsequence.png](..%2Fimg%2FIncreasing%20Triplet%20Subsequence.png)

## Set Matrix Zeroes
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        shouldFillFirstRow = 0 in matrix[0]
        shouldFillFirstCol = 0 in list(zip(*matrix))[0]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if shouldFillFirstRow:
            matrix[0] = [0] * n
        if shouldFillFirstCol:
            for row in matrix:
                row[0] = 0
```
![Set Matrix Zeroes.png](..%2Fimg%2FSet%20Matrix%20Zeroes.png)

## Count and Say
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        def count_til_diff(s: str):
            res = ''
            i = 0
            temp = ''
            while i < len(s):
                count = 1
                check = s[i]
                if check == temp:
                    break
                temp = check
                for j in range(i + 1, len(s)):  
                    if s[j] != check:
                        i = j
                        break
                    count += 1
                    if j == len(s) - 1:
                        i = j
                        break
                res += str(count) + check
            return res
        if n == 1:
            return '1'
        return count_til_diff(self.countAndSay(n - 1))
```
![Count and Say.png](..%2Fimg%2FCount%20and%20Say.png)

## Add Two Numbers
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        total = carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        return res.next
```
![Add Two Numbers.png](..%2Fimg%2FAdd%20Two%20Numbers.png)

## Odd Even Linked List
```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None : return head 
        odd = ListNode(0) 
        odd_ptr = odd
        even = ListNode(0)
        even_ptr = even 
        idx = 1 
        while head != None :
            if idx % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            head = head.next
            idx+=1
        even_ptr.next = None
        odd_ptr.next = even.next
        return odd.next
```
![Odd Even Linked List.png](..%2Fimg%2FOdd%20Even%20Linked%20List.png)

## Binary Tree Inorder Traversal
```python
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
```
![Binary Tree Inorder Traversal.png](..%2Fimg%2FBinary%20Tree%20Inorder%20Traversal.png)

## Binary Tree Zigzag Level Order Traversal
```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = defaultdict(list)
        q = []
        q.append((root,0))
        while len(q)>0:
            cur_n, cur_lvl = q.pop(0)
            if cur_n != None:
                lvls[cur_lvl].append(cur_n.val)
                q.append((cur_n.left, cur_lvl+1))
                q.append((cur_n.right, cur_lvl+1))
        ans = []
        for lvl in lvls:
            if lvl%2==0:
                ans.append(lvls[lvl])
            else:
                ans.append(lvls[lvl][::-1])
        return ans
```
![Binary Tree Zigzag Level Order Traversal.png](..%2Fimg%2FBinary%20Tree%20Zigzag%20Level%20Order%20Traversal.png)

## Construct Binary Tree from Preorder and Inorder Traversal
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_inorder_idx = {inorder[i]: i for i in range(len(inorder))}

        def buildTreePartition(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or inorder_end > len(inorder):
                return None

            root_val = preorder[0]
            root_inorder_idx = val_to_inorder_idx[root_val]
            if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
                return None
            
            root = TreeNode(preorder.pop(0))
            root.left = buildTreePartition(preorder, inorder_start, root_inorder_idx - 1)
            root.right = buildTreePartition(preorder, root_inorder_idx + 1, inorder_end)

            return root

        return buildTreePartition(preorder, 0, len(inorder) - 1)
```
![Construct Binary Tree from Preorder and Inorder Traversal.png](..%2Fimg%2FConstruct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.png)

## Populating Next Right Pointers in Each Node
```python
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i < n - 1: 
                    node.next = q[0]
                if node and node.left: 
                    q.append(node.left)
                if node and node.right: 
                    q.append(node.right)
        return root
```
![Populating Next Right Pointers in Each Node.png](..%2Fimg%2FPopulating%20Next%20Right%20Pointers%20in%20Each%20Node.png)

## Kth Smallest Element in a BST
```python
class Solution:
    def kthSmallest(self, root, k):
        values = []
        self.inorder(root, values)
        return values[k - 1]

    def inorder(self, root, values):
        if root is None:
            return
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)
```
![Kth Smallest Element in a BST.png](..%2Fimg%2FKth%20Smallest%20Element%20in%20a%20BST.png)

## Number of Islands
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
```
![Number of Islands.png](..%2Fimg%2FNumber%20of%20Islands.png)