import re

# potential_phone_numbers = [
#  "dwdwd +33(0)6.80.33.12.26 r4iwedwed",
#  "dwdwd +33176340034dwdwd ",
#  "dwdwd +590 590 94-9604",
#  "01 86 91 99 08dwdwd ",
#  "0682249025 dwdwd ",
#  "dwdwd 514-929-1550", # 1
#  "de 07 68 58 02 88de",
#  "0650432466",
#  "+351 289 009 580"
# ]
# potential_email = "CREATIVR@GMAIL.COM"

# for number in potential_phone_numbers:
#  # phone_regex = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
#  phone_regex = "[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]"
#  is_found = re.findall(phone_regex, number)
#  print(is_found if is_found else None)

# email_regex = "^[^\s@]+@[^\s@]+\.[^\s@]+$"
# is_found = re.findall(email_regex, potential_email)
# print(is_found if is_found else None)
# number_list = []
# def words_in_string(a_string):
#  return a_string in number_list

# numbers = ['3.20.4-2020-06-06', '143-2052900-4361113', '143-2052900-4361113', '0.211997.0', '000-0000000-8675309', '382725310951', '382725310951', '382725310951', '382725310951', '7904561453', '40797412560', '4957431987', '3.20.4-2020-06-06', '3.20.4-2020-06-06', '3.20.4-2020-06-06', '0980392) 3', '201909240029', '201909240029', '201909240029', '1072964635', '9781072964636', '1072964635', '9781072964636', '202004072104', '202004072104', '202004072104', '143-2052900-4361113', '143-2052900-4361113', '(4294967295', '1072964635', '1072964635', '1072964635', '1072964635', '2676882011', '1072964635', '15529609011', '2238192011', '16115931011', '12766669011', '1-888-283-1678', '16857165011', '17853655011', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '465632727431967', '1072964635', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '0.6676300578034682', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '201111161604', '201111161604', '201111161604', '201111161604', '201111161604', '201111161604', '201111161604', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '1000493771', '201111161604', '201111161604', '201111161604', '202004072104', '202004072104', '202004072104', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1591801305', '1000464931', '1000844301', '1000426311', '1072964635', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '143-2052900-4361113', '1072964635', '1072964635', '978-1072964636', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '2.0.1460.0', '2.0.1460.0', '2.0.1460.0', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '1591801305', '143-2052900-4361113', '143-2052900-4361113', '2676882011', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '2676882011', '143-2052900-4361113', '1072964635', '1072964635', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '2102313011', '18190131011', '16218619011', '10232440011', '1072964635', '1072964635', '1072964635', '15547130011', '14498690011', '1591801304259', '1591801304259', '1591801304259', '1591801304259', '143-2052900-4361113', '1072964635', '1072964635', '143-2052900-4361113']
# for number in numbers:
#  total_count = len(number.replace("[-\(\)\+\. ]+", ""))
#  if total_count > 9 and total_count < 12:
#   if(number not in number_list): number_list.append(number)

# print(number_list)

# Phone, tel: , t: , mobile
















source_code = """
Call 0661543485dede dewde
"""
# phone_regex = "\+[\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]" # Priority 1
phone_regex = "((tel|p|t|phone|call|dial|ring)[: -]?[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])" # Priority 2
# phone_regex = "[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]" # Priority 3
# email_regex = "[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
is_found = re.findall(phone_regex, source_code, re.IGNORECASE)
print(is_found)

# for number in potential_phone_numbers:
#  # phone_regex = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
#  phone_regex = "[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]"
#  is_found = re.findall(phone_regex, number)
#  print(is_found if is_found else None)

# email_regex = "^[^\s@]+@[^\s@]+\.[^\s@]+$"
# is_found = re.findall(email_regex, potential_email)
# print(is_found if is_found else None)
# number_list = []
# def words_in_string(a_string):
#  return a_string in number_list

# numbers = ['3.20.4-2020-06-06', '143-2052900-4361113', '143-2052900-4361113', '0.211997.0', '000-0000000-8675309', '382725310951', '382725310951', '382725310951', '382725310951', '7904561453', '40797412560', '4957431987', '3.20.4-2020-06-06', '3.20.4-2020-06-06', '3.20.4-2020-06-06', '0980392) 3', '201909240029', '201909240029', '201909240029', '1072964635', '9781072964636', '1072964635', '9781072964636', '202004072104', '202004072104', '202004072104', '143-2052900-4361113', '143-2052900-4361113', '(4294967295', '1072964635', '1072964635', '1072964635', '1072964635', '2676882011', '1072964635', '15529609011', '2238192011', '16115931011', '12766669011', '1-888-283-1678', '16857165011', '17853655011', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '465632727431967', '1072964635', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '0.6676300578034682', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '201111161604', '201111161604', '201111161604', '201111161604', '201111161604', '201111161604', '201111161604', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '1000493771', '201111161604', '201111161604', '201111161604', '202004072104', '202004072104', '202004072104', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1591801305', '1000464931', '1000844301', '1000426311', '1072964635', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '143-2052900-4361113', '1072964635', '1072964635', '978-1072964636', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '1072964635', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '2.0.1460.0', '2.0.1460.0', '2.0.1460.0', '143-2052900-4361113', '143-2052900-4361113', '1072964635', '1591801305', '143-2052900-4361113', '143-2052900-4361113', '2676882011', '143-2052900-4361113', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '1072964635', '2676882011', '143-2052900-4361113', '1072964635', '1072964635', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '143-2052900-4361113', '2102313011', '18190131011', '16218619011', '10232440011', '1072964635', '1072964635', '1072964635', '15547130011', '14498690011', '1591801304259', '1591801304259', '1591801304259', '1591801304259', '143-2052900-4361113', '1072964635', '1072964635', '143-2052900-4361113']
# for number in numbers:
#  total_count = len(number.replace("[-\(\)\+\. ]+", ""))
#  if total_count > 9 and total_count < 12:
#   if(number not in number_list): number_list.append(number)
