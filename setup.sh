#!/bin/bash

# linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	# if ,git exsist
    if [[ -d ".git" ]]; then
        cp ./pre-commit-hook/pre-commit .git/hooks/
        chmod +x .git/hooks/pre-commit
    # if .git does not exsist
    else
        echo "Directory \".git\" does not exists. Please setup git repo before running \"npm run setup\""
        exit 1
    fi
# Mac OSX
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # if ,git exsist
    if [[ -d ".git" ]]; then
        cp ./pre-commit-hook/pre-commit .git/hooks/
        chmod +x .git/hooks/pre-commit
    # if .git does not exsist
    else
        echo "Directory \".git\" does not exists. Please setup git repo before running \"npm run setup\""
        exit 1
    fi
# POSIX compatibility layer and Linux environment emulation for Windows
elif [[ "$OSTYPE" == "cygwin" ]]; then
    # if ,git exsist
    if [[ -d ".git" ]]; then
        cp ./pre-commit-hook/pre-commit .git/hooks/
        chmod +x .git/hooks/pre-commit
    # if .git does not exsist
    else
        echo "Directory \".git\" does not exists. Please setup git repo before running \"npm run setup\""
        exit 1
    fi
# Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
elif [[ "$OSTYPE" == "msys" ]]; then
    # if ,git exsist
    if [[ -d ".git" ]]; then
        cp ./pre-commit-hook/pre-commit .git/hooks/
        chmod +x .git/hooks/pre-commit
    # if .git does not exsist
    else
        echo "Directory \".git\" does not exists. Please setup git repo before running \"npm run setup\""
        exit 1
    fi
# I am guessing windows is this
elif [[ "$OSTYPE" == "win32" ]]; then
    # if ,git exsist
    if [[ -d ".git" ]]; then
        cp .\pre-commit-hook\pre-commit .git\hooks\
        chmod +x .git\hooks\pre-commit
    # if .git does not exsist
    else
        echo "Directory \".git\" does not exists. Please setup git repo before running \"npm run setup\""
        exit 1
    fi
else
        echo 'i dont know your version'
fi