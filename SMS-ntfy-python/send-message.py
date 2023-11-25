import requests
import json

res = requests.post("https://ntfy.sh/snews",
                    data="Hello ntfy~ 😀".encode(encoding='utf-8'))
print(res.status_code)
# !how cool is this!
requests.post("https://ntfy.sh/",
              data=json.dumps({
                  "topic": "snews",
                  "message": "Disk space is low at 5.1 GB,Hello ntfy~ 😀",
                  "title": "Low disk space alert",
                  #   "tags": ["warning", "cd"],
                  "priority": 4,
                  #   "attach": "https://filesrv.lan/space.jpg",
                  #   "filename": "diskspace.jpg",
                  "click": "https://homecamera.lan/xasds1h2xsSsa/",
                  #   "actions": [{"action": "view", "label": "Admin panel",
                  #   "url": "https://filesrv.lan/admin"}]
              })
              )
