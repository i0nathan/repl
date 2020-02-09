
from github import Github

import getpass

username = input("Github username: ")
password = getpass.getpass("Github password: ")

github = Github(username, password)

organization = github.get_user().get_orgs()[0]

repository_name = input("Github repository: ")
repository = organization.get_repo(repository_name)

branch_or_tag_to_download = input("Branch or tag to download: ")
sha = get_sha_for_tag(repository, branch_or_tag_to_download)

directory_to_download = input("Directory to download: ")
download_directory(repository, sha, directory_to_download)


def get_sha_for_tag(repository, tag):
    """
    Returns a comit PyGithub object for the specified repository and tag.
    """
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]
    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha


def download_directory(repository, sha, server_path):
    """
    Download all contents at server_path with commit tag sha in the
    repository.
    """
    contents = repository.get_dir_contents(server_path, ref=sha)

    for content in contents:
        print("Processing %s" % content.path)
        if content.type =='dir':
            download_directory(repository, sha, content.path)
        else:
            try:
                path = content.path
                file_content = repository.get_contents(path, ref=sha)
                file_data = base64.b64decode(file_content.content)
                file_out = open(content.name, "w")
                file_out.write(file_data)
                file_out.close()
            except (GithubException, IOError) as exc:
                logging.error("Error processing %s: %s", content.path, exc)


