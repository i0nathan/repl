from github import Github
from getpass import getpass

# First create a Github instance:

# using username and password
username = input("Github username: ")
password = getpass("Github password: ")

g = Github(username, password)

# Select a specific repo
# repo_name = input("Repo to download: ")

# or using an access token
# g = Github("access_token")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
        # print(repo.name)

# repo = g.get_user().get_repo(repo_name)
repo = g.get_repo("i0nathan/code_snippets")
# branch_or_tag_to_download = input("Branch or tag to download: ")
# sha = get_sha_for_tag(repo, branch_or_tag_to_download)

# directory_to_download = input("Directory to download: ")
# download_directory(repo, sha, directory_to_download)

contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        path = file_content.path
        content = repo.get_contents(path)
        file_data = content.content
        print(content)
        print(80*"-")
        print(file_data)

