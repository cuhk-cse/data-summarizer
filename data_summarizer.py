#########################################################
# dataset_summarizer.py 
# Last updated: 2015/8/15
#########################################################

import os

#########################################################
# config area
dataDir = 'data' # dataset folder
#########################################################


def summarize(rootDir, level=1): 
    if level==1: 
        (str_size, num_files) = get_size(rootDir)
        str_summary = rootDir + '(' + str(num_files) + 'files)(' + str_size + ')/'
        print_summary(fid, str_summary)  
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists)          
        (str_size, num_files) = get_size(path)
        if os.path.isdir(path): 
            str_summary = '|  '*(level - 1) + '|--' + lists + '('\
                + str(num_files) + 'files)(' + str_size + ')/'
            print_summary(fid, str_summary)
            summarize(path, level + 1) 
        else: 
            str_summary = '|  '*(level - 1)+'|--' + lists + '(' + str_size + ')'
            print_summary(fid, str_summary)


def get_size(path):
    num_files = 0
    if os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
                num_files += 1
    else:
            total_size = os.path.getsize(path)
    
    if total_size < 1024000:
        total_size_str = '%.2fK'%(total_size / 1024.0)
    elif total_size < 1000 * (1024 **2):
        total_size_str = '%.2fM'%(total_size / (1024.0 **2))
    elif total_size < 1000 * (1024 **3):
        total_size_str = '%.2fG'%(total_size / (1024.0 **3))
    else:
        total_size_str = '%.2fT'%(total_size / (1024.0 **4))
    return total_size_str, num_files


def print_summary(fid, str_summary):
    print str_summary
    fid.write(str_summary + '\n')


if __name__ == '__main__':
    with open(dataDir + '_summary.txt', 'w') as fid:
        summarize(dataDir)
