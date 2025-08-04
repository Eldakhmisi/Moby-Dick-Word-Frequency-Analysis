# Import and download packages
import requests
import nltk
from bs4 import BeautifulSoup
from collections import Counter
from nltk.tokenize import RegexpTokenizer

# Download stopwords from NLTK
nltk.download('stopwords')

# Step 0: Fetch HTML
URL = "https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm"
r = requests.get(url=URL)
html = r.text

# Step 1: Parse HTML and get text
html_soup = BeautifulSoup(html, 'html.parser')
moby_text = html_soup.get_text()

# Step 2: Initialize RegexpTokenizer to keep only alphanumeric text
tokenizer = RegexpTokenizer(r'\w+')

# Step 3: Tokenize the text
tokens = tokenizer.tokenize(moby_text)
words = [token.lower() for token in tokens]

# Step 4: Exclude stopwords
stop_words = nltk.corpus.stopwords.words('english')
words_no_stop = [word for word in words if word not in stop_words]

# Step 5: Count top 10 words
count = Counter(words_no_stop)
top_ten = count.most_common(10)

# Step 6: Print result
print(top_ten)
