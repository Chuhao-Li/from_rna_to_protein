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

- Windows: `py.exe 01_generate_contig.py`
- Mac: `python3 01_generate_contig.py`

# Step 2: 序列拼接

De bruijn算法：

- Windows: `py.exe 02_debruijn_assembly.py`
- Mac: `python3 02_debruijn_assembly.py`

OLC算法：

- Windows: `py.exe 02_OLC_assembly.py`
- Mac: `python3 02_OLC_assembly.py`

# Step 3: 翻译为氨基酸

- Windows: `py.exe 03_translate.py -i 02_OLC_assembly.txt -o translated.txt`
- Mac: `python3 03_translate.py -i 02_OLC_assembly.txt -o translated.txt`

# Step 4: 氨基酸折叠

打开上一步生成的`translated.txt`文件，把其中的氨基酸序列复制到<a href="https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb" target="_blank">colabfold网站</a>，点击“运行全部”。模拟折叠该氨基酸序列大概需要7分钟。

运行完毕后，会自动下载一个压缩包，打开该压缩包，可以看到5个以".pdb"结尾的文件。把该文件提交到<a href="https://www.rcsb.org/3d-view" target="_blank">蛋白三维结构查看网站</a>，可以查看该氨基酸的三维结构。