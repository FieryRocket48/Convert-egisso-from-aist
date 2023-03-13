# -*- coding: cp1251 -*-
# ���������� ����� �������� ����, ��� ���������� ������ � ����������. cp1251 ��� ��������� Windows(���������)
import csv

# ���� ������ ������ ���������� ������������� �����, ������� � �������� ����� ��������
ignore = ['RecType','LMSZID', 'categoryID','ONMSZCode','SNILS_reason','FamilyName_reason','Name_reason',
              'Gender_reason', 'BirthDate_reason','doctype_reason','doc_Series_reason','doc_Number_reason',
              'doc_IssueDate_reason','doc_Issuer_reason', 'criteria','FormCode','measuryCode', 'monetization',
              'content','comment','equivalentAmount']
# ��� ������� ������, ������� � �������� ������������ � ����������� �����������(�� ������������� �����)
dict_new = {'RecType': 'Fact', 'assignmentFactUuid': None, 'LMSZID': 'feac0762-4e58-4fbf-a7e9-5c3ec7c652b5',
            'categoryID': '4e0c92ae-a582-48ba-9dc9-90f65d9bcfcf', 'ONMSZCode': '6094.000001',
            'LMSZProviderCode': None, 'providerCode': None, 'SNILS_recip': None, 'FamilyName_recip': None, 'Name_recip': None,
            'Patronymic_recip': None, 'Gender_recip': None, 'BirthDate_recip': None, 'doctype_recip': None,
            'doc_Series_recip': None, 'doc_Number_recip': None, 'doc_IssueDate_recip': None, 'doc_Issuer_recip': None,
            'SNILS_reason': None, 'FamilyName_reason': None, 'Name_reason': None, 'Patronymic_reason': None,
            'Gender_reason': None, 'BirthDate_reason': None, 'kinshipTypeCode': None, 'doctype_reason': None,
            'doc_Series_reason': None, 'doc_Number_reason': None, 'doc_IssueDate_reason': None, 'doc_Issuer_reason': None,
            'decision_date': None, 'dateStart': None, 'dateFinish': None, 'usingSign': None, 'criteria': None,
            'criteriaCode': None, 'FormCode': str('01'), 'amount': None, 'measuryCode': '01', 'monetization': str('���'),
            'content': None, 'comment': None, 'equivalentAmount': None}

# ������ ������, ���� ������ ��� ��� ��������� ������
surname_donor = []

print("������� �������� ����� csv, ����������� �� ���� ����")
print("������: aist")
# �������� ����� ������� ���������� �������
Aist_file = input("�������� �����:")+str(".csv")
try:
    # ��������� ����������� ����
    with open(Aist_file, newline='') as file:
        # � delimiter ��������� �����������
        reader = csv.DictReader(file,   delimiter = ";", )
        # ������ ���� � ������� ����� ����������
        with open('EGISSO.csv','w',) as file_new:
            # ��������� ��������� ��� ����������� csv �����
            fieldnames = ['RecType','assignmentFactUuid','LMSZID','categoryID','ONMSZCode','LMSZProviderCode',
                          'providerCode','SNILS_recip','FamilyName_recip','Name_recip','Patronymic_recip','Gender_recip',
                          'BirthDate_recip','doctype_recip','doc_Series_recip','doc_Number_recip','doc_IssueDate_recip',
                          'doc_Issuer_recip','SNILS_reason','FamilyName_reason','Name_reason','Patronymic_reason',
                          'Gender_reason','BirthDate_reason','kinshipTypeCode','doctype_reason','doc_Series_reason',
                          'doc_Number_reason','doc_IssueDate_reason','doc_Issuer_reason','decision_date','dateStart',
                          'dateFinish','usingSign','criteria','criteriaCode','FormCode','amount','measuryCode','monetization',
                          'content','comment','equivalentAmount']
            # lineterminator - ����������� ������
            writer = csv.DictWriter(file_new,fieldnames=fieldnames, delimiter = ";",lineterminator="\n")
            # ���������� ��������� � csv ����
            writer.writeheader()
            # �������� ��������� ������ �� ������������� �����

            for line in reader:
                # �������� ������� - ��� ����� �������
                str_doc_Issuer_recip = line['doc_Issuer_recip']
                if (len(str_doc_Issuer_recip)) == 0:
                    print("����������� ����������, ��� ����� �������:")
                    surname_donor =  line['FamilyName_recip'] + "".join(' ') + line['Name_recip'] + "".join(' ') \
                                     + line['Patronymic_recip'] + "".join(' ') + line['BirthDate_recip']
                    print(surname_donor)
                    print()
                # �������� ������ �� ����� � ������� �������
                # ������� �� ������������� ����� ������ ����� (���������)
                for names in ignore:
                    del line[names]
                # ��������� ����� �����
                str_SNILS_recip = line['SNILS_recip']
                if len(str_SNILS_recip) == 10:
                    b = str('0')
                    b+=str_SNILS_recip
                    line['SNILS_recip'] = b
                # ��������� ����� ������ ��������
                str_doc_Number_recip = line['doc_Number_recip']
                if len(str_doc_Number_recip) == 5:
                    b = str('0')
                    b+=str_doc_Number_recip
                    line['doc_Number_recip'] = b
                # ��������� ����� ������ ��������
                if len(str_doc_Number_recip) == 4:
                    b = str('00')
                    b += str_doc_Number_recip
                    line['doc_Number_recip'] = b
                # ��������� ����� ����� ��������
                str_doc_Series_recip = line['doc_Series_recip']
                if (len(str_doc_Series_recip)) == 3:
                    b = str('0')
                    b+=str_doc_Series_recip
                    line['doc_Series_recip'] = b
                # ���������� ��������� ������� �� ������� ����������� �� ������������� �����
                a = {**dict_new, **line}
                # ���������� ������������ ������� � csv ����
                writer.writerow(a)


    # ��������� ������� �������� � ������ ������
    if len(surname_donor) > 0:
        print("��������� ������������ ������ ������(��)")
        input('')

except BaseException as errors:
    print(errors)
    input()
