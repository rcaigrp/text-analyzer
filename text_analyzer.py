import re
from collections import Counter

def analyze_text(text):
    words = re.findall(r'\w+', text.lower())
    return dict(Counter(words))

def get_keywords(freq_dict, n=10):
    return dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:n])

def save_report(freq_dict, filename='report.txt'):
    with open(filename, 'w') as f:
        f.write("Word Frequency Report\n")
        for word, count in freq_dict.items():
            f.write(f"{word}: {count}\n")
