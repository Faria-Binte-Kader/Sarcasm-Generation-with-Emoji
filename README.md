# Sarcasm-Generation-with-Emoji
If you use the code/data/resources shared here, fully or partially, please cite our paper.
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
Generation of sarcasm from literal negative input is done using three modules: Reversal of Valence, Retrieval of Commonsense and Emoji Prediction. Please look inside the respective folders' READMEs for more details.
