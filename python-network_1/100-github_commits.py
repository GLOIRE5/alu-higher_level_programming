#!/usr/bin/python3
import requests
import sys

def get_commits(repo_name, owner_name):
  """Fetches and prints 10 commits from a GitHub repository.

  Args:
    repo_name: The name of the repository.
    owner_name: The owner of the repository.
  """
  url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
  headers = {'Accept': 'application/json'}
  params = {'per_page': 10}

  response = requests.get(url, headers=headers, params=params)
  response.raise_for_status()

  for commit in response.json():
    sha = commit['sha']
    author_name = commit['commit']['author']['name']
    print(f"{sha}: {author_name}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python 100-github_commits.py <repo_name> <owner_name>")
    sys.exit(1)

  repo_name = sys.argv[1]
  owner_name = sys.argv[2]

  get_commits(repo_name, owner_name)
