#== urls.py ==#

BASE_URL = 'https://api.github.com'


#== user urls ==#
USERS_URL = BASE_URL + '/users/{0}'

USER_HTML_URL = 'https://github.com/users/{0}'

SELF_URL = f'{BASE_URL}/user'

USER_REPOS_URL = f'{USERS_URL}/repos'

USER_ORGS_URL = f'{USERS_URL}/orgs'

USER_GISTS_URL = f'{USERS_URL}/gists'

USER_FOLLOWERS_URL = f'{USERS_URL}/followers'

USER_FOLLOWING_URL = f'{USERS_URL}/following'


#== repo urls ==#
CREATE_REPO_URL = f'{BASE_URL}/user/repos'

REPOS_URL = BASE_URL + '/repos/{0}' # repos of a user

REPO_URL = BASE_URL + '/repos/{0}/{1}' # a specific repo

REPO_ISSUE_URL = REPO_URL + '/issues/{2}' # a specific issue

#== gist urls ==#
GIST_URL = BASE_URL + '/gists/{0}' # specific gist

CREATE_GIST_URL = f'{BASE_URL}/gists'

#== org urls ==#
ORG_URL = BASE_URL + '/orgs/{0}'