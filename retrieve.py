import nltk
import yaml
import string
import json
from loadconfig import loadConfig
import os
import sys
import json
import ast
from urllib.parse import quote
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

sys.path.append(os.getcwd()+'/comet_distil_2022')
m = {}
words = []

from pattern.en import conjugate, lemma, lexeme, PRESENT, PAST, SG,PARTICIPLE

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def choppunc(stri):
	if stri.endswith('.') or stri.endswith('?') or stri.endswith('!'):
		return stri[:-1]
	else:
		return stri


# def preprocess(utterance):

# 	stop_words, missing, quantifier, replacements, start, wrongNE = loadConfig(
# 	    'Retrieve')
# 	sent = choppunc(utterance)
# 	b = sent.split()
# 	b[0] = b[0].lower().capitalize()
# 	c = nltk.pos_tag(b)
# 	d = nltk.ne_chunk(c, binary=True)
# 	m = {}
# 	for val in d:
# 		if str(type(val)) == "<class 'nltk.tree.Tree'>":
# 			for v in val:
# 				m[v[0]] = val.label()
# 		else:
# 			m[val[0]] = "NNE"
# 	# for u, v in c:
# 	# 	if (v == 'NNP' and m[u] == 'NE' and u not in wrongNE) or (v == 'CD' and u not in quantifier) or u == ',' or u == 'U.S':
# 	# 		stop_words.append(u.lower())

# 	x = sent.lower().split()

# 	elem = []
# 	for i in range(len(x)):
# 		w = x[i]
# 		if (w not in stop_words):
# 			elem.append(w)

# 	if len(elem) >= 5 and missing[0] in elem:
# 		elem = ' '.join(elem).replace(' .', '.')
# 		elem = elem.replace(' '+missing[0], '')
# 	else:
# 		elem = ' '.join(elem).replace(' .', '.')


# 	for v in start:
# 		if elem.startswith(v):
# 			elem = elem.replace(v+' ', '')

# 	for v in replacements:
# 		rep = v.split(',')
# 		if rep[0] in elem:
# 			elem = elem.replace(rep[0], rep[1])

# 	return elem


# def getCommonSense(utterance):
# 	os.system('python comet_distil_2022/generate_comet_distil.py --model_path comet_distil_2022/downloaded/comet-distill-low/ --input "'+utterance+'" --output_file output.json --device 0 --sampling_algorithm beam-5')
# 	output = json.load(open('output.json', "rb"))
# 	for i in range(0,5):
# 		output[0][i] = json.dumps(output[0][i])
# 		print(output[0][i])
# 		output[0][i] = output[0][i].replace('"','')
# 		output[0][i] = output[0][i].strip()
# 		output[0][i] = output[0][i].replace('is ','')
# 		if 'internet' in output[0][i]:
# 			return 'internet'
# 		if ' ' not in output[0][i] and len(output[0][i])>=2:
# 			return output[0][i]
# 	return output[0][4]

def getCommonSense(utterance):
	os.system('python comet_distil_2022/generate_comet_distil.py --model_path comet_distil_2022/downloaded/comet-distill-low/ --input "'+utterance+'" --output_file output.json --device 0 --sampling_algorithm beam-5')
	output = json.load(open('output.json', "rb"))
	#print(output)
	output = json.dumps(output)
	return output
	#print(output)

def processCommonsense(retrieved_utterance):
	if len(retrieved_utterance)>2:
		stop_words = set(stopwords.words('english'))
		word_tokens = word_tokenize(retrieved_utterance)
		filtered_output = [w for w in word_tokens if not w.lower() in stop_words]
		filtered_output = []
		for w in word_tokens:
			if w not in stop_words:
				filtered_output.append(w)
		outputStr = ''.join(filtered_output)
	else:
		outputStr = ''.join(retrieved_utterance)
	outputStr = outputStr.replace('`','')
	outputStr = outputStr.replace("'",'')
	outputStr = outputStr.strip()
	print(outputStr, "outputStr")
	return outputStr

def retrieveCommonSense(utterance):
	# modified_utterance = preprocess(utterance)
	retrieved_utterance = getCommonSense(utterance)
	# print(retrieved_utterance, "retrieve")
	return retrieved_utterance



#print(retrieveCommonSense(sys.argv[1]))




