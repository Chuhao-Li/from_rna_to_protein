# 这里是正确的代码块顺序：A-C-E-D-B


#####################Code block A: 读取传入参数。########################
# 代码注释：min_overlap 参数默认为25，如果用户在命令行末端添加了
# 一个数字，min_overlap将被设置为该数值。
import sys
min_overlap = 25
if len(sys.argv) == 2:
    min_overlap = int(sys.argv[1])
print("min_overlap被设置为：", min_overlap)
#####################Code block A: 读取传入参数。########################



#####################Code block C: 定义函数。########################
# 代码注释：重复运行的代码，为了避免写很多次，我们会定义为“函数”。
# 以下“merge_contig”函数的作用是检测两条序列是否有至少“min_overlap”
# 个碱基的重叠，如果是，那就合并到一起。
def merge_contig(a, b, min_overlap=25):
    min_L = min(len(a), len(b))
    # 处理相互包含的
    if a in b:
        return b
    if b in a:
        return a
    # 处理头尾相接的
    # a head overlap with b tail
    for i in range(min_overlap, min_L+1):
        if a[:i] == b[-i:]:
            c = b + a[i:]
            return c
    # a tail overlap with b head
    for i in range(min_overlap, min_L+1):
        if b[:i] == a[-i:]:
            c = a + b[i:]
            return c
    return None
#####################Code block C: 定义函数。########################



#####################Code block E: 读取reads。########################
# 代码注释：读取所有生成的reads。
reads = open("01_output_reads.txt").read().splitlines()
#####################Code block E: 读取reads。########################



#####################Code block D: 执行拼接。########################
# 代码注释：对reads进行两两比较，如果有重叠，就合并在一起，直到只剩下
# 一条read，或者reads的数目不再变化。
n_reads = len(reads)
while len(reads) > 1:
    for i in range(len(reads)):
        for j in range(i+1, len(reads)):
            a = reads[i]
            b = reads[j]
            if a and b:
                c = merge_contig(a, b, min_overlap=min_overlap)
                if c:
                    reads[i] = c
                    reads[j] = None
    reads = [i for i in reads if i]
    n_reads_tmp = len(reads)
    reduced_reads = n_reads - n_reads_tmp
    if reduced_reads == 0:
        print("reads数没有发生改变，这意味着无法拼成单条完整的序列。退出程序。")
        exit()
    n_reads = n_reads_tmp
#####################Code block D: 执行拼接。########################



#####################Code block B: 输出结果。########################
# 代码注释：把得到的结果输出到文件。
with open("02_OLC_assembly.txt", "w") as f:
    print(">HBB_rna\n" + reads[0], file=f)

print("\n运行完毕！请检查'02_OLC_assembly.txt'文件。")
#####################Code block B: 输出结果。########################

