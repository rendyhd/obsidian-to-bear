import fileinput, glob, os, pathlib, shutil, sys 

# I've always ran this script in the same directory as the "Notes" directory 
# where I've copied my Obsidian Vault to

folder = 'Notes'

# function to move all files to root folder by https://stackoverflow.com/a/39952370
def move_to_root_folder(root_path, cur_path):
    for filename in os.listdir(cur_path):
        if os.path.isfile(os.path.join(cur_path, filename)):
            shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
        elif os.path.isdir(os.path.join(cur_path, filename)):
            move_to_root_folder(root_path, os.path.join(cur_path, filename))
        else:
            sys.exit("Should never reach here.")
    # remove empty folders
    if cur_path != root_path:
        os.rmdir(cur_path)

        
for filepath in pathlib.Path('Notes').glob('**/*'):
    file = filepath.absolute()
    rel_file = filepath.relative_to('Notes')
    only_path = os.path.dirname(rel_file)
    if str(file).endswith('.md'):
        print('processing file > '+str(file))
        tag = str(only_path).replace(" ", "").replace(".","-")
        
        metadata = '\n\n#'+tag
        with open(file, 'r') as original: data = original.read()
        data = data.replace('![[','![](').replace(']]',')')
        with open(file, 'w') as modified: modified.write(data + metadata)

move_to_root_folder('Notes', 'Notes')
