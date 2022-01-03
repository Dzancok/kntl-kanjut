from bs4 import BeautifulSoup as bs
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation
#sfile
@userge.on_cmd("sdw", about={ 
	'header': "SDW",
	'usage': "{tr}sdw [Link File]\n"})
	

async def sdw(event):
	ses = requests.Session()
	url = event.pattern_match.group(1)
	raww = ses.get(url,headers={"User-Agent":"Chrome"}).text
	soup = bs(raww, "html.parser")
	down = re.search('href="https://sfile.mobi/download(.*?)"',raww).group(1)
	load = "https://sfile.mobi/download"+down
	judul_link = re.search('class="img" alt="(.*?)"', raww).group(1)
	oleh = re.search('rel="nofollow">(.*?)<', raww).group(1)
	pada = re.search('i> - Uploaded: (.*?)<', raww).group(1)
	tot_down = re.search('i> - Downloads: (.*?)<', raww).group(1)
	tag = re.search("i> - (.*?)<", raww).group(1)
	penis = re.search('.html">(.*?)<',raww).group(1)
	ukuran = re.search("Download File (.*?)<",raww).group(1)
	await event.edit_message(f"""**================================
[+] URL           : {url}
[*] Title         : {judul_link}
[#] Tags          : {tag}
[] File Type     : {penis}
[-] Bio File      :
[-] File Size     : {ukuran}
[=] Uploaded By   : {oleh}
[?] Upload Date   : {pada}
[*] Total Download: {tot_down}
================================**""")


