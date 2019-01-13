import itertools
def expressiveWords(S, words):
    def RLE(S):
        for k, grp in itertools.groupby(S):
            print(k,list(grp))
        return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(S)])

    R, count = RLE(S)
    print(R,count)
    ans = 0
    for word in words:
        R2, count2 = RLE(word)
        if R2 != R: continue
        ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, count2))

    return ans


S = "heeellooo"
words = ["hello", "hi", "helo"]
expressiveWords(S,words)