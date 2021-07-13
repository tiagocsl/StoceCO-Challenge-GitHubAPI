class Sorters():
    def sort_by_stars(s):
        return s["stargazers_count"]

    def sort_by_comments(s):
        return s["comments"]    

    def sort_by_number(s):
        return s["number"]

class Returns_JSONs():
    return_value_popular_repo = [
            {  
            "id": 100977374,
            "repository_name": "boleto-api",
            "description":"API for register and generate Boletos",
            "url": "https://api.github.com/repos/gabrielclima/boleto-api",
            "stargazers_count": 3
            },{  
            "id": 91150326,
            "repository_name": "bellatrix-rest-api",
            "description":"REST API Getting started for Rust Language",
            "url": "https://api.github.com/repos/gabrielclima/bellatrix-rest-api",
            "stargazers_count": 0
            },{  
            "id": 112373683,
            "repository_name": "alfred",
            "description":"A PDF Reporter API",
            "url": "https://api.github.com/repos/gabrielclima/alfred",
            "stargazers_count": 4
            }
        ]
    
    return_value_popular_issue = [{  
            "id": 982715673,
            "number": 5,
            "repo_url": "https://api.github.com/repos/gabrielclima/alfred/issues/5",
            "title": "Qual framework ?",
            "body":"Qual framework pretende usar nessa api ?",
            "state": "open",
            "comments": 3
        },{  
            "id": 278335673,
            "number": 2,
            "repo_url": "https://api.github.com/repos/gabrielclima/alfred/issues/2",
            "title": "Qual linguagem ?",
            "body":"Qual linguagem pretende codar essa api ?",
            "state": "open",
            "comments": 7
        },{  
            "id": 578462673,
            "number": 1,
            "url": "https://api.github.com/repos/gabrielclima/alfred/issues/1",
            "title": "Qual ambiente ?",
            "body":"Qual ambiente pretende rodar essa api ?",
            "state": "open",
            "comments": 1
        }]
    
    return_value_uninteracted_pull = [
        {  
            "id": 1184208,
            "number": 25,
            "url": "https://api.github.com/repos/guilhermecstro/solid-alura/pulls/25",
            "title": "UninteractedPR test",
            "state": "close",
            "comments": 13,
            "reviews": 0
        },{  
            "id": 1397968,
            "number": 26,
            "url": "https://api.github.com/repos/guilhermecstro/solid-alura/pulls/26",
            "title": "UninteractedPR test",
            "state": "open",
            "comments": 0,
            "reviews": 2
        },{  
            "id": 2846073,
            "number": 31,
            "url": "https://api.github.com/repos/guilhermecstro/solid-alura/pulls/31",
            "title": "UninteractedPR test",
            "state": "close",
            "comments": 0,
            "reviews": 0
        },{  
            "id": 538935460,
            "number": 48,
            "url": "https://api.github.com/repos/guilhermecstro/solid-alura/pulls/48",
            "title": "UninteractedPR test",
            "state": "open",
            "comments": 0,
            "reviews": 0
        },{  
            "id": 436135460,
            "number": 51,
            "url": "https://api.github.com/repos/guilhermecstro/solid-alura/pulls/51",
            "title": "UninteractedPR test",
            "state": "open",
            "comments": 3,
            "reviews": 1
        },{  
            "id": 436135460,
            "number": 65,
            "url": "https://api.github.com/repos/guilhermecstro/solid-alura/pulls/65",
            "title": "UninteractedPR test",
            "state": "open",
            "comments": 0,
            "reviews": 0
        }]