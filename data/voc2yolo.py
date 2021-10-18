#----------------------------------------------------------------------#
#   濡ょ姴鐭侀惁澶愭⒖閸℃瑦鐣遍柛鎺撳笒閸ㄥ酣宕烽埡鐨塧in.py濞寸媴绲块悥婊堟煂瀹�鍕〃閺夆晜绋栭、锟�
#   test.txt闁告粌鐦塧l.txt闂佹彃鐭傚鏉库柦閳╁啯绠掗柛鎰噹椤旀劙寮伴娑卞妧閻㈩垰鎽滃▓鎴﹀Υ閸屾繍鍞茬紓浣稿暕缁楀瀵煎顐⑩枏闁烩偓鍔岄崺宀勫Υ閿燂拷
#----------------------------------------------------------------------#
'''
#--------------------------------婵炲鍔嶉崜锟�----------------------------------#
濠碘�冲�归悘澶愬捶閳虹憟charm濞戞搩鍙�缁诲秶鎮扮仦鐐槯闁圭粯鍔楅妵姘舵晬閿燂拷
FileNotFoundError: [WinError 3] 缂侇垵宕电划娲箥閸欍儳鐟濋柛鎺斿鐎垫氨锟借姘ㄥ▓鎴犳崉椤栨氨绐為柕鍡嫹: './VOCdevkit/VOC2007/Annotations'
閺夆晜鐟﹀Σ绔漼charm閺夆晜鍔橀、鎴︽儎椤旇偐绉块柣銊ュ濡埖锛愬鍫㈢闁哄牞鎷风紒鐙呮嫹闁告娲滃▓鎴﹀棘鐟欏嫮銆婇柡鍕靛灠閻ㄣ垻鎷犻妷锔界�ù鐘烘硾椤︽煡宕氱捄鍝勭厒闁哄秴婀卞ú鎷屻亹閺囩偞鍊甸弶鈺傚姌椤㈡垿濡撮敓锟�
闁告瑯鍨禍鎺楀蓟閵夘煈鍤勫☉鎿勬嫹濞戞挸顑囧ù澶岋拷闈涙贡濞叉媽銇愰弴鐐村闁哄秴婀卞ú鎷屻亹閺囩姵鐣辨慨鎺戝�告惔鐑藉Υ閸屾碍韬琕SCODE濞戞搩鍘介惀鍛村嫉婢跺海绠瑰☉鎿冧邯濡埖锛愬Ο闈╂嫹閿燂拷
#--------------------------------婵炲鍔嶉崜锟�----------------------------------#
'''
import os
import random 
random.seed(0)

xmlfilepath=r'E:/DATASET/VOCdevkit/VOC2007/Annotations'
saveBasePath=r"E:/DATASET/VOCdevkit/VOC2007/ImageSets/Main"
 
#----------------------------------------------------------------------#
#   闁诡垰鐤囬々锔芥櫠閻愭彃顫ｆ繛鏉戭儓閻︻垶姊块崱鏇熷弿闁猴拷缁犲児ainval_percent
#   train_percent濞戞挸绉瑰〒鍓佹啺娴ｉ攱鍙忛柡锟介敓锟�
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
