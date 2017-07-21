# AA_CNN
Two channel depth-wise CNN for multi-label Authorship Attribution problems

### Authors: 

**Dainis Boumber** (dboumber@uh.edu),
**Yifan Zhang** (yzhang114@uh.edu),
**Arjun Mukherjee** (arjun@cs.uh.edu)

University of Houston

Natural Language Processing Laboratory,
Pattern Analysis Laboratory
 

### Description

This is a project to address Multi-Label real-world authorship problems. We contribute:
1. A CNN designed for the task 
2. A large, multi-label, real-world scenario corpus that can be used in Authorship Attribution, Verification, Identification and Plagiarism Detection problems.

### Paper

Currently under review.

### Code

Needs `scikit-learn, tensoflow v1.0, python3` 

Run `python aa.py` for a sample set of experiments. 
Any additional data is to be placed under `datahelpers/data` (you can of course edit that) 

### Dataset

Machine Learning Papers (MLPapers) has been collected as follow:
1. We have collected top 20 publications by top 20 scholars accroding to Google Scholar. 
2. The PDF documents were converted to txt format, encoded in unicode.
3. All documents have been stripped of title and author names, as well as reference lists
4. `Labels.csv` file has been generated which contains the ground truths in the following format: <filename>,<author_1>,<author2>...<author_20>\n
 <filename> is plain text and <author_n> is a digit 0 or 1 indicating whether this author is one of the co-authors. The first row is the header row.

It is located in `./ml_dataset` directory. You can also obtain it as a tarball from

`https://drive.google.com/open?id=0B_LjdXSWGw1YR2dIek95bGFfZEE`



