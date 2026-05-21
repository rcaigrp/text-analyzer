import re
from collections import Counter

def analyze_text(text):
    tokens = re.findall(r'\b\w+', text.lower())
    return dict(Counter(tokens))

def get_keywords(text, n=5):
    freq = analyze_text(text)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[:n]

def save_report(frequencies, filename='report.txt'):
    with open(filename, 'w') as f:
        for word, count in frequencies.items():
            f.write(f'{word}: {count}\n')
