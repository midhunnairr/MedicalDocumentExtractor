import pytesseract
import re
from Backend.src.parser_generic import MedicalDocParser


class Patient(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        patient_info = {
            "patient_name": self.get_patient_info("patient_name"),
            "contact_number": self.get_patient_info("contact_number"),
            "vaccination_status": self.get_patient_info("vaccination_status"),
            "medical_issues": self.get_patient_info("medical_issues")
        }
        return patient_info

    def get_patient_info(self,field_name):
        pattern_dict = {
            "patient_name": {
                "pattern": "Date(.*?)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)",
                "flags": re.DOTALL
            },
            "contact_number": {
                "pattern": r"(\(\d{3}\).*)Weight",
                "flags": re.DOTALL
            },
            "vaccination_status": {
                "pattern": r"vaccination\?.*?(Yes|No)",
                "flags": re.DOTALL
            },
            "medical_issues": {
                "pattern": r"headaches.:(.*)Name",
                "flags": re.DOTALL
            }
        }
        dict_object = pattern_dict[field_name]
        content = re.findall(dict_object["pattern"], self.text, flags=dict_object["flags"])
        if content:
            if field_name == "patient_name":
                return content[0][0].strip()
            else:
                return content[0].strip().replace("\n", " ")
        else:
            return None



inp = '''Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020


_—

Name of Insurance Company:
Random Insuarance Company

Policy Number:
5638746258

Do you have medical insurance?

_ Yes

Medical Insurance Details

List any allergies:
N/A

List any medication taken regularly:

N/A

4218 Smeeler Ridge Dr
Buffalo, New York, 14206
United States

Expiry Date:
31 December 2020

'''

# o = Patient(inp)
# print(o.parse())
