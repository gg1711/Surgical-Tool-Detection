import json

video_data = open("video.txt","r")
frame = video_data.readlines()
frames = []
tools = []
for i in frame:
    a = i.split()
    frames.append(a[0])
    tools.append(a[1:])
data_dic = dict(zip(frames, tools))
# print (data_dic)

data_file = open("data.txt","r")
frame_data = data_file.readlines()
for i in frame_data:
    data_str = str(i)
json_acceptable_string = data_str.replace("'", "\"")
d = json.loads(json_acceptable_string)
data_tools = []
for j in frames:
    data_tools.append([0,0,0,0,0,0,0])
a = 0
for j in frames:
    for k in d[j]:
        if k == "Grasper":
            data_tools[a][0] = "1"
        if k == "Bipolar":
            data_tools[a][1] = "1"
        if k == "Hook":
            data_tools[a][2] = "1"
        if k == "Scissors":
            data_tools[a][3] = "1"
        if k == "Clipper":
            data_tools[a][4] = "1"
        if k == "Irrigator":
            data_tools[a][5] = "1"
        if k == "SpecimenBag":
            data_tools[a][6] = "1"
        else:
            continue
    a = a+1
# print (data_tools)
tools_dic = dict(zip(frames, data_tools))
# print(tools_dic)
print (data_dic == tools_dic)    

