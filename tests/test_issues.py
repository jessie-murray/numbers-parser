import pytest

from numbers_parser import Document, NumberCell

ISSUE_3_REF = [("A", "B"), (2.0, 0.0), (3.0, 1.0), (None, None)]
ISSUE_4_REF_1 = "Part 1 \n\nPart 2\n"
ISSUE_4_REF_2 = "\n\nPart 1 \n\n\nPart 2\n\n"
ISSUE_4_REF_3 = "今天是个好日子"
ISSUE_4_REF_4 = "Lorem ipsum\n\ndolor sit amet,\n\nconsectetur adipiscing"


def test_issue_3():
    doc = Document("tests/data/issue-3.numbers")
    sheets = doc.sheets()
    tables = sheets[0].tables()
    table = tables[0]
    ref = []
    for row in tables[0].iter_rows():
        ref.append(tuple([x.value for x in row]))
    assert ref == ISSUE_3_REF

    ref = []
    for row in tables[0].iter_rows(values_only=True):
        ref.append(row)
    assert ref == ISSUE_3_REF


def test_issue_4():
    doc = Document("tests/data/issue-4.numbers")
    sheets = doc.sheets()
    tables = sheets[0].tables()
    table = tables[0]
    assert table.cell(1, 0).value == ISSUE_4_REF_1
    assert table.cell(1, 1).value == ISSUE_4_REF_2
    assert table.cell(2, 0).value == ISSUE_4_REF_3
    assert table.cell(2, 1).value == ISSUE_4_REF_4
