from github import Github
from getpass import getpass
import base64
import os

def main():
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

    # branch_or_tag_to_download = input("Branch or tag to download: ")  # 'master'
    branch_or_tag_to_download = "master"
    sha = get_sha_for_tag(repo, branch_or_tag_to_download)

    server_path = "Python/Flask_Blog/12-Error-Pages"

    os.makedirs(server_path)
    download_directory(repo, sha, server_path)

    # directory_to_download = input("Directory to download: ")

def get_sha_for_tag(repository, tag):
    """
    Returns a commit PyGithub object for the specified repository and tag.
    """
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]
    if matched_branches:
        return matched_branches[0].commit.sha

    tags = repository.get_tags()
    matched_tags = [match for match in tags if match.name == tag]
    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha


def download_directory(repository, sha, server_path):
    """
    Download all contents at server_path with commit tag sha in
    the repository.
    """
    contents = repository.get_contents(server_path, ref=sha)

    for content in contents:
        print("Processing %s" % content.path)
        if content.type == 'dir':
            os.makedirs(content.path)
            download_directory(repository, sha, content.path)
        else:
            try:
                path = content.path
                file_content = repository.get_contents(path, ref=sha)
                file_data = base64.b64decode(file_content.content).decode("utf-8")
                with open(content.path, "w") as file:
                    file.write(file_data)
                # file_out = open(content.path, "w")
                # file_out.write(file_data)
                # file_out.close()
            except (GithubException, IOError) as exc:
                logging.error('Error processing %s: %s', content.path, exc)


if __name__ == '__main__':
    main()
