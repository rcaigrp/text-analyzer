import pytest
import os
from text_analyzer import analyze_text, get_keywords, save_report

def test_criterion_1_module_exists():
    import text_analyzer

def test_criterion_2_analyze_text():
    result = analyze_text("the cat sat on the mat")
    assert isinstance(result, dict)
    assert 'cat' in result

def test_criterion_3_get_keywords():
    freq = {'a': 5, 'b': 2, 'c': 8}
    result = get_keywords(freq, 2)
    assert list(result.keys()) == ['c', 'a']

def test_criterion_4_save_report():
    freq = {'a': 1}
    save_report(freq, 'test_report.txt')
    assert os.path.exists('test_report.txt')
    os.remove('test_report.txt')
