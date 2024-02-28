# 1. 读取序列。
# 2. 根据reads长度、覆盖度生成随机数。
# 3. 把生成的随机n数作为序列的起点，n+read length作为终点，contigs.

def read_fasta(infile):
    out = {}
    ID = None
    for i in open(infile):
        if i.startswith(">"):
            if ID:
                out[ID] = "".join(seq)
            ID = i.lstrip(">").split(" ")[0]
            seq = []
        else:
            seq.append(i.strip())
    else:
        out[ID] = "".join(seq)
    return(out)

ref = read_fasta("HBB_datasets/rna.fna")

contig_len = 50
coverage = 50

seq = ref["NM_000518.5"]
ref_len = len(seq)
contig_num = int(ref_len*coverage/ contig_len)

start = 0
end = ref_len - contig_len

import random
with open("01_output_contig.txt", "w") as f:
    start_points = [random.randint(start, end) for i in range(contig_num)]
    # print(sorted(start_points))
    for n in start_points:
        print(seq[n:n+contig_len], file=f)

print("\n运行完毕！请检查结果文件'01_output_contig.txt'。")
