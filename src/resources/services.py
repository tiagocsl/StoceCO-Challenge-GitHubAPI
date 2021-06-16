import requests as req
import json
from src.resources.utils import Sorters

GitHubAPI = "https://api.github.com"

def mostPopularRepo(user):
    repositories = req.get(GitHubAPI + '/users/' + user + '/repos?per_page=100')
    popularRepository = repositories.json()
    popularRepository.sort(key=Sorters.sortByStars, reverse=True)

    if repositories.status_code == 200:
        return popularRepository[0]
    if repositories.status_code == 404:
        return "An error ocurred in your request!"

def mostCommentedIssue(user, repo):
    mostCommented = []
    issue = req.get(GitHubAPI + '/repos/'+ user +'/' + repo + '/issues')
    parsedIssues = issue.json()

    for openIssues in parsedIssues:
        if openIssues['state'] == "open":
            mostCommented.append(openIssues)

    mostCommented.sort(key=Sorters.sortByComments, reverse=True)
    print(mostCommented)

    if issue.status_code == 200:
        if mostCommented == []:
            return "There are no open issues!"
        else:
            return mostCommented[0]
    if issue.status_code == 404:
        return "An error ocurred in your request!"

def uninteractedPull(user, repo):
    uninteractedPRs = []
    pullRequests = req.get(GitHubAPI +'/repos/'+ user +'/' + repo + '/pulls')
    parsedPullReqs = pullRequests.json()    
    
    for openPR in parsedPullReqs:
        if openPR["state"] == "open":
            unreviewedPR = req.get(GitHubAPI + '/repos/' + user + '/' + repo + '/pulls/' + str(openPR["number"]) + '/reviews').json()
            if unreviewedPR == []:
                uncommentedPR = req.get(openPR['url']).json()
                if uncommentedPR['comments'] == 0:
                    uninteractedPRs.append(uncommentedPR)
    
    uninteractedPRs.sort(key=Sorters.sortByNumber)
    
    if pullRequests.status_code == 200:
        if uninteractedPRs == []:
            return "There are no open pull requests that have not been interacted!"
        else:
            return uninteractedPRs[0]
    
    if pullRequests.status_code == 404:
        return "An error ocurred in your request!" 