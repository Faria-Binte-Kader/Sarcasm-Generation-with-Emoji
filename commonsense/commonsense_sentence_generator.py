import spacy
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-common_gen")
model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-common_gen")

def genSentence(words, max_length=32):
   input_text = words
   features = tokenizer([input_text], return_tensors='pt')
   output = model.generate(input_ids=features['input_ids'], 
               attention_mask=features['attention_mask'],
               max_length=max_length)
   print(tokenizer.decode(output[0], skip_special_tokens=True))
   return tokenizer.decode(output[0], skip_special_tokens=True)

def detectSubject(input, sub):
   nlp = spacy.load("en_core_web_sm")
   sent = input
   doc=nlp(sent)
   sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj") ]
   for i in sub_toks:
     sub = i.text
   return sub

def genCommonsenseSentence(input, keyphrase):
   sub = detectSubject(input, "I")
   if (sub == "I" or sub == "i") and ("is" in keyphrase or "are" in keyphrase):
      keyphrase = keyphrase.replace('is','am')
      keyphrase = keyphrase.replace('are','am')
   elif (sub == "They" or sub == "they") and ("is" in keyphrase or "am" in keyphrase):
      keyphrase = keyphrase.replace('is','are')
      keyphrase = keyphrase.replace('am','are')
   elif (sub == "He" or sub == "he" or sub == "She" or sub == "she") and ("am" in keyphrase or "are" in keyphrase):
      keyphrase = keyphrase.replace('am','is')
      keyphrase = keyphrase.replace('are','is')
   keyphrase = keyphrase.replace('"','') 
   words = keyphrase + " " + sub
   return genSentence(words)

# output = genCommonsenseSentence("They will never learn", "is a failure")
# print(output)