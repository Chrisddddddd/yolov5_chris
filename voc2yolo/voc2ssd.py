#----------------------------------------------------------------------#
#   楠岃瘉闆嗙殑鍒掑垎鍦╰rain.py浠ｇ爜閲岄潰杩涜
#   test.txt鍜寁al.txt閲岄潰娌℃湁鍐呭鏄甯哥殑銆傝缁冧笉浼氫娇鐢ㄥ埌銆�
#----------------------------------------------------------------------#
'''
#--------------------------------娉ㄦ剰----------------------------------#
濡傛灉鍦╬ycharm涓繍琛屾椂鎻愮ず锛�
FileNotFoundError: [WinError 3] 绯荤粺鎵句笉鍒版寚瀹氱殑璺緞銆�: './VOCdevkit/VOC2007/Annotations'
杩欐槸pycharm杩愯鐩綍鐨勯棶棰橈紝鏈�绠�鍗曠殑鏂规硶鏄皢璇ユ枃浠跺鍒跺埌鏍圭洰褰曞悗杩愯銆�
鍙互鏌ヨ涓�涓嬬浉瀵圭洰褰曞拰鏍圭洰褰曠殑姒傚康銆傚湪VSCODE涓病鏈夎繖涓棶棰樸��
#--------------------------------娉ㄦ剰----------------------------------#
'''
import os
import random 
random.seed(0)

xmlfilepath=r'Annotations'
saveBasePath=r"ImageSets\Main"
 
#----------------------------------------------------------------------#
#   鎯宠澧炲姞娴嬭瘯闆嗕慨鏀箃rainval_percent
#   train_percent涓嶉渶瑕佷慨鏀�
#----------------------------------------------------------------------#
trainval_percent=1
train_percent=1

temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

num=len(total_xml)  
list=range(num)  
tv=int(num*trainval_percent)  
tr=int(tv*train_percent)  
trainval= random.sample(list,tv)  
train=random.sample(trainval,tr)  
 
print("train and val size",tv)
print("traub suze",tr)
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')  
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')  
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')  
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')  
 
for i  in list:  
    name=total_xml[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
