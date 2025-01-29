import os

def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in '{directory}': {files}")
        return files
    except FileNotFoundError:
        print(f"The directory {directory} does not exist")
    except PermissionError:
        print(f"Permission denied to list files in {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"The file {old_name} does not exist")
    except PermissionError:
        print(f"Permission denied to rename {old_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage
# old_name = 'old_file.txt'
# new_name = 'new_file.txt'
# rename_file(old_name, new_name)

# Example usage
directory = 'F:/Profile/somnath3112.github.io/_portfolio/'
all_files = list_files_in_directory(directory)
portfolio_files = [file for file in all_files if file.startswith('portfolio')]
no_of_portfolio_files = len(portfolio_files)

new_file_ID = int(input("\n\nCreate a portfolio file using ID [0 to reset names]: "))

# Sort the names 
for pf_id, file in enumerate(reversed(portfolio_files)): 
    file_path = os.path.join(directory, file)
    sorted_file_path = os.path.join(directory, 'portfolio-' + str(no_of_portfolio_files - pf_id) + '.md')
    rename_file(file_path, sorted_file_path)
    
# Rename the files to insert a new one 
if new_file_ID>=1:
    for pf_id in range(no_of_portfolio_files, new_file_ID-1, -1):
        old_file_path = os.path.join(directory, 'portfolio-' + str(pf_id) + '.md')
        new_file_path = os.path.join(directory, 'portfolio-' + str(pf_id + 1) + '.md')
        rename_file(old_file_path, new_file_path)

    new_file_path = os.path.join(directory, 'portfolio-' + str(new_file_ID) + '.md')
    try:
        with open(new_file_path, 'w') as new_file:
            new_file.write(
            "---"
            + "\ntitle: \"Enter a title.\""
            + "\nexcerpt: \"About the project.<br/><img src='/images/sample.png' style='width:500px;height:500px;'>\""
            + "\ncollection: portfolio"
            + "\n---"
            + "\n"
            + "\nDescription of the project."
            )
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")