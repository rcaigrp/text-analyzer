import os
import pytest
import text_analyzer

def test_criterion_1_module_import():
    import text_analyzer
    assert text_analyzer is not None

def test_criterion_2_analyze_text():
    text = "hello world hello python"
    result = text_analyzer.analyze_text(text)
    assert isinstance(result, dict)
    assert "hello" in result
    assert result["hello"] == 2

def test_criterion_3_get_keywords():
    text = "apple banana apple pear banana apple"
    result = text_analyzer.get_keywords(text, n=2)
    assert len(result) == 2
    assert result[0] == ("apple", 3)

def test_criterion_4_save_report():
    freq = {"test": 1}
    filename = "/workspace/projects/text_analyzer/report.txt"
    text_analyzer.save_report(freq, filename)
    assert os.path.exists(filename)
    with open(filename, "r") as f:
        content = f.read()
        assert "test" in content
