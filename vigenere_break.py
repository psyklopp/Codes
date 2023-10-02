#1 get length of cipher text
cipher_text = "uwmunjmakfsmfaavbuokvuflkglcomdtoklhavtykwctsflhnwgapnsjlgdbdtokbfjyulkwaggucuktaaqypatyhwfmgabfovtmymugwdcuoucmhggucukrdtoklgfvtylpryneurxtraykravhnwdwkkkwqrrvkibjwrcvtylprlbjbhuxlprymjikhwjavkloqhnujmnsvghcbkvurstvahnwligawgngakrfokkjqryggbnsbtibakvknrelpraskcruxwwcjggahnwkwitvgnkgmvabuklprahmkuuxxanylaubgdvlvtmymqgkcfvaafwhnbfobuovqyhwlfrkgemntvlprdavmyuxwqfkbtibywvpvspacusroixogxmmkllprtevciytvavjhwqhugtmntvwwfgedkcswgvaxxjwqubtibauraffblncxrgdobmaknturaffrgd"
cipher_length = len(cipher_text)
print('Cipher Length:',cipher_length)

#2 iterate and get trigrams and save it in a set
trigram_set = set()
for i in range(0, cipher_length-2):
    trigram = cipher_text[i:i+3]
    trigram_set.add(trigram)

#3 find the count of each trigram 
count_dic = {x:cipher_text.count(x) for x in trigram_set}

#4 and sort it to find the 10 highest appearances
sorted_count_dic = sorted(count_dic.items(), key=lambda item:item[1], reverse = True)
print('\n',sorted_count_dic[:10])
check_trigram = sorted_count_dic[0] #highest occurence = lpr
print('\nHighest occurence - ',check_trigram)

#5 find the locations of trigram in the cipher_text
import re
for i in re.finditer('lpr', cipher_text):
    print('\nFound', i.start(), i.end())

#6 GCD is 5 - length of key is taken as 5
t = 5
chunks = [cipher_text[i:i+t] for i in range(0, cipher_length, t)]
#print('\n',chunks)

#7 make helper dictionary from a to y with 1-25
import string
helper_dict = dict(zip(string.ascii_lowercase, range(1,27)))
helper_dict.pop('z')
print(helper_dict)

#8 read each chunk - we know that 'lpr' translates to 'the'
# l = 12 t = 20
# p = 16 h = 8
# r = 18 e = 5
# to get the key, we do cipher text - plainttext mod 25 (because we don't have z)
# We do this for each chunk we got earlier
key_list = list(helper_dict.keys())
val_list = list(helper_dict.values())
for item in chunks:
    # position 1
    position_1 = (helper_dict[item[0]] - 17) % 25
    char_1 = key_list[position_1-1]
    # position 2
    position_2 = (helper_dict[item[1]] - 8) % 25
    char_2 = key_list[position_2-1]
    # position 3
    position_3 = (helper_dict[item[2]] - 13) % 25
    char_3 = key_list[position_3-1]
    # position 4
    position_4 = (helper_dict[item[3]] - 6) % 25
    char_4 = key_list[position_4-1]
    # position 5
    position_5 = (helper_dict[item[4]] - 18) % 25
    char_5 = key_list[position_5-1]
    print(char_1+char_2+char_3+char_4+char_5)

#clarification, after checking out the correct 3 words in each chunk it was quite easy to guess the remaining
#letters
