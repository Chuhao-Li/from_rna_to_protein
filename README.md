# Bioinformatics experiment: From RNA to protein

# Introduction

**实验目的：**

通过完成核苷酸序列的拼接、翻译、折叠，对生物信息学有进一步的认识。

**实验步骤：**

0. 安装python，下载实验所需文件。
1. 对RNA进行模拟测序，生成核苷酸序列片段。
2. 序列拼接
3. 翻译为氨基酸
4. 氨基酸折叠

# Step 0: 安装python，下载实验所需文件。

-  脚本文件下载地址：https://github.com/Chuhao-Li/from_rna_to_protein
-  python下载地址：https://www.python.org/downloads/

检查python是否安装成功：

首先要打开terminal：

- Windows: 进入脚本文件所在文件夹，在资源管理器地址栏输入“cmd”，然后敲击“Enter”键。
- Mac: 进入脚本文件所在文件夹，右击空白处，选择“在这里打开terminal”。

在terminal（弹出的黑色界面）中输入以下命令：

- Windows: `py.exe 00_hello_world.py`
- Mac: `python3 00_hello_world.py`

如果python正确安装了，则会输出以下内容：

```
--------------
Hello world!
Your python environment has been successfully set up!
--------------
```

# Step 1: 对RNA进行模拟测序，生成核苷酸序列片段。

1 查看`HBB_datasets/rna.fna`文件。

2 运行`01_generate_reads.py`脚本，根据指定的序列生成**reads**。

`01_generate_reads.py`的用法：

- Windows: `py.exe 01_generate_reads.py`
- Mac: `python3 01_generate_reads.py`

如果没有提供参数，则默认生成长度为50，**测序深度**为50的reads。可以通过下面的指令来修改参数：

- Windows: `py.exe 01_generate_reads.py 30 20`
- Mac: `python3 01_generate_reads.py 30 20`

其中30代表reads的长度，20代表测序的深度。

# Step 2: 序列拼接

理解De bruijn算法和OLC算法。

## De bruijn算法：

- Windows: `py.exe 02_debruijn_assembly.py`
- Mac: `python3 02_debruijn_assembly.py`

脚本说明：通过de bruijn算法对序列进行拼接。该脚本可以设置k的值。如果不设置，默认为15。

探索：k值过大或者过小会出现什么结果？为什么？

## OLC算法：

- Windows: `py.exe 02_OLC_assembly.py`
- Mac: `python3 02_OLC_assembly.py`

脚本说明：通过OLC算法对序列进行拼接。该脚本可以设置min_overlap的值。如果不设置，默认为25。

如无意外，运行上述命令的时候会报错：

```
min_overlap被设置为： 25
Traceback (most recent call last):
  File "C:\Users\a8799\Desktop\document\001博士学习\005实验室相关\2024-02-23_中学生生物信息实验\Bioinformatics_experiments\from_rna_to_protein\02_OLC_assembly.py", line 19, in <module>
    print(">HBB_rna\n" + reads[0], file=f)
NameError: name 'reads' is not defined
```

这是因为脚本里面的代码块的顺序被打乱了。现在，为了让脚本能够正确运行，请打开脚本文件，仔细阅读里面5个代码块的注释信息，使用剪切-粘贴的功能把顺序调整好，然后再次运行。

参考答案：`02_OLC_assembly_correct.py`

探索：min_overlap值过大或者过小会出现什么结果？为什么？

# Step 3: 翻译为氨基酸

理解RNA翻译为氨基酸的过程。

- Windows: `py.exe 03_translate.py -i 02_OLC_assembly.txt -o translated.txt`
- Mac: `python3 03_translate.py -i 02_OLC_assembly.txt -o translated.txt`

参考答案：可以把结果与`HBB_datasets/protein.faa`比较，检查是否正确翻译。

# Step 4: 氨基酸折叠

打开上一步生成的`translated.txt`文件，把其中的氨基酸序列复制到<a href="https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb" target="_blank">colabfold网站</a>中的`query_sequence`处，然后点击上方菜单栏中的“代码执行程序，然后点击“全部运行”。模拟折叠该氨基酸序列大概需要5-7分钟。

理解蛋白折叠和alphafold。

运行完毕后，会自动下载一个压缩包，打开该压缩包，可以看到5个以".pdb"结尾的文件，分别对应5种折叠方案。把该文件提交到<a href="https://www.rcsb.org/3d-view" target="_blank">蛋白三维结构查看网站</a>，可以查看该氨基酸的三维结构。

探索：修改部分氨基酸序列，看看折叠的结果有什么不一样。