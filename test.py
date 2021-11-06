import json
#テスト用のファイル
#map=open(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\map.json")
with open(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\map.json") as f:
    map=f.read()
    
map=json.loads(map, strict=False)
print(map)
print(type(map))
#print(map["x0y0"])
#map.close()
