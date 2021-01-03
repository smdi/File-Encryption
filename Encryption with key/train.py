

import sys
import csv
from itertools import islice
import re


from  encrypt_file import enocdeWord
from  decrypt_file import  decodeWord


#
# csv.field_size_limit(sys.maxsize)

title_encoded = open("title_encoded.tsv", "w")
title_encoded_tsv_writer = csv.writer(title_encoded, delimiter='\t')


N = 500

with open('../title.tsv', 'r') as paseddata:

    print("started")
    while True:
        try:
            next_n_lines = list(islice(paseddata, N))
            read_tsv = csv.reader(next_n_lines, delimiter="\t")
            if not next_n_lines:
                break
            try:

                for row in read_tsv:

                    try:
                        head = str(row[0]).strip().lower()
                        encWord = enocdeWord(head)

                        title_encoded_tsv_writer.writerow([head, encWord])
                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

    print("completed")
    title_encoded.close()
    paseddata.close()









