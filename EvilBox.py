#!/usr/bin/env/python3
# This Python file uses the following encoding:utf-8

# Author: HackWeiser360(MådMâx)
# Github: Github.com/HackWeiser360
# Twitter: Twitter.com/503_madmax
# Instagram: Instagram.com/madmax4708
# If you copy or use any part of this program give HackWeiser360 the credits they deserve

import dns.resolver
import json
import nmap
import os
import re
import requests
import socket
import time
import urllib.request
from time import gmtime, strftime


banner = ("""
            \033[1;34m
          _____       _ _ ____
          | ____|_   _(_) | __ )  _____  __
          |  _| \ \ / / | |  _ \ / _ \ \/ /
          | |___ \ V /| | | |_) | (_) >  <
          |_____| \_/ |_|_|____/ \___/_/\_\
          
        
            \033[1;m

        \033[31mEvilBox\033[0m Recon Toolkit

        Author:  HackWeiser360(MådMâx)
        Github:  Github.com/HackWeiser360
        Twitter: @503_madmax

            \031[1;31mLet's play a game\033[0m😈
            """)

print (banner)
time.sleep(0.4)


target = input("[+] \033[34mWhat domain do you want to search: \033[0m").strip()
compname = input("[+] \033[34mEnter the company name: \033[0m").strip()
company = target.partition(".")
comp = company[0]
time.sleep(1)


def jan():
    try:
        url = ("http://ip-api.com/json/")
        response = urllib.request.urlopen(url + target)
        data = response.read()
        jso = json.loads(data)
        time.sleep(1.5)

        print("\n [+] \033[34mUrl: " + target + "\033[0m")
        print(" [+] " + "\033[34m" + "IP: " + jso["query"] + "\033[0m")
        print(" [+] " + "\033[34m" + "Status: " + jso["status"] + "\033[0m")
        print(" [+] " + "\033[34m" + "Region: " + jso["regionName"] + "\033[0m")
        print(" [+] " + "\033[34m" + "Country: " + jso["country"] + "\033[0m")
        print(" [+] " + "\033[34m" + "City: " + jso["city"] + "\033[0m")
        print(" [+] " + "\033[34m" + "ISP: " + jso["isp"] + "\033[0m")
        print(" [+] " + "\033[34m" + "Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
        print(" [+] " + "\033[34m" + "Zipcode: " + jso["zip"] + "\033[0m")
        print(" [+] " + "\033[34m" + "TimeZone: " + jso["timezone"] + "\033[0m")
        print(" [+] " + "\033[34m" + "AS: " + jso["as"] + "\033[0m" + "\n")
        print ("»"*60 + "\n")
        time.sleep(1)

    except Exception:
        pass

    except KeyboardInterrupt:
            print("\n")
            print("[-] User Interruption Detected..!")
            time.sleep(1)


def header():
    try:
        print("\033[34mScanning.... HTTP Header \033[0m" + target)
        time.sleep(1.5)
        command = ("http -v " + target)
        proces = os.popen(command)
        results = str(proces.read())
        print("\033[1;34m" + results + command + "\033[1;m")
        print ("»"*60 + "\n")

    except Exception:
        pass

    except KeyboardInterrupt:
            print("\n")
            print("[-] User Interruption Detected..!")
            time.sleep(1)


def nmaps():
    try:
        print("\033[34mScanning.... Nmap Port Scan: \033[0m" + target)
        print ("[+]\033[34m - --> \033[0mThis may take some minutes. Get a cup of coffe \033[34mEvilBox\033[0m gathers the data.....\n")
        time.sleep(1)

        scanner = nmap.PortScanner()
        command = ("nmap -Pn " + target)
        process = os.popen(command)
        results = str(process.read())
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())

        print("\033[34m" + results + command + logPath + "\033[0m")
        print("\033[34mNmap Version: \033[0m", scanner.nmap_version())
        print ("»"*60 + "\n")

    except Exception:
        pass

    except KeyboardInterrupt:
            print("\n")
            print("[-] User Interruption Detected..!")
            time.sleep(1)


def aug():
    print ("[+] \033[34mMail Servers:\033[0m " + target + "\n")
    time.sleep(0.5)
    for sun in dns.resolver.query(target, "MX"):
        print ("\t\033[34m" + (sun.to_text()) + "\033[0m")
    print ("\n" + "»" * 60)
    print ("[+] \033[34mDNS Text Records:\033[0m " + target + "\n")
    time.sleep(0.2)
    for sun in dns.resolver.query(target, "TXT"):
        print ("\t\033[34m" + (sun.to_text()) + "\033[0m")
    print ("\n" + "»" * 60)
    print ("[+] \033[34mNameserver Records:\033[0m " + target + "\n")
    time.sleep(0.2)
    for sun in dns.resolver.query(target, "NS"):
        print ("\t\033[34m" + (sun.to_text()) + "\033[0m")
    print ("\n" + "»" * 60)
    okta = comp + ".okta.com"
    webmail = "webmail." + comp + ".com"
    email = "email." + comp + ".com"
    slack = "%s.slack.com" % comp

    try:
        if len(socket.gethostbyname(okta)) <= 15:
            print ("\n\t\033[34mHost of interest:\033[0m " + okta)
            time.sleep(0.3)
        if len(socket.gethostbyname(webmail)) <= 15:
            print ("\t\033[34mHost of interest:\033[0m " + webmail)
            time.sleep(0.3)
        if len(socket.gethostbyname(email)) <= 15:
            print ("\t\033[34mHost of interest:\033[0m " + email)
            time.sleep(0.3)
        if len(socket.gethostbyname(slack)) <= 15:
            print ("\t\033[34mHost of interest:\033[0m " + slack + "\n")
            time.sleep(0.3)

    except Exception:
        pass


def june():
    print ("»" * 60 + "\n")
    print ("[+] \033[34mSearch Results for: \033[0m%s " % target)
    url = ("https://ctsearch.entrust.com/api/v1/certificates?fields=subjectDN&domain=%s&includeExpired=false&exactMatch=false&limit=5000" % target)
    useragent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36")
    headers = {"User-Agent": useragent}
    try:
        print ("[+]\033[34m - --> \033[0mThis may take some minutes. Get yourself some coffe \033[34mEvilBox\033[0m gathers the data.....\n")
        time.sleep(1)
        response = requests.get(url, headers=headers)
        rain = re.findall(r'subjectDN": "cn\\u003d[a-zA-Z0-9.\-]{1,}', response.text)
        babs = []

        for item in rain:
            xtra = re.sub("subjectDN\": \"cn\\\\u003d", '', item)
            babs.append(xtra)

        dmset = set(babs)
        counter = 0
        print ("")

        for itemm in dmset:
            counter = counter + 1
            print ("%s. %s" % (str(counter), str(itemm)))

            try:
                ns = dns.resolver.query(str(itemm), "A")
                if "dns.resolver" in str(ns):
                    for joo in ns.response.answer:
                        for aug in joo.items:
                            ip = str(aug)
                            print("\t[+]\033[34m %s resolves to: %s\033[0m" % (str(itemm), str(ip)))

            except Exception:
                pass

        print ("")
        print ("\033[34m[+] Total Domains: %s\033[0m" % str(counter))

        print ("»"*60 + "\n")
        time.sleep(1)

    except KeyboardInterrupt:
            print ("\n\033[1;91m[!]\033[0 User Interruption Detected..!")
            time.sleep(1)

    except Exception:
        pass


mainhub = ("https://github.com/%s" % comp)
gitpeople = ("https://github.com/orgs/%s/people" % comp)
response = requests.get(mainhub)
response_text = response.text
resp = requests.get(gitpeople)
respon_text = resp.text
listusers = re.findall(r'self\" href=\"[a-zA-Z0-9\-/]{3,}', respon_text)
listuser = []


def list_users():
    try:
        for item in listusers:
            x = re.sub("self\" href=\"/", "", item)
            listuser.append(x)

        usersset = set(listuser)
        counter = 0

        if listusers != []:
            print ("\033[34m[+] List of %s github user pages:\033[0m" % target)
            print ("»"*60 + "\n")
            for user in usersset:
                try:
                    counter = counter + 1
                    userpage = ("https://github.com/%s" % user)
                    print (str(counter) + " \t[+] " + "\033[34m " + userpage + "\033[0m")
                except Exception as e:
                    print("Error: %s" % e)

        print ("")
        print ("\033[34m[+] Total Users Found: %s\033[0m" % str(counter))

        print ("»"*60 + "\n")
        time.sleep(1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!]\033[0 User Interruption Detected..!")
            time.sleep(1)

    except Exception:
        pass


def mails():
    listofusers2 = set(listuser)
    try:
        print ("[+] \033[34mList of possible company email addresses harvested")
        print ("from %s github user pages & duckduckgo searches:\033[0m" % target)
        time.sleep(0.5)
        print ("»"*60 + "\n")
        for user in listofusers2:
            userpage = ("https://api.github.com/users/%s/events/public" % user)
            respon = requests.get(userpage)
            respons_text = respon.text
            findemail = re.findall(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', respons_text)
            if findemail != []:
                emailset = set(findemail)
                for each in emailset:
                    if target in each:
                        print ("\t[+] \033[34m" + (each) + "\033[0m")
                        time.sleep(0.1)

        searchurl = ("https://duckduckgo.com/html/?q=site%3Alinkedin.com+email+%40%22" + target + '%22')
        webresponse = requests.get(searchurl)
        webresp = webresponse.text
        findem = re.findall(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', webresp)
        if findem != [1]:
            setmail = set(findem)
            for each in setmail:
                if target in each:
                    print ("\t[+] \033[34m" + (each) + "\033[0m\n\n")
                    time.sleep(1)
            print ("\n\n\t\033[34m[!] Don't use me for illegal purposes\033[0m 🤒\n\n")

    except KeyboardInterrupt:
            print ("\n\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(1)
            print ("\n\n\t\033[34m[√] Nice coffee\033[0m\n\n")

    except Exception:
        pass


print ("\n\t\033[34m Visit github.com/HackWeiser360 for more\033[0m 😃\n")


# =====# Main #===== #
if __name__ == "__main__":
    jan()
    header()
    nmaps()
    aug()
    june()
    list_users()
    mails()