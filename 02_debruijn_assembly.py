import sys

def debrujin(z):
    nodes, edges = set(), set()
    for s in z:
        a, b = s[:-1], s[1:]
        nodes.add(a)
        nodes.add(b)
        edges.add((a,b))
    return nodes, edges

def adjlist(nodes, edges):
    outgoing = {}
    for node in nodes:
        outgoing[node] = set()
    for a,b in edges:
        outgoing[a].add(b)
    return outgoing

def revcmp(s):
    return s[::-1].translate(str.maketrans({'A':'T','T':'A','C':'G','G':'C'}))

def revcmpext(z):
    x = set(z)
    for s in z:
        x.add(revcmp(s))
    return x

def kmers(z, k):
    x = set()
    for s in z:
        for i in range(len(s)-k+1):
            x.add(s[i:i+k])
    return x

# reads = sys.stdin.read().strip().split("\n")
# reads = open("rosalind_gasm.txt").read().splitlines()
reads = open("01_output_reads.txt").read().splitlines()

# for k in range(len(reads[0])-1, 1, -1): # 尝试多种k
k = 15
if len(sys.argv) == 2:
    k = int(sys.argv[1])

print("\n设置了k（把reads打断为片段的长度）为：", k)

z = reads
# nodes, edges = debrujin(kmers(revcmpext(z), k)) # 考虑反向互补
nodes, edges = debrujin(kmers(z, k)) # 不考虑反向互补
adj = adjlist(nodes, edges)
# start = sorted(nodes)[0] # 随机起点
# 没有source的node作为起点。
targets = set([i[1] for i in edges])
putative_starts = set(nodes) - targets
# print("putative_starts: ", putative_starts)
# 没有target的node作为终点。
putative_ends = set(nodes) - set([i[0] for i in edges])
if len(putative_starts) > 1:
    print("有多个起点，退出程序。")
    exit()
if len(putative_starts) == 0:
    print("没有找到起点，退出程序。")
    exit()
if len(putative_ends) > 1:
    print("有多个终点，退出程序。")
    exit()
if len(putative_ends) == 0:
    print("没有找到终点，退出程序。")
    exit()

out = open("02_debruijn_assembly.txt", "w")
for start in putative_starts:
    if len(adj[start]) > 1:
        print("出现分叉，退出程序。")
        break
    succ = list(adj[start])[0] # succ: start对应的第一个target
    s = [start]
    while len(adj[succ]) > 0:
        if len(adj[succ]) > 1:
            print("出现分叉，退出程序。")
            exit()
        s.append(succ[-1])
        succ = list(adj[succ])[0]
    s.append(succ[-1])
    print(">HBB_rna\n" + "".join(s), file=out)

out.close()

print("\n运行完毕！请检查输出文件'02_debruijn_assembly.txt'。")
