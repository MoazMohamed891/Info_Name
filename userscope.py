import requests
import concurrent.futures
import json
import csv
import os

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

requests.packages.urllib3.disable_warnings()


def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(MAGENTA + """
                                                                                         
                                                                                          
                             ,'  'KKl                                                     
                            l.   'WMMX.                                                   
                           ;:  ,ldOXWMW.                                                  
                          .0d,'..   .l0K.                                                 
                         ;K            :W.                                                
                         .k:           dc                                                 
                       'klkNk.       :0OXK0c                                              
                      ;K    .;      .'   :ckd                                             
                    ;k;                     0k:                                           
                   k0.   d::;;;;;;;;;;;,,l' .ckx'                                         
                 dXWd    d               ;.   .KM                                         
                ::;ccc;. c      ,l;      ; ..:d00c'                                       
                         '      .l'      '    ...                                         
                         .                                                                
                                                       
""" + RESET)
    print(RED + "#" * 67)
    print(RESET)
    print(BLUE + "        PHISHING DETECTOR - URL Scanner" + RESET)
    print(RED + "#" * 67)
    print(RESET)
    print(MAGENTA + " ⚡ " + BLUE + "BY.Moaz Mohamed" + MAGENTA + " ⚡" + RESET)
    print(BLUE)
    print(" Github   : https://github.com/MoazMohamed891")
    print(" Linkedin : https://www.linkedin.com/in/moaaz-mohamed-hassan-07604a348")
    print(" Website  : https://asseccccccza78184867.github.io/access/")
    print(RESET)
    print(RED + "#" * 67)
    print(RESET)
    print()

def check_site(site, url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        status = "FOUND" if r.status_code == 200 else "NOT FOUND"
        return {"site": site, "url": url, "status": status}
    except Exception:
        return {"site": site, "url": url, "status": "ERROR"}

show_banner()
username = input("[?] Username: ").strip()

sites = {
    "GitHub": f"https://github.com/{username}",
    "GitLab": f"https://gitlab.com/{username}",
    "Bitbucket": f"https://bitbucket.org/{username}",
    "Facebook": f"https://www.facebook.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "X": f"https://x.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Threads": f"https://www.threads.net/@{username}",
    "Snapchat": f"https://www.snapchat.com/add/{username}",
    "Telegram": f"https://t.me/{username}",
    "YouTube": f"https://www.youtube.com/@{username}",
    "Twitch": f"https://www.twitch.tv/{username}",
    "Vimeo": f"https://vimeo.com/{username}",
    "Medium": f"https://medium.com/@{username}",
    "WordPress": f"https://{username}.wordpress.com",
    "Blogspot": f"https://{username}.blogspot.com",
    "Tumblr": f"https://{username}.tumblr.com",
    "Dev.to": f"https://dev.to/{username}",
    "Behance": f"https://www.behance.net/{username}",
    "Dribbble": f"https://dribbble.com/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Quora": f"https://www.quora.com/profile/{username}",
    "Disqus": f"https://disqus.com/by/{username}/",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Flickr": f"https://www.flickr.com/people/{username}",
    "SoundCloud": f"https://soundcloud.com/{username}",
    "Audiomack": f"https://audiomack.com/{username}",
    "Steam": f"https://steamcommunity.com/id/{username}",
    "CodePen": f"https://codepen.io/{username}",
    "Replit": f"https://replit.com/@{username}",
    "Kaggle": f"https://www.kaggle.com/{username}",
    "HackerOne": f"https://hackerone.com/{username}",
    "Bugcrowd": f"https://bugcrowd.com/{username}",
}

results = []

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(check_site, s, u) for s, u in sites.items()]
    for future in concurrent.futures.as_completed(futures):
        results.append(future.result())

found = 0
for r in results:
    if r["status"] == "FOUND":
        found += 1
        print(f"[FOUND] {r['site']} -> {r['url']}")

with open(f"{username}_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

with open(f"{username}_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["site", "url", "status"])
    writer.writeheader()
    writer.writerows(results)

print(f"Profiles Found: {found}")
print(f"Platforms Checked: {len(sites)}")
