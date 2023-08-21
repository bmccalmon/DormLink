#!/usr/bin/env python3

import sys
sys.path.append("Dependencies")

import os
import git

"""
This is the updater for the DormLink Home screen and all of its applications.
It uses GitHub to check for updates and clone repositories.
Any project within the 'Apps' folder will be checked for updates.
"""

apps_directory = "Apps"

def update_repo(repository_path):
    print(f"### Updating {repository_path} ###")

    repo = git.Repo(repository_path)
    current_branch = repo.active_branch
    repo.remotes.origin.fetch()
    remote_branch = repo.remotes.origin.refs[current_branch.name]

    remote_commit_hash = remote_branch.commit.hexsha
    local_commit_hash = current_branch.commit.hexsha

    if local_commit_hash != remote_commit_hash:
        print("Update found! Updating...")

    print(f"{repository_path} is up-to-date.")

def update_apps():
    # Update the main DormLink repository
    update_main_repository = True
    if update_main_repository:
        update_repo('.')

    # Update the installed apps
    for app in os.listdir(apps_directory):
        app_path = os.path.join(apps_directory, app)
        if os.path.isdir(app_path):
            update_repo(app_path)

def main():
    update_apps()

if __name__ == "__main__":
    main()
