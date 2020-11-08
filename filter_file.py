#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is used to filter a text file.
It's reading each line and if there is no occurences I do not want
then it writes the line in a file.
It's using a comprehensive list.
"""


def main():
    open('entrouvert_git_repo_list_filtered.txt', 'w').writelines(
        [line for line in open("entrouvert_git_repo_list.txt")
         if '/tree/' not in line and '/log/' not in line]
        )


if __name__ == "__main__":
    main()
