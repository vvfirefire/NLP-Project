##### All the commands here are already included inside the submitted ipynb notebook file, here is only for clarification purpose

# Quick Setup the environment 
1. Python 3.6
2. Install environment 
```ruby
pip install -r requirements.txt
```
3. Download necessary word embeddings (GloVe, ELMo and Cove)
```ruby
sh download.sh
```
4. Download the en module for spacy
```ruby
python -m spacy download en
```
# Train the model on SQuAD 2.0 Dataset
1. Data preprocessing
```ruby
python preprocess.py
```
2. Train the model
```ruby
python train.py
```
