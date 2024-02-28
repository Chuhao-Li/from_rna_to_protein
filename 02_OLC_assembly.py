
def merge_contig(a, b, min_overlap=25):
    min_L = min(len(a), len(b))
    # 处理相互包含的
    if a in b:
        return b
    if b in a:
        return a
    # 处理头尾相接的
    # a head overlap with b tail
    for i in range(25, min_L+1):
        if a[:i] == b[-i:]:
            c = b + a[i:]
            return c
    # a tail overlap with b head
    for i in range(25, min_L+1):
        if b[:i] == a[-i:]:
            c = a + b[i:]
            return c
    return None

contigs = open("01_output_contig.txt").read().splitlines()

# a = "GCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTG"
# b = "TGGTGGTGAGGCCCTGGGCAGGCTGCTGTTTGCCACACTGAGTGAGCTGC"

# c = merge_contig(a, b)

# print("n contigs: ", len(contigs))
while len(contigs) > 1:
    for i in range(len(contigs)):
        for j in range(i+1, len(contigs)):
            a = contigs[i]
            b = contigs[j]
            if a and b:
                c = merge_contig(a, b)
                if c:
                    contigs[i] = c
                    contigs[j] = None
    contigs = [i for i in contigs if i]
    # if len(contigs) == 4:
    #     print(contigs)
    # print("n contigs: ", len(contigs))

with open("02_OLC_assembly.txt", "w") as f:
    print(">HBB_rna\n" + contigs[0], file=f)

print("\n运行完毕！请检查'02_OLC_assembly.txt'文件。")

