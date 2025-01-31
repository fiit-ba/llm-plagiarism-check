# LLM-plagiarism-check

We're trying to build a system for source code plagiarism detection using Large Language Models (LLMs) via the DSPy framework. The goal is to compare two input code files, determine if plagiarism has occurred, and provide an explanation for the result.


## Installation

```bash
# Clone the repository
git clone https://github.com/williambrach/LLM-plagiarism-check.git
cd LLM-plagiarism-check

# Create a virtual environment
python3 -m venv llm-plagiarism-check

# Activate the virtual environment
source llm-plagiarism-check/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Usage

Our project consists of several key components, each serving a specific purpose in our research workflow:

### Jupyter Notebooks
- [check.ipynb](check.ipynb): This is where we compile and train our DSPy programs.
- [eval.ipynb](eval.ipynb): Use this notebook to evaluate the performance of our DSPy programs.
- [jplag.ipynb](jplag.ipynb): Run this to calculate the JPlag benchmark.
- [analysis.ipynb](analysis.ipynb): This notebook contains all our plots and analysis of results.

### Python Scripts
- [dataloader.py](dataloader.py): Provides support for loading our research data.
- [models.py](models.py): Contains the model definitions for our DSPy programs.

### Data Directories
- `data/IR-Plag-Dataset/`: This directory contains our plagiarism dataset, sourced from [this GitHub repository](https://github.com/oscarkarnalim/sourcecodeplagiarismdataset/blob/master/IR-Plag-Dataset.zip).
- `data/jplag/`: Used for the JPlag benchmark calculations.
- `data/metadata/`: Stores metadata for our DSPy programs.
- `data/results/`: Where we save our research results.
- `data/train.tsv`: Our training dataset for DSPy.
- `programs/` : Contains DSPy programs.

## Citation

```
@INPROCEEDINGS{10852497,
  author={Brach, William and Košt’ál, Kristián and Ries, Michal},
  booktitle={2024 2nd International Conference on Foundation and Large Language Models (FLLM)}, 
  title={Can Large Language Model Detect Plagiarism in Source Code?}, 
  year={2024},
  volume={},
  number={},
  pages={370-377},
  keywords={Measurement;Computer languages;Codes;Accuracy;Reviews;Plagiarism;Large language models;Source coding;Education;Software development management;large language models;natural language processing;code similarity;code plagiarism},
  doi={10.1109/FLLM63129.2024.10852497}}

```


## Contact

William Brach - [@williambrach](https://x.com/williambrach) - william.brach@stuba.sk
