#json slice

import os
import json
from collections import OrderedDict
import xlwt 
from xlwt import Workbook

joint = {'r_shoulder' : ['1','2','3'], 'r_elbow' : ['2','3','4'], 'l_shoulder' : ['1','5','6'], 'l_elbow' : ['5','6','7']}

for njoint in joint:
    print(joint[njoint])

path_dir = 'C://Users//Administrator//Desktop//openpose/openpose_json'#파일디렉토리지정
file_list = os.listdir(path_dir) #피험자 리스트
print(file_list)


for i in file_list :#subject
    open_file = path_dir + '/' + i
    open_file = str(open_file)
    frame_list = os.listdir(open_file)
    
    for j in frame_list :#frame별 slice
        open_frame = open_file +'/' + j
        
        #딕셔너리를 통해 slice
        with open(open_frame, encoding="utf-8") as data_file : 
            data = json.load(data_file, object_pairs_hook=OrderedDict)
        
        for people, part_candidates in enumerate(data["part_candidates"]) :
            if people > 0 : print(", ", end="")
            
            #point_data 저장
            for njoint in joint :#주요point
                for a in range(0,3) : #x,y,confi data 추출-slice
                    print(a)
