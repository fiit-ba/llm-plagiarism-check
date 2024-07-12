# LLM-plagiarism-check

## TLDR

We're trying to build a system for source code plagiarism detection using Large Language Models (LLMs) via the DSPy framework. The goal is to compare two input code files, determine if plagiarism has occurred, and provide an explanation for the result.

## Using DSPy in 8 Steps

1. **Define your task**
   - Expected input: Two input code files (strings containing plain code) to be compared.
   - Expected output:
     - Plagiarism detection result (Yes/No)
     - Explanation/justification of the result
   - Quality and Cost Specifications: Cost is not a concern; quality is the main priority. We want to try different models.

2. **Define your pipeline**
   - We don't need any external tools or document retrieval. It will be a simple chain-of-thought step, as we want to evaluate LLM capabilities for plagiarism detection.

3. **Explore a few examples**
   - We explored LLM capabilities for plagiarism detection using a few examples with ChatGPT and Claude, yielding promising results.

4. **Define your data**
   - We are working with a dataset from the publication: [Source Code Plagiarism Detection in Academia with Information Retrieval: Dataset and the Observation](https://github.com/oscarkarnalim/sourcecodeplagiarismdataset/blob/master/IR-Plag-Dataset.zip)
   - We selected a subset and manually labeled the dataset with our output labels. This dataset should be used for training and testing, while the rest of the original dataset should be used for evaluation.
   - Dataset: [train.tsv](/data/train.tsv) (65 samples)

5. **Define your metric**
   - We are dealing with a **classification problem**, so we will use accuracy as our main metric. *We don't want to evaluate the explanation/justification of the result at the moment*.
   - Our metric will be simple: if pred_label == true_label then 1 else 0.

6. **Collect preliminary "zero-shot" evaluations**
   - Done in code.

7. **Compile with a DSPy optimizer**
   - We don't want to update weights of the LLM, so we are looking at optimizers such as:
     - BootstrapFewShot
     - BootstrapFewShotWithRandomSearch
     - MIPRO
     - (Consider adding other relevant optimizers)

8. **Iterate**
    - ???