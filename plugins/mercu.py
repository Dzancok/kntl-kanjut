import time, requests as req
from bs4 import BeautifulSoup as bs
from userge import userge, Message

@userge.on_cmd("merc", about={
	'header': "Untuk cek akun MERCU",
	'usage': "{tr}mercu [nim]:[pass]\n"})
	
async def merc(message: Message):
	"""Untuk cek akun MERCU"""
	replied = message.input_str
	if not replied:
		await message.err("```Isi nim:pass setelah command, untuk mengecek akun.```", del_in=5)
		return 
	if ":" not in replied:
		await message.err("```Format harus nim:pass.```", del_in=5) 
		return
	await message.edit("```Sedang mengecek, tunggu...```")
	u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
	ses = req.Session()
	url = 'https://sso.mercubuana.ac.id'
	raw = ses.get(url).text
	tok = bs(raw, 'html.parser').findAll('input')[0]['value']
	dat = {'_method':tok,
	'username':u,
	'password':p,
	'submit':'submit'}
	post = ses.post(url, data=dat)
	if "Home" in post.text:
		await message.edit(f"MERCU\nNIM  : `{u}`\nPass : `{p}`\nGagal Login! Password salah.", del_in=5)
	else:
		await message.edit(f"MERCU\nNIM  : `{u}`\nPass : `{p}`\nBerhasil Login.")
	
		

