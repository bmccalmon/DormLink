#!/usr/bin/env python3

import sys
sys.path.append("Dependencies")

import os
import git
import json

"""
This is the installer for applications.
Provided a remote repository URL, the installer will clone the repository to the "Apps" folder.
"""

apps_directory = "Apps"

def get_apps_to_download():
    """
    This returns a (hopefully) updated list of the endorsed applications available to download.
    """
    with open('apps_to_download.json', 'r') as json_file:
        apps_data = json.load(json_file)
    return apps_data

def download_app(repository_url):
    print(f"Downloading from {repository_url}...")
    
    app_name = repository_url.splot('/')[-1].replace('.git', '')
    git.Repo.clone_from(repository_url, os.path.join(apps_directory, app_name))

def main():
    apps = get_apps_to_download()
    download_app(apps[0]["download_link"])

if __name__ == "__main__":
    main()
