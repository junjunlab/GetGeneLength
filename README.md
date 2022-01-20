# GetGeneLength Package

- Extract gene length based on featureCount calculation gene nonredundant exon length method.

- If you want to calculate TPM/FPKM/RPKM to visualize results and for other downstream analysis with only count matrix, you can use this **GetGeneLength** function to get gene length information and get normalized values.

## Install

```shell
$ pip install GetGeneLength
```

## Usage

help infomation:

```shell
$ GetGeneLength -h
usage: GetGeneLength --database ensembl --gtffile gencode.v38.annotation_human.gtf --lengthfile gene_length.txt

Get gene length from GTF annotation file.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d {ucsc,ensembl,gencode}, --database {ucsc,ensembl,gencode}
                        which annotation database you choose. (default="ensembl")
  -g GTFFILE, --gtffile GTFFILE
                        input your GTF file. (ucsc/ensembl/gencode)
  -l LENGTH_INFO, --lengthfile LENGTH_INFO
                        output your gene lenth file. (gene_length.txt)

Thank your for your support, if you have any questions or suggestions please contact me: 3219030654@stu.cpu.edu.cn.
```

for ucsc gtf file:

```shell
$ GetGeneLength -d ucsc -g hg38.ncbiRefSeq.gtf -l ucsc_gene_length.txt
Your job is running, please wait...

Your job is done!

$ head -n 3 ucsc_gene_length.txt
TRNP	TRNP	68
TRNT	TRNT	66
CYTB	CYTB	1141
```

for gencode/ensembl gtf file:

```shell
$ GetTss -d gencode -g gencode.v38.annotation_human.gtf -l gene_length.txt
Your job is running, please wait...

Your job is done!

$ head -n 3 gene_length.txt
DDX11L1	ENSG00000223972.5	transcribed_unprocessed_pseudogene	1735
WASH7P	ENSG00000227232.5	unprocessed_pseudogene	1351
MIR6859-1	ENSG00000278267.1	miRNA	68
```