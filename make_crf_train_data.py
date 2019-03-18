import sys
import codecs

def data_tag(input_file,output):
    input_data=codecs.open(input_file,'r','utf-8')
    output_data=codecs.open(output,'w','utf-8')
    for line in input_data.readlines():
        #逐行读取数据
        #按空格切分
        word_list=line.strip().split()
        for word in word_list:
            if len(word)==1:
                output_data.write(word+"\tS\n")
            else:# BMMME
                output_data.write(word[0]+"\tB\n")
                for w in word[1:len(word)-1]:
                    output_data.write(w+"\tM\n")
                output_data.write(word[len(word)-1]+"\tE\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()

if __name__=="__main__":
    input_file="F://pku_training.utf8"
    output_file="F://crf_data.txt"
    data_tag(input_file,output_file)