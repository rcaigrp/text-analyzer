import pytest
import os

def test_criterion_1_module_import():
    import text_analyzer
    assert text_analyzer is not None

def test_criterion_2_analyze_text_returns_dict():
    import text_analyzer
    result = text_analyzer.analyze_text("hello world hello")
    assert isinstance(result, dict)

def test_criterion_3_get_keywords_returns_list():
    import text_analyzer
    result = text_analyzer.get_keywords("hello world hello", n=1)
    assert isinstance(result, list)

def test_criterion_4_save_report_writes_file():
    import text_analyzer
    result = text_analyzer.analyze_text("hello world hello")
    text_analyzer.save_report(result, "/tmp/test_report.txt")
    assert os.path.exists("/tmp/test_report.txt")
