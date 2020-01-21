#json slice

import os
import json
from collections import OrderedDict
import xlwt 
from xlwt import Workbook

path_dir = 'C://Users//user//Desktop//openpose'#파일디렉토리지정
file_list = os.listdir(path_dir) #피험자 리스트
points = ['1','2','5','8','11']

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'X') 
sheet1.write(0, 1, 'Y') 
sheet1.write(0, 2, 'Confidence')

for i in file_list :#subject
    open_file = path_dir + '//' + i
    frame_list = os.listdir(open_file)
    
    for j in frame_list :#frame별 slice
        open_frame = open_file +'//' + j
        
        #딕셔너리를 통해 slice
        with open(open_frame, encoding="utf-8") as data_file : 
            data = json.load(data_file, object_pairs_hook=OrderedDict)
        
        for people, part_candidates in enumerate(data["part_candidates"]) :
            if people > 0 : print(", ", end="")
            
            #point_data 저장
            for point_num in points :#주요point
                for a in range(0,3) : #x,y,confi data 추출-slice
                    for cell in range(2,len(frame_list)+1):
                        point_x = part_candidates[point_num]
                        print(point_x)
                        point_x2 = point_x[a]
                        sheet1.write(cell,a+1,point_x2)

endpath='C://Users//user//Desktop//openpose/'+filename+'.xls'
wb.save(endpath) 
