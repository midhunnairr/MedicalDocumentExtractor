from .parser_generic import MedicalDocParser
import re


class Prescription(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return{
            "patient_name": self.get_field('patient_name'),
            "patient_address": self.get_field('patient_address'),
            "patient_medicines": self.get_field('patient_medicines'),
            "directions": self.get_field('directions'),
            "refills": self.get_field('refills')
        }

    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {'pattern': "Name:(.*)Date", 'flags': 0},
            "patient_address": {'pattern': "Address:(.*)\n", 'flags': 0},
            "patient_medicines": {'pattern': "Address[^\n]*(.*)Directions",'flags': re.DOTALL},
            "directions": {'pattern': "Directions:(.*)Refill", 'flags': re.DOTALL},
            "refills": {'pattern': "Refill:(.*)", 'flags': 0}
        }
        pattern_obj = pattern_dict.get(field_name)
        result = re.findall(pattern_obj['pattern'], self.text, flags=pattern_obj['flags'])

        if result:
            return result[0].strip().replace("\n", " ")
        else:
            return None


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

