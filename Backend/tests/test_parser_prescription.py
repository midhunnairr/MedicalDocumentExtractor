from Backend.src.parser_prescription import Prescription
import pytest


@pytest.fixture()
def doc_maria():
    input1 = '''Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    K

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mig every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times'''

    return Prescription(input1)


@pytest.fixture()
def doc_vk():
    input1 = '''Dr John >mith, M.D
            2 Non-Important street,
            New York, Phone (900)-323- ~2222
            Name:  Virat Kohli Date: 2/05/2022
            Address: 2 cricket blvd, New Delhi
            | Omeprazole 40 mg
            Directions: Use two tablets daily for three months
            Refill: 3 times'''

    return Prescription(input1)


@pytest.fixture()
def doc_empty():
    return Prescription('')


def test_get_name(doc_maria, doc_vk, doc_empty):
    assert doc_maria.get_field("patient_name") == "Marta Sharapova"
    assert doc_vk.get_field("patient_name") == "Virat Kohli"
    assert  doc_empty.get_field("patient_name") == None


def test_get_address(doc_maria, doc_vk, doc_empty):
    assert doc_maria.get_field("patient_address") == "9 tennis court, new Russia, DC"
    assert doc_vk.get_field("patient_address") == "2 cricket blvd, New Delhi"
    assert doc_empty.get_field("patient_address") == None

def test_get_medicine(doc_maria, doc_vk, doc_empty):
    assert doc_maria.get_field("patient_medicines") == '''K      Prednisone 20 mg     Lialda 2.4 gram'''
    assert doc_vk.get_field("patient_medicines") == "| Omeprazole 40 mg"
    assert doc_empty.get_field("patient_medicines") == None

def test_get_directions(doc_maria, doc_vk, doc_empty):
    assert doc_vk.get_field("directions") == "Use two tablets daily for three months"
    assert doc_maria.get_field("directions") == '''Prednisone, Taper 5 mig every 3 days,     Finish in 2.5 weeks a     Lialda - take 2 pill everyday for 1 month'''
    assert doc_empty.get_field("directions") == None

def test_get_refills(doc_maria, doc_vk, doc_empty):
    assert doc_vk.get_field("refills") == "3 times"
    assert doc_maria.get_field("refills") == "2 times"
    assert doc_empty.get_field("refills") == None

def test_parse(doc_vk, doc_maria, doc_empty):

    vk = doc_vk.parse()
    assert vk == {
        "patient_name": "Virat Kohli",
        "patient_address": "2 cricket blvd, New Delhi",
        "patient_medicines": "| Omeprazole 40 mg",
        "directions": "Use two tablets daily for three months",
        "refills": "3 times"
    }

    maria = doc_maria.parse()
    assert maria == {
        "patient_name": "Marta Sharapova",
        "patient_address": "9 tennis court, new Russia, DC",
        "patient_medicines": "K      Prednisone 20 mg     Lialda 2.4 gram",
        "directions": "Prednisone, Taper 5 mig every 3 days,     Finish in 2.5 weeks a     Lialda - take 2 pill everyday for 1 month",
        "refills": "2 times"
    }

    empty = doc_empty.parse()
    assert empty == {
        "patient_name": None,
        "patient_address": None,
        "patient_medicines": None,
        "directions": None,
        "refills": None
    }
