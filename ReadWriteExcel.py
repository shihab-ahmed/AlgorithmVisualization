import pandas as pd
import xlsxwriter as xlWriter
import random

file = 'MRTK_Content.xlsx'
xl = pd.read_excel(file, sheet_name="Sheet1", header=0)


def main():
    wb = xlWriter.Workbook("Apple.xlsx")
    ws = wb.add_worksheet("Sheet1")
    xleys = xl.keys()
    print(xlKeys[0])

    ws.write("A1", str(row[0]))
    ws.write("B1", str(row[1]))
    ws.write("C1", str(row[2]))
    ws.write("D1", str(row[3]))
    ws.write("E1", str(row[4]))
    ws.write("F1", str(row[5]))
    ws.write("G1", str(row[6]))

    for index, row in xl.iterrows():
        """
        keyTopic = row["Topic\nトピック"]
        keySubcategory = row["Sub Category\nサブカテゴリー"]
        keySubcategory2 = row["Sub Category 2\nサブカテゴリー 2"]
        keySubcategory3 = row["Sub Category 3\nサブカテゴリー3"]
        keyContent = row["Content\nコンテンツ"]
        keyURL = row["URL"]
        print(str(index)+" "+str(row[6]) + str(len(row)))
       
       
        ws.write("A" + str(index + 1) , "str(row[0])")
        ws.write("B" + str(index + 1) , "str(row[1])")
        ws.write("C" + str(index + 1) , "str(row[2])")
        ws.write("D" + str(index + 1) , "str(row[3])")
        ws.write("E" + str(index + 1) , "str(row[4])")
        ws.write("F" + str(index + 1) , "str(row[5])")
        ws.write("G" + str(index + 1) , "str(row[6])")
        
        ws.write("A" + str(index + 1), str(row[0]))
        ws.write("B" + str(index + 1), str(row[1]))
        ws.write("C" + str(index + 1), str(row[2]))
        ws.write("D" + str(index + 1), str(row[3]))
        ws.write("E" + str(index + 1), str(row[4]))
        ws.write("F" + str(index + 1), str(row[5]))
        ws.write("G" + str(index + 1), str(row[6]))
        """
        #print(row[0])
    wb.close()

main()
"""
ws.write("A", str(index + 1) +)
ws.write("B", "Number Of Apple")
ws.write("C", "Type Of Tree")
ws.write("D", "ID")
ws.write("E", "Number Of Apple")
ws.write("F", "Type Of Tree")
"""
