import sys, os, glob

print(sys.platform)
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

#glob.glob() obtains list of filenames. Created filenames variable
filenames = glob.glob(pattern)
# for file in filenames:
#     print(file)

for file in filenames:
    if os.path.getsize(file) > 0:
        print(os.path.getsize(file))
        print(os.path.basename(file))





# TODO: Use the glob.glob() function to obtain the list of filenames

# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

