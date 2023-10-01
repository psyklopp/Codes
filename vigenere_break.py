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


