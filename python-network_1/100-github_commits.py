#!/usr/bin/python3
import requests
import sys

def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    commits = []
    page = 1
    while len(commits) < 10:
        response = requests.get(url, params={'page': page, 'per_page': 10})
        if response.status_code != 200:
            print("Failed to fetch data")
            return []
        
        data = response.json()
        if not data:  # No more commits available
            break

        for commit in data:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            commits.append(f"{sha}: {author_name}")
        
        page += 1  # Move to the next page if necessary

    return commits[:10]  # Ensure only the latest 10 commits are returned

def main():
    # Taking arguments from the command line
    if len(sys.argv) != 3:
        print("Usage: python 100-github_commits.py <repo> <owner>")
        sys.exit(1)
    
    repo = sys.argv[1]
    owner = sys.argv[2]
    
    commits = get_commits(repo, owner)
    
    if commits:
        for commit in commits:
            print(commit)

if __name__ == "__main__":
    main()

