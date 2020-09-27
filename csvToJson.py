import csv
import json
from copy import deepcopy

def makeJsonSample(row, length): ## Simple function for making Json Instance
    sample =  '{'
    for count in range(length):
        sample += '"'+ row[count] +'":' + '""'
        if(count == len(row)-1):
          sample+= '}'
        else:
          sample+=','
    return sample

def convertCsvToJson(fileFrom, fileTo, num_lim = None):
  with open(fileFrom, 'r') as file:
    reader = csv.reader(file)
    row1 = next(reader)  # gets the first line
    # data =  '{ "id":"", "premise":, "hypothesis":""}'
    length = len(row1) # gets length of first line  
    res = makeJsonSample(row1,length) # create Json Instance
    jsonSample = json.loads(res) # loads as Json Object
    # print(jsonSample)
    arr = []
    for row in reader:
      jsonSampleCopy = deepcopy(jsonSample) # Make copy of Json Instance
      for j in range(length):
        jsonSampleCopy[row1[j]] = row[j] 
      print(jsonSampleCopy,end='\n') ##For Testing and see input in colab uncomment
      arr.append(jsonSampleCopy)
      if(num_lim != None):
        if(reader.line_num == num_lim):
          break

    with open(fileTo,'w+') as json_file:
        json.dump(arr,json_file)
    json_file.close()
  file.close()

csvFile = "train.csv"
jsonFile = "newJsonFile1.json"
num_lim = 10 ##For Testing and see input in colab uncomment it and if condition below 

convertCsvToJson(csvFile, jsonFile, num_lim)
