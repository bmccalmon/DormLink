#!/usr/bin/env python3

import json

"""
This is the installer for applications.
Provided a remote repository URL, the installer will clone the repository to the "Apps" folder.
"""

def get_apps_to_download():
    """
    This returns a (hopefully) updated list of the endorsed applications available to download.
    """
    with open('apps_to_download.json', 'r') as json_file:
        apps_data = json.load(json_file)
    return apps_data

def main():
    print(str(get_apps_to_download()))

if __name__ == "__main__":
    main()
