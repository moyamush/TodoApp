# import requests, json

# def get_info(request):
#     url = "http://127.0.0.1:8000/api/user/"
#     print("request: ", request.user.password)
#     #requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
#     response = requests.get(url)
#     print("response: ",response)

#     #response.json()でJSONデータに変換して変数へ保存
#     # jsonData = response.json()
#     # print("jsonData: ", jsonData)

#     # task = jsonData["user_task"]
#     # return task