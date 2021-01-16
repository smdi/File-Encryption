







import csv
from itertools import islice



from  encrypt_file import enocdeWord
from  decrypt_file import  decodeWord



#
# title_encoded = open("title_encoded.tsv", "w")
# title_encoded_tsv_writer = csv.writer(title_encoded, delimiter='\t')


encodefile = open('title_encoded.tsv', "a")

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

                        encodefile.write(head+"\t"+encWord+"\n")

                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

    print("completed")
    # title_encoded.close()
    paseddata.close()
    encodefile.close()




































