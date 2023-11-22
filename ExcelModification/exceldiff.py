import pandas as pd
#file1 -> file which you use
file1 = pd.read_excel('fistExcel.xlsx', sheet_name=None)
#file2 -> file which comes with config gen tool
file2 = pd.read_excel('SecondExcel.xlsx' , sheet_name=None)
diff_dict = {}
for sheet_name in file1.keys():
    df1 = file1[sheet_name]
    df2 = file2[sheet_name]
    diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
    if not diff.empty:

        print(f"Differences in sheet '{sheet_name}':")
        print(diff)
        diff_dict[sheet_name] = diff

# Save the differences to a new Excel file
with pd.ExcelWriter('differences.xlsx') as writer:
    for sheet_name, diff in diff_dict.items():
        diff.to_excel(writer, sheet_name=sheet_name, index=False)