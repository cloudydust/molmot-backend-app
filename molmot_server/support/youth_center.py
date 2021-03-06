from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



URL = f"https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?_csrf=d852c94c-4a08-449a-925f-fc961f296287&bizId=&chargerOrgCdAll=&dtlOpenYn=Y&frameYn=&pageIndex=1&pageUnit=12&plcyTpOpenTy=&srchAge=&srchEdubg=012008&srchEmpStatus=006001"
#https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?_csrf=d852c94c-4a08-449a-925f-fc961f296287&bizId=&chargerOrgCdAll=&dtlOpenYn=Y&frameYn=&pageIndex=2&pageUnit=12&plcyTpOpenTy=list_004003&srchAge=&srchEdubg=012008&srchEmpStatus=006006&srchSortOrder=2&srchSpecField=007006&srchTermMm=1&srchWord=&trgtJynEmp=&trgtJynEmp=#
#https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?_csrf=d852c94c-4a08-449a-925f-fc961f296287&bizId=&chargerOrgCdAll=&dtlOpenYn=Y&frameYn=&pageIndex=2&pageUnit=12&plcyTpOpenTy=list_004003&srchAge=&srchEdubg=012008&srchEmpStatus=006006&srchSortOrder=2&srchSpecField=007006&srchTermMm=1&srchWord=&trgtJynEmp=&trgtJynEmp=#

def get_today_info() :
    website = requests.get(URL)
    soup = BeautifulSoup(website.text,"html.parser")
   

    chrome_options = Options()
    chrome_options.add_argument( '--headless' )
    chrome_options.add_argument( '--log-level=3' )
    chrome_options.add_argument( '--disable-logging' )
    chrome_options.add_argument( '--no-sandbox' )
    chrome_options.add_argument( '--disable-gpu' )
    
    driver = webdriver.Chrome('/Users/heejeong/gitkraken/molmot-backend-app/molmot_server/chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(3)
    driver.get( URL )

    driver.execute_script("fn_move(6);")
    driver.implicitly_wait(2)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    notice=soup.find("div",class_="sch-result-wrap compare-result-list")
    print(notice)
    notice=notice.find("div",class_="result-list-box")
    location=soup.find("div",class_="badge").get_text()
    try:
        location=soup.find("span",class_="grey-label").get_text()
    except:
        pass
    for i in notice.find("ul").find_all('li'):
        supports_list=i.find("a")["id"][8:]
    
        jv_script="f_Detail('"+supports_list+"');"
        print(jv_script)
        query={
            "openApiVlak":"167693bf2984bec5368623af",
            "display":1,
            "pageIndex":1
        }
        query['srchPolicyId']=supports_list
        dict2_type=get_youth_center(query)
        support_dict=dict2_type['empsInfo']['emp']
        support_serializers=OpenapiSupportSerializer(data=support_dict, many=isinstance(dict2_type,list))
        print(support_serializers.data)
        #driver.execute_script(jv_script)
    
    

    
    #driver.execute_script("f_Detail('R2022012501406')")
    #html = driver.page_source
    #print(html)
    
    #for i in range(1, 10):
    #    print("Current page is {0}".format(i))
    #    driver.execute_script("f_Detail({0})".format(i))



#

# #srchFrm > div.sch-result-wrap.compare-result-list//*[@id="srchFrm"]/div[4]/div[2]/ul
get_today_info()
