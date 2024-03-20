import os
import subprocess

def gitOperations(directory):
    cwd = os.getcwd()
    os.chdir(directory)
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Automated commit by autocommit.py'])
    subprocess.run(['git', 'push'])

def requirementOperations(directory):
    os.chdir(directory)
    subprocess.run(['pip', 'freeze'], stdout=open('requirements.txt', 'w'))

if __name__ == "__main__":
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    directories = [d for d in os.listdir('.') if os.path.isdir(d)]
    if directories:
        for index, directory in enumerate(directories):
            if directory == "Config":
                print("Extracted requirements.txt")
                requirementOperations(directory)
            else:
                print(f"Processing repo {index + 1}/{len(directories)-1}: {directory}")
                gitOperations(directory)
            print("Done.")
            os.chdir(parent_dir)
    else:
        print("No directories found.")
