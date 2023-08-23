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
    """
    Given a specific repo, this updates it if it isn't already up-to-date.
    Returns True if there was an update found, False otherwise
    """
    #nonlocal n_updates

    print(f"### Updating {repository_path} ###")

    repo = git.Repo(repository_path)
    current_branch = repo.active_branch
    repo.remotes.origin.fetch()
    remote_branch = repo.remotes.origin.refs[current_branch.name]

    remote_commit_hash = remote_branch.commit.hexsha
    local_commit_hash = current_branch.commit.hexsha

    update_found = False
    if local_commit_hash != remote_commit_hash:
        update_found = True
        print("Update found! Updating...")
        repo.remotes.origin.pull()

    print(f"{repository_path} is up-to-date.")
    return update_found

def update_apps():
    """
    This updates DormLink and ALL of the installed apps if they aren't already up-to-date.
    Returns the number of apps updated.
    """
    #nonlocal n_updates
    #n_updates = 0

    # Update the main DormLink repository
    update_main_repository = True
    if update_main_repository:
        update_repo('.')

    n_updates = 0
    # Update the installed apps
    for app in os.listdir(apps_directory):
        app_path = os.path.join(apps_directory, app)
        if os.path.isdir(app_path):
            if update_repo(app_path) == True:
                n_updates += 1

    print(f"{n_updates} apps updated.")

    return n_updates

def main():
    update_apps()

if __name__ == "__main__":
    main()
