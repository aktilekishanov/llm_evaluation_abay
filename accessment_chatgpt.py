import matplotlib.pyplot as plt
import pandas as pd
import json
from sacrebleu import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer
from nltk.tokenize import word_tokenize

with open('kazakh_translated.json', 'r', encoding='utf-8') as f:
    gpt_translations = {item['id']: item['translated_content']
                        for item in json.load(f)['texts']}

with open('golden.json', 'r', encoding='utf-8') as f:
    golden_translations = {item['id']: item['content']
                           for item in json.load(f)['texts']}

rouge = rouge_scorer.RougeScorer(
    ['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

results = []
for id_ in gpt_translations:
    gpt_text = gpt_translations[id_]
    golden_text = golden_translations[id_]

    bleu = sentence_bleu(gpt_text, [golden_text]).score / 100

    meteor = meteor_score([word_tokenize(golden_text)],
                          word_tokenize(gpt_text))

    rouge_scores = rouge.score(golden_text, gpt_text)
    rouge1 = rouge_scores['rouge1'].fmeasure
    rouge2 = rouge_scores['rouge2'].fmeasure
    rougel = rouge_scores['rougeL'].fmeasure

    results.append({
        'ID': id_,
        'BLEU': bleu,
        'METEOR': meteor,
        'ROUGE1': rouge1,
        'ROUGE2': rouge2,
        'ROUGEL': rougel
    })

df_results = pd.DataFrame(results)
df_results.to_csv('translation_evaluation.csv', index=False)
print("Evaluation metrics saved to 'translation_evaluation.csv'")


# getting averages
df = pd.read_csv("translation_evaluation.csv")
average_scores = df[['BLEU', 'METEOR', 'ROUGE1', 'ROUGE2', 'ROUGEL']].mean()
print("Average Scores:")
print(average_scores)
average_scores.to_csv("average_scores.csv", header=["Score"])


# score interpretation

# Metric	Average     Score	        Interpretation
# BLEU   	~0.0489	    Low:            Indicates limited n-gram overlap. GPT-translated text may diverge significantly from the reference.
# METEOR	~0.2993	    Moderate:       Translations align partially but may lack fluency or precision.
# ROUGE-1	~0.4746	    Moderate:       Captures about half the unigrams, indicating partial content alignment.
# ROUGE-2	~0.0907	    Low:            Limited bigram overlap—suggests a lack of fluency or consistent phrasing.
# ROUGE-L	~0.2204	    Low to Moderate: Indicates partial overlap in sequence structure but room for improvement.


# observations:

# BLEU is Low: Suggests the GPT-translated texts may not closely match the exact phrasing or structure of the reference translations. BLEU typically favors exact matches, so this isn't unexpected for free-form language generation.
# METEOR is Moderate: Reflects reasonable alignment with synonyms and stemming but highlights semantic gaps or missing details.
# ROUGE-1 is Moderate: Indicates some overlap in key terms, suggesting translations are partially capturing main ideas.
# ROUGE-2 and ROUGE-L are Low: Points to issues with fluency, phrasing consistency, and capturing longer textual patterns.
