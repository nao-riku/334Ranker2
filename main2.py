import chromedriver_binary
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import threading
import time
import datetime
import calendar
import json
import copy
import requests
import os
import sys
import traceback

post_url = ""
post_body = {}
today_result = {}
world_rank = {}
load_res_yet = True
timeline_body = {}
getuser_url = ""
getuser_body = {}

start_now = datetime.datetime.now()
start_time = ""
end_time = ""


def tweet(driver):
    global post_body, post_url
    for _ in range(5):
        try:
            driver.get('https://twitter.com/334ranking/status/1642369911325593600')
            try:
                element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role=textbox]")))
            except:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[href='/login']")))
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, "[href='/login']").click()
                time.sleep(20)
                driver.get('https://twitter.com/334ranking/status/1642369911325593600')
                element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role=textbox]")))
            time.sleep(1)

            element_box = driver.find_element(By.CSS_SELECTOR, "[role=textbox]")
            element_box.send_keys("a")
            time.sleep(2) 
            
            driver.find_element(By.CSS_SELECTOR, "[data-testid=tweetButtonInline]").click()
            time.sleep(20)


            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "CreateTweet" in request.url:
                            post_url = request.url
                            post_body2 = json.loads(request.body)
                            time.sleep(0.5)
                            if "variables" in post_body2:
                                post_body = post_body2
                                print("set post_body")
                                break
                if post_body != {}:
                    break
                time.sleep(0.5)
                    

            time.sleep(3)

        except Exception as e:
            traceback.print_exc()
            time.sleep(2)
        else:
            break
	
    

def login_twitter(account, password, tel, driver):
    global timeline_body, getuser_body, getuser_url
    for _ in range(5):
        try:
            driver.get('https://twitter.com/i/flow/login')
            driver.maximize_window()
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "text")))
            time.sleep(1)
            
            element_account = driver.find_element(By.TAG_NAME, "input")
            element_account.send_keys(account)
            time.sleep(2) 
            element_account.send_keys(Keys.ENTER)
            time.sleep(20)

            element_pass = driver.find_elements(By.TAG_NAME, "input")[1]
            element_pass.send_keys(password)
            time.sleep(2)
            element_pass.send_keys(Keys.ENTER)
            time.sleep(20)

            element_tel = driver.find_elements(By.NAME, "text")
            if len(element_tel) > 0:
                element_tel[0].send_keys(tel)
                time.sleep(2) 
                element_tel[0].send_keys(Keys.ENTER)
                time.sleep(20)

            driver.get('https://twitter.com/home')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "Timeline" in request.url and "graphql" in request.url:
                            if request.body != b'':
                                timeline_body2 = json.loads(request.body)
                                time.sleep(0.5)
                                if "variables" in timeline_body2:
                                    timeline_body = timeline_body2
                                    print("set timeline_body")
                                    break
                            else:
                                timeline_body2 = request.params
                                time.sleep(0.5)
                                if "variables" in timeline_body2:
                                    timeline_body = timeline_body2
                                    timeline_body["variables"] = json.loads(timeline_body["variables"])
                                    timeline_body["features"] = json.loads(timeline_body["features"])
                                    print("set timeline_body")
                                    break
                if timeline_body != {}:
                    break
                time.sleep(0.5)
		
            driver.get('https://twitter.com/intent/user?user_id=1')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "UserByRestId" in request.url and "graphql" in request.url:
                            getuser_url = request.url
                            if request.body != b'':
                                getuser_body2 = json.loads(request.body)
                                time.sleep(0.5)
                                if "variables" in getuser_body2:
                                    getuser_body = getuser_body2
                                    print("set getuser_body")
                                    break
                            else:
                                getuser_body2 = request.params
                                time.sleep(0.5)
                                if "variables" in getuser_body2:
                                    getuser_body = getuser_body2
                                    getuser_body["variables"] = json.loads(getuser_body["variables"])
                                    getuser_body["features"] = json.loads(getuser_body["features"])
                                    print("set getuser_body")
                                    break
                if getuser_body != {}:
                    break
                time.sleep(0.5)
                
            driver.get('https://twitter.com/search?q=%40rank334&src=recent_search_click&f=live')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "adaptive" in request.url:
                            getuser_url = request.url
                            if request.body != b'':
                                getuser_body2 = json.loads(request.body)
                                time.sleep(0.5)
                                if "variables" in getuser_body2:
                                    getuser_body = getuser_body2
                                    print("set getuser_body")
                                    break
                            else:
                                getuser_body2 = request.params
                                time.sleep(0.5)
                                if "variables" in getuser_body2:
                                    getuser_body = getuser_body2
                                    getuser_body["variables"] = json.loads(getuser_body["variables"])
                                    getuser_body["features"] = json.loads(getuser_body["features"])
                                    print("set getuser_body")
                                    break
                if getuser_body != {}:
                    break
                time.sleep(0.5)
                
            tweet(driver)
        
        except Exception as e:
            traceback.print_exc()
            time.sleep(2)
        else:
            break



def reply(req, driver):
    print("reply start", datetime.datetime.now())
    driver.execute_script("""
var url = arguments[0];
    
var cookie = document.cookie.replaceAll(" ", "").split(";");
var token = "";
cookie.forEach(function (value) {
    let content = value.split('=');
    if (content[0] == "ct0") token = content[1];
})

var xhr = new XMLHttpRequest();
xhr.open('POST', url);
xhr.setRequestHeader('Authorization', 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA');
xhr.setRequestHeader('x-csrf-token', token);
xhr.setRequestHeader('x-twitter-active-user', 'yes');
xhr.setRequestHeader('x-twitter-auth-type', 'OAuth2Session');
xhr.setRequestHeader('x-twitter-client-language', 'ja');
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.withCredentials = true;

var data = JSON.stringify(arguments[1]);
xhr.send(data);

""", post_url, req)



def TweetIdTime(id):
    epoch = ((id >> 22) + 1288834974657) / 1000.0
    d = datetime.datetime.fromtimestamp(epoch)
    return d


def TimeToStr(d):
    stringTime = ""
    stringTime += '{0:02d}'.format(d.hour)
    stringTime += ':'
    stringTime += '{0:02d}'.format(d.minute)
    stringTime += ':'
    stringTime += '{0:02d}'.format(d.second)
    stringTime += '.'
    stringTime += '{0:03d}'.format(int(d.microsecond / 1000))
    return stringTime



def receive(dict, driver):
    ranker_id = "1558892196069134337"

    for item in dict:
	    
        if item["status"]["data"]["user"]["id_str"] != ranker_id:
            rep_text = False
            if item["status"]["data"]["in_reply_to_status_id_str"] == None:
                pass
            else:
                if item["status"]["data"]["in_reply_to_user_id_str"] == ranker_id:
			        pass
                else:
                    user_id = item["status"]["data"]["in_reply_to_user_id_str"]
                    user_name = ""
                    text_range = item["status"]["data"]["display_text_range"]
                    mentions = item["status"]["data"]["entities"]["user_mentions"]
                    flag = False 
                    for user in mentions:
                        if user["id_str"] == ranker_id and text_range[0] <= user["indices"][0] and user["indices"][1] <= text_range[1]:
                            flag = True
                        if user["id_str"] == user_id:
                            user_name = user["name"]
                    if flag:
                        if user_name == "":
                            pass
                        if rep_text == False:
                            orig_time = TweetIdTime(int(item["status"]["data"]["in_reply_to_status_id_str"]))
                            rep_text = "ツイート時刻: " + TimeToStr(orig_time)

            if rep_text != False:
                print(item["status"]["data"]["user"]["name"])
                req = copy.deepcopy(post_body)
                req["variables"]["reply"]["in_reply_to_tweet_id"] = item["status"]["data"]["id_str"]
                req["variables"]["tweet_text"] = rep_text
                threading.Thread(target=reply, args=(req, driver,)).start()



def interval(since, until, end, index, driver):
    driver.execute_script("""
var url = 'https://api.twitter.com/1.1/search/universal.json?q=@rank334 since:""" + since2.strftime('%Y-%m-%d_%H:%M:%S_JST') + """ until:""" + until.strftime('%Y-%m-%d_%H:%M:%S_JST') + """ -filter:retweet -filter:quote&count=100&result_type=recent&tweet_mode=extended';

var cookie = document.cookie.replaceAll(" ", "").split(";");
var token = "";
cookie.forEach(function (value) {
    let content = value.split('=');
    if (content[0] == "ct0") token = content[1];
})

var callback = arguments[arguments.length - 1];

var xhr = new XMLHttpRequest();
xhr.open('GET', url);
xhr.setRequestHeader('Authorization', 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA');
xhr.setRequestHeader('x-csrf-token', token);
xhr.setRequestHeader('x-twitter-active-user', 'yes');
xhr.setRequestHeader('x-twitter-auth-type', 'OAuth2Session');
xhr.setRequestHeader('x-twitter-client-language', 'ja');
xhr.withCredentials = true;

xhr.onload = function () {
    callback(xhr.responseText);
}

xhr.send();
    """, index % 10)
            out = json.loads(res)["modules"]
            if out != []:
                receive(out, driver)
            if datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 36, 0) < until and load_res_yet:
                get_allresult()
            break
        time.sleep(0.01)


def start():
    global start_now, start_time, end_time
    for _ in range(3):
        try:
            options=Options()
            #options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options = options)
            
        except Exception as e:
            traceback.print_exc()
            time.sleep(2)
        else:
            break

            
    times = [
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 7, 20, 0)], #2:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 7, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 11, 20, 0)], #6:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 11, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 15, 20, 0)], #20:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 15, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 19, 20, 0)], #14:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 19, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 23, 20, 0)], #18:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 23, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0) + datetime.timedelta(days=1)], #22:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0) + datetime.timedelta(days=1), datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0) + datetime.timedelta(days=1)]
    ]
    for i in range(len(times)):
        if start_now < times[i][0]:
            start_time = times[i][0]
            end_time = times[i][1]
            
            get_allresult()
            login_twitter(os.environ['NAME'], os.environ['PASS'], os.environ['TEL'], driver)
            if len(sys.argv) != 1:
                start_time = datetime.datetime.now().replace(microsecond = 0) + datetime.timedelta(seconds=2)
                end_time = times[i][0]
            threading.Thread(target=interval, args=(start_time, start_time + datetime.timedelta(seconds=1), end_time, 0, driver,)).start()
            
            break
         
threading.Thread(target=start).start()
            
