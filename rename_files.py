import os

def rename_files_in_directory(directory):
    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        # Construct full file path
        old_file_path = os.path.join(directory, filename)
        
        # Skip directories, only rename files
        if os.path.isfile(old_file_path):
            # Replace spaces with underscores in the filename
            new_filename = filename.replace(" ", "_")
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Specify the directory containing the files you want to rename
directory_path = '/Users/eacalder/Documents/brewster/financials'
rename_files_in_directory(directory_path)
