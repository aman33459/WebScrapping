import webbrowser
import requests
import bs4

video=raw_input("enter the videos u want to watch\n");
url="http://www.youtube.com/results?search_query="+video;
#print url
r=requests.get(url);
soup=bs4.BeautifulSoup(r.content);
ss=soup.select(".yt-lockup-title a");
#print ss[0].get("href");
webbrowser.open("http://www.youtube.com"+ss[0].get("href"))


