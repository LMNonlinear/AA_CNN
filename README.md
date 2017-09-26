# Experiments with Convolutional Neural Networks for Multi-Label Authorship Attribution 

**Dainis Boumber** (dboumber@uh.edu),
**Yifan Zhang** (yzhang114@uh.edu),
**Arjun Mukherjee** (arjun@cs.uh.edu)

University of Houston

Publication pending review.
 
### Description

We explore the use of Convolutional Neural Networks (CNNs) for multi-label Authorship Attribution (AA) problems and propose a CNN specifically designed for such tasks.  By treating smaller documents as sentences and averaging the author probability distributions at sentence level for the longer documents, our design adapts to single-label datasets and various document sizes, retaining the capabilities of a traditional CNN. As a part of this work, we also create and make available to the public a multi-label Authorship Attribution dataset (ML Papers) , consisting of 400 scientific publications by 20 authors from the field of Machine Learning. Experimental results demonstrate that our method outperforms several state-of-the-art models on the proposed task. 

### Multi-label CNN

Prerequisits: `scikit-learn, tensoflow v1.0, python3` 

Run `python aa.py` for a sample set of experiments. 
Any additional data is to be placed under `datahelpers/data` (default, can be changed)

### ML Papers dataset

The data is located in `./ml_dataset` directory. You can also obtain it as a tarball from

`https://drive.google.com/open?id=0B_LjdXSWGw1YR2dIek95bGFfZEE`

`Labels.csv` contains the ground truths in the following format: <filename>,<author_1>,<author2>...<author_20>\n
 <filename> is plain text and <author_n> is a digit 0 or 1 indicating whether this author is one of the co-authors. The first row is the header row.

See (MLPA-400)[https://github.com/dainis-boumber/AA_CNN/wiki/MLPA-400-Dataset] for more details.




