def f(pat):
    next = [0]
    len_ = 0
    i = 1
    while i < len(pat):
        if pat[len_] == pat[i]:
            len_ += 1
            next.append(len_)
            i += 1
        else:
            if len_ == 0:
                next.append(0)
                i += 1
            else:
                len_ = next[len_ - 1]
                print(pat[0:i+1],i,len_)
    return next

S = "ababaaababaa"
print(S)
print(f(S))