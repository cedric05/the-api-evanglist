This collections allows you to backup your Postman collections to GitHub. It only backs up one collection at a time, but due to API limits on Postman and GitHub, it makes sense to execute and schedule as monitors one by one.

To use you will need a Postman environment with the following variables:

- github_token - A valid GitHub token, you can issue at https://github.com/settings/tokens.
- github_user - The GitHub user or organizatiobn you wish to be writing data to.
- github_repo - The public or private GitHub repository you wish to be writing data to.
- postman_api_key - Your Postman API key which you can find under your account settings.

If you have any questions you can tweet at @apievangelist, or [submit an issue on the GitHub issues for all of the capbilities I am developing](https://github.com/api-evangelist/capabilities).