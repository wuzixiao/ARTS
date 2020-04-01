# 
import csv

class CSVEditor():
    def __init__(self):
        pass

    def edit(self, input_file, output_file, column_name, column_value, filters):
        with open(input_file, newline='') as input:
            reader = csv.DictReader(input, skipinitialspace=True)
            header = reader.fieldnames
            output_list = []
            for r in reader:
                r[column_name] = column_value
                output_list.append([i[1] for i in r.items()])
            
            with open(output_file, 'wt') as output:
                writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
                writer.writerow([','.join('"' + h + '"' for h in header)])
                writer.writerows(output_list)
            

if __name__ == '__main__':
    editor = CSVEditor()
    editor.edit("/Users/lxc/Documents/ARTS/Tips/test.csv", "/Users/lxc/Documents/ARTS/Tips/testout.csv", "column3", 0)