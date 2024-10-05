import requests

# Replace 'your_token' with your GitHub PAT
GITHUB_TOKEN = 'your_token'
GITHUB_USERNAME = 'your_username'


def get_repos(username, token):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def check_codeowners(repo, token):
    locations = ['CODEOWNERS', 'docs/CODEOWNERS', '.github/CODEOWNERS']
    headers = {'Authorization': f'token {token}'}
    for location in locations:
        url = f'https://api.github.com/repos/{repo}/contents/{location}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
    return False

def main():
    repos = get_repos(GITHUB_USERNAME, GITHUB_TOKEN)
    for repo in repos:
        repo_name = repo['full_name']
        if not check_codeowners(repo_name, GITHUB_TOKEN):
            print(f'No CODEOWNERS file in {repo_name}')
        else:
            print(f"{repo_name} has a CODEOWNERS file")

if __name__ == '__main__':
    main()
