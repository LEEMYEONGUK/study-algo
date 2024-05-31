# 트리순회

def preorder(x):
    if x:
        print(chr(x), end="")
        preorder(l_lst[x])
        preorder(r_lst[x])

def inorder(x):
    if x:
        inorder(l_lst[x])
        print(chr(x), end="")
        inorder(r_lst[x])
def postorder(x):
    if x:
        postorder(l_lst[x])
        postorder(r_lst[x])
        print(chr(x), end="")


N = int(input())
l_lst = [0] * 100
r_lst = [0] * 100
for _ in range(N):
    a, b, c = map(str, input().split())
    if b.isalpha():
        l_lst[ord(a)] = (ord(b))
    if c.isalpha():
        r_lst[ord(a)] = (ord(c))

preorder(65)
print()
inorder(65)
print()
postorder(65)
