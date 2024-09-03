import streamlit as st,os,shutil,datetime
from emailapp.Unzip import UnzipOfd,zipofdfile
from emailapp.Imboxapp import downloadmail
from emailapp.ReNameFOD import renameofd
from emailapp.ofd2pdf import multiofd2pdf
from emailapp.mergePDFbyorder import Mergepdf
from emailapp.config import *



def front():
        st.title('Tkt & Itinerary Query System')
        st.write('-'*60)

def clearDir(ofdpath):
    if os.path.exists(ofdpath):
        shutil.rmtree(ofdpath)
        os.makedirs(ofdpath)
    else:
        os.makedirs(ofdpath)

def UploadFiles(ofdpath:str) -> bool:
    fileNo=0
    if files:=st.file_uploader('上传OFD文件',['ofd','zip','rar'],accept_multiple_files=True,):
        clearDir(ofdpath)
        for file in files:
            fileNo += 1 
            if file.name[-3:] in ['zip','rar'] :
                UnzipOfd(file,ofdpath)
            else:    
                with open(os.path.join(ofdpath,file.name),'wb') as f:
                    f.write(file.getvalue())
        
        return True


if __name__=='__main__':
    front()

    st.map()

html_temp = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>地图单击拾取经纬度</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <style>
    body,
    html,
    #container {
        overflow: hidden;
        width: 100%;
        height: 100%;
        margin: 0;
        font-family: "微软雅黑";
    }
    </style>
    <script src="//api.map.baidu.com/api?type=webgl&v=1.0&ak=你的秘钥"></script>
</head>
<body>
    <div id="container"></div>
</body>
</html>
<script>
var map = new BMapGL.Map('container');
map.centerAndZoom(new BMapGL.Point(122.09281887930774, 37.54103421694607), 15);
map.enableScrollWheelZoom(true);
map.addEventListener('click', function (e) {
    alert('点击位置经纬度：' + e.latlng.lng + ',' + e.latlng.lat);
});
</script>
"""
# html_component = st.components.v1.html(html_temp, height=600)

# 显示经纬度
# if html_component:
    # st.write(f"点击位置经纬度: {html_component}")


# with st.sidebar:
#     with st.expander('设置'):
#         # st.write('shezhei')
#         pass

# mailsender=st.text_input('只收取以下发件人的当天邮件，多人用逗号隔开：','eip@travelsky.com')
# senderlst=mailsender.replace('，',',').replace(' ','').split(',')

# if st.button('批量下载邮件！'):
#     with st.spinner('正在收取附件...',):
#         attno = downloadmail(ofdpath,senderlst)  
#         st.write('下载完毕！共收到{attno}个OFD文件！')
#     renameofd()
#     zipfilename = zipofdfile(renamed_ofdpath)
    
#     st.download_button('下载打包文件',open(zipfilename,'rb'),'zippedofd.zip',mime='zip')    
    
# # with st.empty():
# #     for seconds in range(60):
# #         st.write(f"⏳ 已过去 {seconds} 秒")
# #         time.sleep(1)
# #     st.write("✔️ 1 分钟结束！")