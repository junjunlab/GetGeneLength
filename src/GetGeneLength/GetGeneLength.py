def main():
    """
    Extract gene length based on featureCount calculation gene nonredundant exon length method.
    """
    # 引入库
    import argparse

    parser = argparse.ArgumentParser(usage="GetGeneLength --database ensembl --gtffile gencode.v38.annotation_human.gtf --lengthfile gene_length.txt",
                                    description="Get gene length from GTF annotation file.",
                                    epilog="Thank your for your support, if you have any questions or suggestions please contact me: 3219030654@stu.cpu.edu.cn.")
    parser.add_argument('-v','--version', action='version', version='%(prog)s 0.0.1')
    # 读取注释类型文件
    parser.add_argument('-d','--database',type=str,action="store",dest="database",choices=['ucsc','ensembl','gencode'],
                        default="ensembl",help='which annotation database you choose. (default="ensembl")')
    # 读取gtf文件
    parser.add_argument('-g','--gtffile', type=str,action="store",dest="gtffile",help='input your GTF file. (ucsc/ensembl/gencode)')
    # 导出文件名称
    parser.add_argument('-l','--lengthfile', type=str,action="store",dest="length_info",help='output your gene lenth file. (gene_length.txt)')
    # 解析参数
    args = parser.parse_args()

    # 获取参数
    database = args.database
    gtffile =  args.gtffile
    length_info = args.length_info
    
    # main fuction
    print("Your job is running, please wait...\n")
    # 打开测试 gtf 文件
    with open(gtffile,'r') as gtf:
        # 信息保存在字典里
        info = {}
        for line in gtf:
            # 跳过注释行
            if line.startswith('#'):
                continue
            # 分割
            fields = line.split()
            # 类型
            type = fields[2]
            # database
            if database == "ucsc":
                if type == 'exon':
                    # 名称
                    gene_name = fields[17].replace('"','').replace(';','')
                    gene_id = fields[9].replace('"','').replace(';','')
                    # 连接名称
                    key = gene_name + '|' + gene_id
                    # 计算多个外显子长度
                    start = int(fields[3])
                    end = int(fields[4]) + 1
                    tmpfield = list(range(start,end))
                    # 储存所有exon位置信息
                    info.setdefault(key,[])
                    info[key] += tmpfield
                else:
                    pass
            else:
                if type == 'exon':
                    # 名称
                    gene_name = fields[15].replace('"','').replace(';','')
                    gene_id = fields[9].replace('"','').replace(';','')
                    gene_type = fields[13].replace('"','').replace(';','')
                    # 连接名称
                    key = gene_name + '|' + gene_id + '|' + gene_type
                    # 计算多个外显子长度
                    start = int(fields[3])
                    end = int(fields[4]) + 1
                    tmpfield = list(range(start,end))
                    # 储存所有exon位置信息
                    info.setdefault(key,[])
                    info[key] += tmpfield
                else:
                    pass

    # 取并集(删除重复元素)
    # final_res = {}
    # loop for every gene
    # for key,val in info.items():
    #     length = len(list(set(val)))
    #     final_res[key] = length
    # 计算长度
    final_res = {key:len(list(set(val))) for key,val in info.items()}

    # 导出保存
    res =  open(length_info,'w')  

    # database
    if database == "ucsc":
        for key,val in final_res.items():
            ids = key.split(sep='|')
            res.write(ids[0] + '\t' + ids[1] + '\t' + str(val) + '\n') 
    else:
        for key,val in final_res.items():
            ids = key.split(sep='|')
            res.write(ids[0] + '\t' + ids[1] + '\t' + str(val) + '\n') 
                    
    # 关闭文件    
    res.close()
    print("Your job is done!")
