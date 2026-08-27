import csv

def read_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)

read_csv("data/csv1.csv")
# ['id', 'first_name', 'last_name', 'email', 'department', 'salary', 'start_date', 'is_active']
# ['1', 'Maya', 'Chen', 'maya.chen@example.com', 'Engineering', '118000', '2019-03-11', 'True']
# ...


def read_csv2(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        print(reader.fieldnames)

        for row in reader:
            print(row["first_name"], row["department"])

read_csv2("data/csv1.csv")
# ['id', 'first_name', 'last_name', 'email', 'department', 'salary', 'start_date', 'is_active']
# Maya Engineering
# Omar Engineering
# Priya Design
# ...
#
# DictReader omits the first title row -> becomes dict keys


def write_csv1(path):
    rows = [
        {"name": "Maya", "dept": "Engineering", "salary": 118000},
        {"name": "Omar", "dept": "Sales", "salary": 88000},
    ]
    with open(path, "w", newline='') as csvfile:
        # writer = csv.DictWriter(csvfile, fieldnames=["first_name", "department", "salary_level"])
        
        writer = csv.DictWriter(csvfile, fieldnames=["name", "dept", "salary"])
        writer.writeheader()
        writer.writerows(rows)

write_csv1("data/csv2.csv")
#   line 220, in _dict_to_list
#     raise ValueError("dict contains fields not in fieldnames: "
#                      + ", ".join([repr(x) for x in wrong_fields]))
#
# writer fieldnames and row field names must match

# write_csv1("data/csv2.csv")     second call
# name,dept,salary
# Maya,Engineering,118000
# Omar,Sales,88000
#
# ^ writted to csv2.csv
