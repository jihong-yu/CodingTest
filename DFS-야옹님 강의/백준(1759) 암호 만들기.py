def dfs(depth, start, password):
    if depth == L:
        vowel_count = 0
        for i in password:
            if i in aeiou:
                vowel_count += 1
        if vowel_count <= 0 or vowel_count >= L - 1:
            return
        print(password)
        return

    for i in range(start, C):
        dfs(depth + 1, i + 1, password + pw[i])


L, C = map(int, input().split())
pw = list(input().split())

aeiou = ['a', 'e', 'i', 'o', 'u']
pw.sort()
dfs(0, 0, '')
