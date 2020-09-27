# CsvToJson

You can read any csv file and export as json file but first line of csv file have to be headers.

**Functions:**


1.   makeJsonSample(row, length)


***row*** - First line of CSV file ( Headers) - STRING


***length*** - Count of Header names - Number
2.   convertCsvToJson(fileFrom, fileTo, num_lim = None)


***fileFrom*** - It is CSV file name. - STRING 


***fileTo*** - It is output name ( JSON name) - STRING 


***num_lim*** - Optional variable. You can use for testing ( If you don't want to see all data ) - Number

I used https://jsonchecker.com/ to check validity of JSON.
I tested it data with 10,100,600,1000 and more. 

You can see detailed explanation at the collab - https://colab.research.google.com/drive/1j1IHpcHdNQi1OrwdtTWeNbkaP6a-53_r?usp=sharing
