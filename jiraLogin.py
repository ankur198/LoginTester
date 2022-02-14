from jira import JIRA

def tryJira(host, port, username, password):   
    try:
        url = f'{host}:{port}'
        JIRA(url, auth=(username, password))
        return True
    except Exception as e:
        return False