"""
Define some page labels in a PDF.
Check success in various aspects.
"""
import fitz


def make_doc():
    doc = fitz.open()
    for i in range(10):
        page = doc.new_page()
    return doc


def make_labels():
    return [
        {"startpage": 0, "prefix": "A-", "style": "D", "firstpagenum": 1},
        {"startpage": 4, "prefix": "", "style": "R", "firstpagenum": 1},
    ]


def test_setlabels():
    doc = make_doc()
    doc.set_page_labels(make_labels())
    page_labels = [p.get_label() for p in doc]
    answer = ["A-1", "A-2", "A-3", "A-4", "I", "II", "III", "IV", "V", "VI"]
    assert page_labels == answer
    assert doc.get_page_numbers("V") == [8]
    assert doc.get_page_labels() == make_labels()
