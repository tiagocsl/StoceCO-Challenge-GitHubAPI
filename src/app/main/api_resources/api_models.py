from flask_restx import fields
from main.api_resources.api_namespaces import api_v1 

# -------------------------- #
# Modelos de payloads da API #
# -------------------------- #


# Modelos api v1 
# ------------------------
most_popular_repo = api_v1.model("Popular Repository", {
                    'user': fields.String(required = True, description = 'Name of user to find repository')
})

most_popular_issue = api_v1.model("Popular Issue", {
                    'fullname_repo': fields.String(requiered = True, description = 'Full name of repository to find issue')
})

uninteracte_pull_request = api_v1.model("Uninteracted Pull Request", {
                    'fullname_repo': fields.String(requiered = True, description = 'Full name of repository to find pull request')
})

copy_and_delete_comment = api_v1.model("Copy and Delete the Original Comment", {
                    'fst_fullname_repo': fields.String(requiered = True, description = 'Full name of first repo to find comment'),
                    'fst_pr_number': fields.String(required = True, description = 'Number of the pull request to find comment'),
                    'fst_comment_id': fields.String(required = True, description = 'Id of comment to copy and delete'),
                    'snd_fullname_repo': fields.String(required = True, description = 'Full name of second repo to find comment'),
                    'snd_pr_number': fields.String(required = True, description = 'Number of the pull request to past a comment')
})

create_or_overwrite_gitignore = api_v1.model("Create or overwrite gitignore file", {
                    'fullname_repo': fields.String(requiered = True, description = 'Full name of the repository to create the gitignore'),
                    'author': fields.String(requiered = True, description = 'Author name of commit')
})



# --------------------------- #
# Modelos de responses da API #
# --------------------------- #


# Modelos api v1 
# ------------------------
most_popular_repo_reponse = {200: 'OK',
                             404: 'An error ocurred in your request!'}

most_popular_issue_reponse = {200: 'OK',
                              404: 'An error ocurred in your request!'}

uninteracte_pull_request_reponse = {200: 'OK',
                                    404: 'An error ocurred in your request!'}

copy_and_delete_comment_reponse = {201: 'The original comment has been successfully replicated and deleted!',
                                   404: 'An error ocurred in your request!'}

create_or_overwrite_gitignore_reponse = {201: 'The GitIgnore file was created or overwritten successfully!',
                                         404: 'An error ocurred in your request!'}