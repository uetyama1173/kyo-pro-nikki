from itertools import product  # import文は一番上にまとめておくほうが良いです


def judge(pro):
    S = 0
    for i in range(N): #0,1,2,3,4
        #タプルを全検索
        if pro[i]==1:  # pro[i] が 1 なら A[i] を足す（if文の判定では、0はFalse扱い、他の整数はTrue扱いされます）
            S += A[i] #2+4 = 6

    if S == W:  # S == W なら +1、そうでなければ 0 を返す
        return 1
    else:
        return 0


#N=5 配列数, A={1,2,3,6,8}  W=10　たしあわせて10　になる　組み合わせは何通り存在するのか
# N, W = map(int, input().split())
# A = list(map(int, input().split()))
N, W = 5, 10
A = [1,2,3,6,8]

ans = 0
for pro in product((0, 1), repeat=N):
    #[0,0,0,0,0]
    #[0,1,0,0,1]
    ans += judge(pro)  #  タプルproを渡す judgeは選び方の合計がWなら1, そうでないなら0を返す 

print(ans)