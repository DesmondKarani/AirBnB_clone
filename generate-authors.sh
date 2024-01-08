#!/bin/bash

# File: generate-authors.sh

AUTHORS_FILE="AUTHORS"

# Generating AUTHORS file
echo "# File @generated by generate-authors.sh. DO NOT EDIT." > $AUTHORS_FILE
echo "# This file lists all contributors to the repository." >> $AUTHORS_FILE
echo "# See generate-authors.sh to make modifications." >> $AUTHORS_FILE
echo "" >> $AUTHORS_FILE

git log --format='%aN <%aE>' | sort -u >> $AUTHORS_FILE
