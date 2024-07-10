#Code to generate a list of Excel column headers starting with A and Ending with ZZ and put them in a format I like.
#Author: Lucas Kowe
#generate a list of Excel column headers starting with A and Ending with ZZ
def ExcelColumns():
    columns = []
    for i in range(26):
        columns.append(chr(65+i))
    for i in range(26):
        for j in range(26):
            columns.append(chr(65+i)+chr(65+j))
    return columns

#Create a data structure that includes the above list and also includes the corresponding number for each column
def ExcelColumnsWithNumbers():
    columns = []
    for i in range(26):
        columns.append(chr(65+i))
    for i in range(26):
        for j in range(26):
            columns.append(chr(65+i)+chr(65+j))
    columnsWithNumbers = {}
    for i in range(len(columns)):
        columnsWithNumbers[columns[i]] = i+1
    return columnsWithNumbers

#Save the above data structure to a csv file with a column for the column header and a column for the corresponding number
#After every 26 Rows, start at the top again ajacent to the last column
def ExcelColumnsToCSV(csvFile):
    # Generate column headers
    columns = [chr(65+i) for i in range(26)] + [chr(65+i)+chr(65+j) for i in range(26) for j in range(26)]
        # Initialize rows
    rows = [[] for _ in range(26)]
        # Fill rows with column headers and numbers
    for index, column in enumerate(columns):
        colIndex = index // 26  # Calculate current CSV column index
        rowIndex = index % 26  # Calculate row index within current set of 26 rows 
        # Ensure there's enough space in the row for the new column
        while len(rows[rowIndex]) < colIndex * 2:
            rows[rowIndex].append("")  # Fill with empty strings for spacing   
        # Add column header and number
        rows[rowIndex].extend([column, str(index + 1)])
    # Write to CSV
    with open(csvFile, 'w', newline='') as f:
        for row in rows:
            f.write(','.join(row) + '\n')

print(ExcelColumns())
print(ExcelColumnsWithNumbers())
ExcelColumnsToCSV("ExcelColumns.csv")