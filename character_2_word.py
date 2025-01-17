import codecs
import sys

def character_2_word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        if line == "\r\n":
            output_data.write("\r\n")
        else:
            char_tag_pair = line.strip().split('\t')

            char = char_tag_pair[0]
            tag = char_tag_pair[2]
            #print(char,' ',tag)

            if tag == 'B':
                output_data.write(' ' + char)
            elif tag == 'M':
                output_data.write(char)
            elif tag == 'E':
                output_data.write(char + ' ')
            else: # tag == 'S'
                output_data.write(' ' + char + ' ')
                input_data.close()
    output_data.close()

if __name__ == '__main__':

    input_file = 'F://crf_testing.tag.utf8'
    output_file = 'F://result.utf8'
    character_2_word(input_file, output_file)