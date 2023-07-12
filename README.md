# “When Words Fail, Emojis Prevail”: Generating Sarcastic Utterances with Emoji Using Valence Reversal and Semantic Incongruity
This repository contains the code, data, and models of the paper titled "“When Words Fail, Emojis Prevail”: Generating Sarcastic Utterances with Emoji Using Valence Reversal and Semantic Incongruity" published in  ***61st Annual Meeting of the Association for Computational Linguistics-Student Research Workshop : ACL SRW 2023***.

[![arXiv](https://img.shields.io/badge/arXiv-2305.04105-b31b1b.svg)](https://arxiv.org/abs/2305.04105)
[![anthology](https://img.shields.io/badge/ACL%20Anthology-2023.aclsrw.47-EE161F.svg)](https://aclanthology.org/2023.acl-srw.47/)
[![GoogleScholar](https://img.shields.io/badge/Google%20Scholar-4285F4?style=flat&logo=Google+Scholar&logoColor=white&color=gray&labelColor=4285F4)](https://tinyurl.com/2zh5nrsh)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?style=flat&logo=ResearchGate&logoColor=white&color=gray&labelColor=00CCBB)](https://tinyurl.com/278f4us9)

[![PDF](https://img.shields.io/badge/Paper%20PDF-EF3939?style=flat&logo=adobeacrobatreader&logoColor=white&color=gray&labelColor=ec1c24)](https://aclanthology.org/2023.acl-srw.47.pdf)
[![Poster](https://img.shields.io/badge/Poster%20PDF-EF3939?style=flat&logo=Microsoft+PowerPoint&logoColor=white&color=gray&labelColor=B7472A)](https://drive.google.com/file/d/1EGaVY3H-iyaKjEr2bchgOmJ8Q771CE00/view?usp=sharing)
[![Video](https://img.shields.io/badge/Video%20Presentation-4285F4?style=flat&logo=Google+Drive&logoColor=white&color=gray&labelColor=4285F4)](https://drive.google.com/file/d/1IR6yGm2vlVmYwJb3HGedVL4BUJ83GYP3/view?usp=sharing)



**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

[![license](https://arxiv.org/icons/licenses/by-nc-sa-4.0.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Data Format




## Data Construction
Generation of sarcasm from literal negative input is done using three modules: Reversal of Valence, Retrieval of Commonsense and Emoji Prediction.
### Model Architecture
![model](https://github.com/WrightlyRong/Sarcasm-Generation-with-Emoji/assets/55374565/31762ad7-b29e-46ba-897f-21f5816c8061)

### Reversal of Valence

### Retrieval of Commonsense
You can get the data and model for COMET-DISTIL [here](https://storage.googleapis.com/ai2-mosaic-public/projects/symbolic-knowledge-decoding/symbolic-knowledge-distillation.tar.gz)

For using COMET-ATOMIC2020 instead, you can find the data [here](https://allenai.org/data/atomic-2020) and you would need to download the [BART](https://storage.googleapis.com/ai2-mosaic-public/projects/mosaic-kgs/comet-atomic_2020_BART.zip) and [GPT2](https://storage.googleapis.com/ai2-mosaic-public/projects/mosaic-kgs/comet-atomic_2020_GPT2XL.zip) model separately. 

### Emoji Prediction



## Results

## Citation
If you find this work useful, please cite our paper:
```
@inproceedings{kader-etal-2023-words,
    title = "{``}When Words Fail, Emojis Prevail{''}: A Novel Architecture for Generating Sarcastic Sentences With Emoji Using Valence Reversal and Semantic Incongruity",
    author = "Kader, Faria Binte  and
      Hossain Nujat, Nafisa  and
      Sogir, Tasmia Binte  and
      Kabir, Mohsinul  and
      Mahmud, Hasan  and
      Hasan, Md Kamrul",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-srw.47",
    pages = "334--351",
    abstract = "Sarcasm is a form of figurative language that serves as a humorous tool for mockery and ridicule. We present a novel architecture for sarcasm generation with emoji from a non-sarcastic input sentence in English. We divide the generation task into two sub tasks: one for generating textual sarcasm and another for collecting emojis associated with those sarcastic sentences. Two key elements of sarcasm are incorporated into the textual sarcasm generation task: valence reversal and semantic incongruity with context, where the context may involve shared commonsense or general knowledge between the speaker and their audience. The majority of existing sarcasm generation works have focused on this textual form. However, in the real world, when written texts fall short of effectively capturing the emotional cues of spoken and face-to-face communication, people often opt for emojis to accurately express their emotions. Due to the wide range of applications of emojis, incorporating appropriate emojis to generate textual sarcastic sentences helps advance sarcasm generation. We conclude our study by evaluating the generated sarcastic sentences using human judgement. All the codes and data used in this study has been made publicly available.",
}

```
