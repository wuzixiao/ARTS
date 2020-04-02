# 
import csv

class CSVEditor():
    def __init__(self):
        pass

    def edit(self, input_file, output_file, column_name, column_value, dict_filters):
        with open(input_file, newline='') as input:
            reader = csv.DictReader(input, skipinitialspace=True)
            header = reader.fieldnames
            output_list = []
            for r in reader:
                pass_filter = True
                for filter in dict_filters:
                    if r.get(filter) != dict_filters.get(filter):
                        pass_filter = False
                        break
                # only update the columns that pass filters
                if pass_filter:
                    r[column_name] = column_value
                output_list.append([i[1] for i in r.items()])
            
            with open(output_file, 'wt') as output:
                writer = csv.writer(output, quoting=csv.QUOTE_NONE,escapechar=' ')
                writer.writerow([','.join('"' + h + '"' for h in header)])
                writer.writerows(output_list)
            

if __name__ == '__main__':
    editor = CSVEditor()
    filters = {'column1':'def'}
    editor.edit("/Users/lxc/Documents/ARTS/Tips/test.csv", "/Users/lxc/Documents/ARTS/Tips/testout.csv", "column3", 0, filters)