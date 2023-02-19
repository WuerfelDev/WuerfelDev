#!/usr/bin/env python3
import configparser
import json
import urllib.request

conf = configparser.ConfigParser()
conf.read("config.ini")
config = conf["CONFIG"]

# Api reference: https://docs.gitlab.com/ee/api/projects.html#list-user-projects
url = "https://gitlab.com/api/v4/users/" + config["username"] + "/projects?order_by=last_activity_at&per_page=100"
pixel = "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="

with urllib.request.urlopen(url) as r:
    repos = json.loads(r.read())


table = "|| Project | Description\n---|---|---\n"
for repo in repos:
    avatar = "<a href='" + repo["web_url"] + "'><img src='" + (repo["avatar_url"] or pixel) + "' height='48'></a>"
    name = "<a href='" + repo["web_url"] + "'>" + repo["name"] + "</a>"
    description = repo["description"] or ""
    table += avatar + "|" + name + "|" + description + "\n"


with open('README.md','w') as f:
    f.write("# " + config["title"] + "\n")
    f.write(config["intro"] + "\n\n")
    f.write(table)
    f.write("\n<br>" + config["outro"])
