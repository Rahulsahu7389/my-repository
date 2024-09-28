import wikipedia
import datetime
import webbrowser
from googlesearch import search

while True:
	i = input("enter identification : ")
	if "Zira" in i:
		print("you can access now")
		print("\U0001F603")
		break
	else:
		print("anauthorized user ")

h = int(datetime.datetime.now().hour)
if h >=0 and  h <12:
	print(" good morning sir\nhow can i help you")
else:
	print("Good Evening Sir\nhow can i help you.")
	
while True:
	d = input()
	if "who are you" in d :
		print("my name is ZIRA programmed by Rahul Sahu ")
		
	elif "time" in d:
		h = datetime.datetime.now().time()
		print(h)
		
	elif "date" in d :
		y= datetime.datetime.now().date()
		print(y)
	elif "weather" in d:
		se = input("of which area : ")
		
		webbrowser.open(f"http://m.accuweather.com/en/in/{se}/3198661/extended-weather-forecast/3198661?unit=c&lang=en-us&partner=xiaomiwidget")
	
	elif d =="how are you":
		print("\U0001F603 i am fine") 
	
	elif "open" in d:
		c = d.replace("open","")
		q = (f"https://www{c}.com")
		re = q.replace(" ",".")
		webbrowser.open(re)
	
	elif "class9th" in d:
		webbrowser.open("https://www.successcds.net/learn-english/class-9/rain-on-the-roof-class-9-cbse-english.html")
		
	elif "where is" in d or "locate" in d:
		if "where is" in d:
			replaced = d.replace("where is ","")
		elif "locate" in d:
			replaced = d.replace("locate ","")
		webbrowser.open(f"https://maps.google.com/maps?q={replaced}")
		
	elif "make a" and "website" in d or "create a" and "website" in d:
			input1 = input("what do you want to name you file : ")
			with open("/storage/emulated/0/pydroid 2/index2.html") as f:
				reader = f.read()
				with open(f"/storage/emulated/0/pydroid 2/{input1}.html","a") as f2:
					f2.write(reader)
					print("your website is ready, check it out!")
			
		
    	
	elif "wikipedia" in d:
		try:
			print("Searching....")
			#wikipedia.set_lang("hi")
			print(wikipedia.summary(d))
		except :
			print("we cannot match your search from web\nso enter again from other id")
		
		
	else:
		try:
			#query = input("what you want to search : ")
			print("searching.......")
			for r in search(d,tld="co.in", num=10,
			stop=10, pause=2):
				print(r)
		except:
			print("please check your internet connection.It is necessary to on data while your doing net scraping.")
