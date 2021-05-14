def news2(list):

    import requests
    import json
    url=("http://newsapi.org/v2/top-headlines?country=in&apiKey=89ea07d3dbd4423bb2a72120069c1453")
    response=requests.get(url).text
    my_json=json.loads(response)
    for i in range(3):
        list.append((f"the No.{i+1} news title is"))
        list.append((my_json["articles"][i]["title"]))
        list.append((f"the No. {i+1} news  is"))
        list.append((my_json["articles"][i]["description"]))
        list.append(my_json["articles"][i]["description"])
    return list
l=[]
news2(l)
