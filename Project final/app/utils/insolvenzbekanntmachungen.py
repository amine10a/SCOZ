from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

def get_dates_between(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
    dates_between = []
    current_date = start_date
    while current_date <= end_date:
        dates_between.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    return dates_between

def converttoHtml(url,datem,dateM,mot):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    dr=webdriver.Chrome(options=chrome_options)
    dr.get(url)
    element = dr.find_element(by='id', value="frm_suche:ldi_datumVon:datumHtml5")
    element.clear()  # Optional: Use this if you want to clear the existing value first
    element.send_keys(datem)
    element = dr.find_element(by='id', value="frm_suche:ldi_datumBis:datumHtml5")
    element.clear()  # Optional: Use this if you want to clear the existing value first
    element.send_keys(dateM)
    element = dr.find_element(by='id', value="frm_suche:litx_firmaNachName:text")
    element.send_keys(mot+Keys.ENTER)
    time.sleep(1)
    html=dr.page_source
    dr.close()
    return html

def is_valid_date(date_str, format='%d.%m.%Y'):
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def FindBt(t):
    for i in range(len(t)):
        if is_valid_date(t[i]):
            return i
    return -1

def SplitList(info):
    u=[]
    while True:
        x=FindBt(info)
        if (FindBt(info[x+1:])!=-1):
            x=FindBt(info[x+1:])
            u.append(info[:x+1])
            info=info[x+1:]
        else:
            u.append(info)
            break
    return u

def get_alldata(i,datem,dateM):
    url="https://neu.insolvenzbekanntmachungen.de/ap/ergebnis.jsf"
    alldata=pd.DataFrame()
    S=Selector(text=converttoHtml(url,datem,dateM,i))
    columns=['Veröffentlichungsdatum','aktuelles Aktenzeichen','Gericht','Name, Vorname / Bezeichnung','Sitz / Wohnsitz','Register']
    h=S.xpath(".//table[@id='tbl_ergebnis']/tbody//tr//td//text()").extract()
    h=[a for a in h if a!="\n"]
    if len(h)>0:
        h = SplitList(h)
    df=pd.DataFrame(h,columns=columns)
    df=df[df["aktuelles Aktenzeichen"].str.contains("/24|/23")]
    alldata=pd.concat([alldata,df],ignore_index=True)
    return alldata

def Acceptall(d):
    click_coordinates = {'x': 724, 'y': 438}
    action = ActionChains(d)
    action.move_by_offset(click_coordinates['x'], click_coordinates['y']).click().perform()

def ListToString(x):
    return " ".join(x).strip(", ")

def captcha(driver):
    time.sleep(2)
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()
    driver.implicitly_wait(5)
    driver.switch_to.default_content()
    iframe = driver.find_element(By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,'//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]').click()
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(2)
    btn=driver.find_element(by="xpath",value="html/body/div[1]/div/div/div/div[2]/div/div[2]/form/button")
    driver.execute_script("arguments[0].click();",btn)
    time.sleep(3)

def get_data(i):
    url1="https://www.creditreform.de/suche"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_extension(r"utils\buster.crx")
    dr=webdriver.Chrome(options=options)
    dr.get(url1)
    time.sleep(2)
    try:
        Acceptall(dr)
    except:
        pass
    try:
        element = dr.find_element(by="xpath",value='//*[@id="tx-solr-search-form-pi-results"]/div/input')
        element.send_keys(i+Keys.ENTER)
    except:
        pass
    time.sleep(2)

    try:

        element = dr.find_element(by="xpath",value='//*[@id="tx-solr-search"]/div[3]/div/div[2]/div/div/div[2]/a[1]')
        dr.execute_script("arguments[0].click();",element)
        k=1
    except:
        k=0

    time.sleep(2)
    if k==1:
        all_handles = dr.window_handles
        dr.close()
        dr.switch_to.window(all_handles[1])
        link=dr.current_url
        time.sleep(3)
        if "captcha" in dr.current_url.lower():
            captcha(dr)
        try:

            element = dr.find_element(by="xpath",value="html/body/div[1]/div/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[2]/p/span")
            dr.execute_script("arguments[0].click();",element)
        except:
            try:

                element = dr.find_element(by="xpath",value="/html/body/div[1]/div/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/p/span")
                dr.execute_script("arguments[0].click();",element)
            except:
                pass

        time.sleep(1)
        html=dr.page_source
        dr.close()
        return [html,link]
    else:
        dr.close()
        return ["None","None"]

def AppendDataFrames(alldata,d):
    df=pd.DataFrame(d)
    df["Namecompany"]=df["Name"].apply(lambda x: x[:x.find(", ")])
    df["Region"]=df["Name"].apply(lambda x: x[x.find(", ")+2:].strip())
    df=df[["URL","Teliphone","Email","WebSite","Purpose","Namecompany","Region"]]
    all_data=alldata.merge(df,left_on=["Name, Vorname / Bezeichnung","Sitz / Wohnsitz"],right_on=["Namecompany","Region"])
    all_data.drop(columns=["Namecompany","Region"],inplace=True)
    return all_data

def Insolvenzbekanntmachungen(keyword,datem,dateM):
    ad=get_alldata(keyword,datem,dateM)
    if len(ad)==0:
        dates=get_dates_between(datem,dateM)
        for j in dates:
            d=get_alldata(keyword,j,j)
            ad=pd.concat([ad,d])
    l=ad["Name, Vorname / Bezeichnung"]+", "+ad["Sitz / Wohnsitz"]
    l=l.to_list()
    l=list(set(l))
    d=[]
    for i in l:
        t=get_data(i)
        html=t[0]
        link=t[1]
        if html!="None":
            S=Selector(text=html)
            email=ListToString(S.xpath(".//p[@class='adres-white cursor-pointer']//text()").extract())
            tel=ListToString(S.xpath('.//p[@class="adres-white"]//span//text()').extract())
            site=ListToString(S.xpath('.//a[@class="text-white cursor-pointer"]//text()').extract())
            propose=ListToString(S.xpath("//*[@id='firmenauskunft']/div/p/span/text()").extract())
            dic={
                "Name":i,
                "URL":link,
                "Teliphone":tel,
                "Email":email,
                "WebSite":site,
                "Purpose":propose
            }
        else:
            dic={
                "Name":i,
                "URL":"None",
                "Teliphone":"",
                "Email":"",
                "WebSite":"",
                "Purpose":""
            }
        d.append(dic)
    return AppendDataFrames(ad,d)

#Testing
if __name__ == "__main__":
    keyword="*GMbH" 
    datem="07-07-2024"
    dateM="07-07-2024"
    data = Insolvenzbekanntmachungen(keyword,datem,dateM)
    