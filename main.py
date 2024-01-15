import schoolfilesystem

print("Welcome to the School File System")
print(schoolfilesystem.handleCSV('data.csv').generate_summary())

print(schoolfilesystem.handleExcel('data.xlsx').generate_summary())

print(schoolfilesystem.handleText('bible.txt').generate_summary())