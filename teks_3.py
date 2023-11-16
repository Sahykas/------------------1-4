import os


def read_files(list_files):
    num_lines={}
    for files in list_files:
        with open(files, encoding='utf-8') as f:
            num_lines[files]=len(f.readlines())
    sorted_lines={k: v for k, v in sorted(num_lines.items(), key=lambda x: x[1], reverse=True)}
    print(sorted_lines)
    with open('res.txt','a') as res_file:
        for k, v in sorted_lines.items():
            res_file.write(k+'\n')
            res_file.write(str(v)+'\n')
            with open(k,'r', encoding='utf-8') as f:
                res_file.write(f.read())
                res_file.write('\n')


list_files=['1.txt', '2.txt', '3.txt']
print(read_files(list_files))