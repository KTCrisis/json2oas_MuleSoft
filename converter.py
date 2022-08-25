
from matplotlib.font_manager import json_load
import sys
sample = json_load("sample.json")

string_line = "type: string"
number_line = "type: number"
boolean_line = "type: boolean"
array_line = "type: array"
array_object = """
items:
    type: object
    additionalProperties: false
    properties:
"""

with open('oas_sample.txt', 'w') as sys.stdout:
  for k,v in  sample.items():
      if type(v) == str:
          print("description : " + k)
          print(string_line)
          print('example: "' + str(v) + '"')
      elif type(v) == int or type(v) == float:
          print("description : " + k)
          print(number_line)
          print('example: "' + str(v) + '"')
      elif type(v) == type(True):
          print("description : " + k)
          print(boolean_line)
          print('example: "' + str(v) + '"')
      elif type(v) == list:
          for item in v :
              if type(item) == dict:
                  print("description : " + k)
                  print(array_line)
                  print(array_object)
                  for k2,v2 in v[0].items():
                      if type(v2) == str:
                          print("description : " + k2)
                          print(string_line)
                          print('example: "' + str(v2) + '"')
                      elif type(v2) == type(True):
                          print("description : " + k2)
                          print(boolean_line)
                          print('example: "' + str(v2) + '"')
                      elif type(v2) == int or type(v2)==float:
                          print("description : " + k2)
                          print(number_line)
                          print('example: "' + str(v2) + '"')
                      elif type(v2) == list:
                          print("description : " + k2)
                          print(array_line)

              elif type(item) == int or type(item) == str:
                  print("description : " + k2)
                  print(array_line)
