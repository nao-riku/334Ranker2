import chromedriver_binary
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import os



def login_twitter(account, password, tel, driver):
    for _ in range(3):
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
        
        except Exception as e:
            print(e)
            print(e.args)
        else:
            break


            
def make_ranking(dict, driver):
    time1 = datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 34, 0)
    winner = ""
    users = []
    dict2 = []
    for item in dict:
        if item["text"] == "334" and item["user"]["id_str"] not in users:
            users.append(item["user"]["id_str"])
            time2 = TweetIdTime(int(item["id_str"]))
            res = (time2 - time1).total_seconds()
            if 0 <= res and res < 1:
                result = '{:.3f}'.format(res)
                if winner == "" or result == winner:
                    winner = result

                img_src = "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png"
                if item["user"]["profile_image_url_https"] != "":
                    img_src = item["user"]["profile_image_url_https"]
                
                dict2.append([
                    img_src,
                    item["user"]["name"],
                    str(result),
                    item["source"],
                    item["id_str"],
                    "@" + item["user"]["screen_name"],
                    item["user"]["id_str"]
                ])

    print(str(dict2))

    

def get_334(driver):
    time1 = datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 33, 59)
    time2 = datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 34, 2)
    get_time = datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 34, 3)
    while True:
        if get_time < datetime.datetime.now():
            driver.execute_script("""
window.data = "";
var url1 = 'https://api.twitter.com/1.1/search/';
var url2 = '.json?count=100&result_type=recent&q=334 since:""" + time1.strftime('%Y-%m-%d_%H:%M:%S_JST') + """ until:""" + time2.strftime('%Y-%m-%d_%H:%M:%S_JST') + """ -filter:retweet -filter:quote -filter:replies';
var out = [];
var out2 = [];

var cookie = document.cookie.replaceAll(" ", "").split(";");
var token = "";
cookie.forEach(function (value) {
    let content = value.split('=');
    if (content[0] == "ct0") token = content[1];
})

get_tweets();

function setheader(xhr) {
    xhr.setRequestHeader('Authorization', 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA');
    xhr.setRequestHeader('x-csrf-token', token);
    xhr.setRequestHeader('x-twitter-active-user', 'yes');
    xhr.setRequestHeader('x-twitter-auth-type', 'OAuth2Session');
    xhr.setRequestHeader('x-twitter-client-language', 'ja');
    xhr.withCredentials = true;
}

function get_tweets(max_id) {
    let xhr = new XMLHttpRequest();
    let url = max_id !== undefined ? url1 + "universal" + url2 + " max_id:" + max_id : url1 + "universal" + url2;
    xhr.open('GET', url);
    setheader(xhr);
    xhr.send();

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            res = JSON.parse(xhr.responseText).modules;
            if (res.length <= 0 || (max_id !== undefined && res.length <= 1)) {
                out.reverse();
                get_tweets2();
            } else {
                if (max_id !== undefined) res.shift();
                for (let i = 0; i < res.length; i++) out.push(res[i].status.data);
                get_tweets(out[out.length - 1].id_str);
            }
        }
    }
}

function get_tweets2(max_id) {
    let xhr = new XMLHttpRequest();
    let url = max_id !== undefined ? url1 + "tweets" + url2 + " max_id:" + max_id : url1 + "tweets" + url2;
    xhr.open('GET', url);
    setheader(xhr);
    xhr.send();

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            res = JSON.parse(xhr.responseText);
            if ('statuses' in res) {
                res = res.statuses;
                if (res.length <= 0 || (max_id !== undefined && res.length <= 1)) {
                    out2.reverse();
                    loop: for (let i = 0; i < out2.length; i++) {
                        for (let j = 0; j < out.length; j++) if (out2[i].id_str === out[j].id_str) continue loop;
                        if (i === 0) out.unshift(out2[i]);
                        else {
                            for (let k = 0; k < out.length; k++) {
                                if (out2[i - 1].id_str === out[k].id_str) {
                                    out.splice(k, 0, out2[i]);
                                    break;
                                }
                            }
                        }
                    }
                    window.data = out;
                } else {
                    if (max_id !== undefined) res.shift();
                    for (let i = 0; i < res.length; i++) out2.push(res[i]);
                    get_tweets2(out2[out2.length - 1].id_str);
                }
            } else window.data = out;
        }
    }
}
            """)
            while True:
                time.sleep(0.01)
                res = driver.execute_script("return window.data")
                if res != "":
                    make_ranking(res, driver)
                    break
            break
        time.sleep(0.01)


def start():
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
            print(e)
            print(e.args)
        else:
            break

        login_twitter(os.environ['NAME'], os.environ['PASS'], os.environ['TEL'], driver)
        get_334(driver)
         
start()
            
