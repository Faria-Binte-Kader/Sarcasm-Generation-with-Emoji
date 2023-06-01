from retrieve import retrieveCommonSense, processCommonsense
from rank import rankContext , getRoberta
import sys
import csv

roberta = getRoberta()

file = open('comettest.csv')
type(file)
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    utterance = row[0]
    rov = row[1]
    commonsense = retrieveCommonSense(utterance)
    processed_commonsense = processCommonsense(commonsense)
    mostincongruent = rankContext(roberta,rov,utterance,''.join(processed_commonsense),''.join(commonsense))
    sarcasm = rov + ''.join(mostincongruent)
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([utterance, sarcasm])
    print(utterance)
    print(sarcasm)
    print("\n")

file.close()



# from reverse import reverse_valence
# from retrieve import retrieveCommonSense, processCommonsense
# from rank import rankContext , getRoberta
# import sys

# roberta = getRoberta()

# utterance = sys.argv[1]
# rov = reverse_valence(utterance).capitalize()
# # op = retrieveCommonSense(utterance)
# # commonsense, extra = op[0], op[1]
# commonsense = retrieveCommonSense(utterance)
# processed_commonsense = processCommonsense(commonsense)
# mostincongruent = rankContext(roberta,rov,utterance,''.join(processed_commonsense),''.join(commonsense))
# sarcasm = rov + ''.join(mostincongruent)
# mysarcasm = utterance + ''.join(mostincongruent)
# print(sarcasm)
# print(mysarcasm)





	
