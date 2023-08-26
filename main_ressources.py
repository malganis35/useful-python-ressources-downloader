#!/usr/bin/env python #
"""
Main script to load ressources

author: caotrido
"""

#%% Load the package
import pandas as pd
import os
import git 

#%% General functions

# Clone or update all the repo
def update_ressource(lst_ressource):
    """function to update the ressources, 
    either by cloning or just fetch/rebase if exist

    Args:
        lst_ressource (list): list of git repo on github or gitlab
    """
    print("--------------------------------------------------------")
    print("--> Update the ressources")
    
    for url in lst_ressource: 
        
        print("Testing url :" + url)
        folderName = url.rsplit('/', 1)[-1]
        
        print("Corresponding local folder: " + folderName) 
        if os.path.isdir(folderName):
            print("Folder exist. Making git fetch and git rebase")
            g = git.cmd.Git("./" + folderName)
            g.fetch()
            g.rebase()
            print("Fetch and rebase done")
        else:
            print("Cloning the repo")
            git.Repo.clone_from(url, './' + folderName)
            print("Cloning done")


def list_all_directories():
    """list of repositories within the current folder without .git/ folder

    Returns:
        lst_subdirectories(list): list of repositories within the current folder
    """
    
    print("--------------------------------------------------------")
    print("--> List all the directories")
    
    # Initiate the list
    lst_subdirectories = []

    # Loop to check if element is a directory and add it to the list
    for item in os.listdir():
        if os.path.isdir(item):
            lst_subdirectories.append(item)

    # print the subdirectories
    print(lst_subdirectories)

    # Delete .git from the list
    print("Removing .git/ folder")
    lst_subdirectories.remove(".git") 
    
    print(lst_subdirectories)
    
    return lst_subdirectories


def update_gitignore(subdirectories):
    """Update the .gitignore if a folder present in subdirectories
    does not exist

    Args:
        subdirectories (list): list of directories to check
    """
    
    print("--------------------------------------------------------")
    print("--> Update the .gitignore if necessary")
    
    gitignore_path = '.gitignore'

    # Load .gitignore
    with open(gitignore_path, 'r') as f:
        gitignore_content = f.read()

    # Loop the folder and check if present
    for subdirectory in subdirectories:
        print("Testing directory: " + subdirectory)
        if subdirectory not in gitignore_content:
            print("Folder does not exist. Adding to .gitignore")
             # Add folder to .gitignore
            gitignore_content += f'\n{subdirectory}/'
        else:
            print("Folder exist. Continue")

    # Update .gitignore with the content
    with open(gitignore_path, 'w') as f:
        f.write(gitignore_content)

#%% Main file

# Load the data
lst_ressource = pd.read_csv("./ressources.txt", header=None)[0].to_list()

# Update the ressources folder
update_ressource(lst_ressource)

# List all the directories in the current folder
lst_subdirectories = list_all_directories()

# Update the .gitignore
update_gitignore(lst_subdirectories)
