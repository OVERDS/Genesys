import requests, socket, sys, os

os.system('clear')
h = "\33[0;32m"
hm = "\33[32;1m"
b = "\33[0;36m"
bm = "\33[36;1m"
m = "\33[31;1m"
p = "\33[37;1m"
hit = "\33[30;1m"
o = "\33[33;1m"
k = "\33[1;33m"

print p
os.system('figlet -f standard "GENESYS"')
print k + " >>>>>>>>>>>>>>"+ m +"{"+ p +"OVERDOSIS"+ m +"}"+ k +"<<<<<<<<<<<<<<"
print m + "       {"+ p +"https://github.com/OVERDS"+ m +"}" + p
try :
  web = raw_input("Enter website "+ m +"~> " + p)
  rep = web.replace("https://", "").replace("http://", "").replace("www.", "")
  ip = socket.gethostbyname(rep)
  print "IP Address "+ m +":"+ p +" ",ip
except socket.gaierror:
  print m + "Unknown website"
  sys.exit(1)

data = {
  "q": rep
}

#menu 
def menu() :
  print "Choose your menu "+ m +": "
  print "{"+ p +"01"+ m +"} "+ p +"DNS LOOKUP"
  print m + "{"+ p +"02"+ m +"} "+ p + "WHOIS LOOKUP"
  print m + "{"+ p +"03"+ m +"} "+ p + "GEO IP LOOKUP"
  print m + "{"+ p +"04"+ m +"} "+ p + "PORT SCANNER"
  print m + "{"+ p +"05"+ m +"} "+ p + "PAGE LINKS"
  print m + "{"+ p +"06"+ m +"} "+ p + "ZONE TRANSFER"
  print m + "{"+ p +"07"+ m +"} "+ p + "HTTP HEADER"
  print m + "{"+ p +"08"+ m +"} "+ p + "HOST FINDER"
  print m + "{"+ p +"09"+ m +"} "+ p + "DNS FINDER"
  print m + "{"+ p +"10"+ m +"} "+ p + "SUBNET LOOKUP"
  print m + "{"+ p +"11"+ m +"} "+ p + "ASN LOOKUP"
  print m + "{"+ p +"12"+ m +"} "+ p + "ANALITYCS SEARCH"
  print m + "{"+ p +"13"+ m +"} "+ p + "TRACEOUT"
  print m + "{"+ p +"14"+ m +"} "+ p + "PING TESTER"
  print m + "{"+ p +"15"+ m +"} "+ p + "REVERSE DNS"
  print m + "{"+ p +"16"+ m +"} "+ p + "REVERSE IP LOOKUP"
  print m + "{"+ p +"17"+ m +"} "+ p + "EXIT"

def back() :
  back = raw_input("Back?Y/N "+ m +": " + p)
  if back.lower() == "y" :
    os.system('clear')
    menu()
    main()
  elif back.lower() == "n" :
    sys.exit(1) 
  else:
    sys.exit(1)


def main() :
  try:
    choose = raw_input("Enter your choose "+ m +"~> " + p)
    
    if choose == "1" or choose == "01" :
      url = "https://api.hackertarget.com/dnslookup"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "2" or choose == "02" :
      url = "https://api.hackertarget.com/whois/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "3" or choose == "03" :
      url = "https://api.hackertarget.com/geoip/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "4" or choose == "04" :
      url = "https://api.hackertarget.com/nmap/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "5" or choose == "05" :
      url = "https://api.hackertarget.com/pagelinks/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "6" or choose == "06" :
      url = "https://api.hackertarget.com/zonetransfer/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "7" or choose == "07" :
      url = "https://api.hackertarget.com/httpheaders/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "8" or choose == "08" :
      url = "https://api.hackertarget.com/hostsearch/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "9" or choose == "09" :
      url = "https://api.hackertarget.com/findshareddns/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "10" :
      url = "https://api.hackertarget.com/subnetcalc/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "11" :
      url = "https://api.hackertarget.com/aslookup/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "12" :
      url = "https://api.hackertarget.com/analyticslookup/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "13" :
      url = "https://api.hackertarget.com/mtr/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "14" :
      url = "https://api.hackertarget.com/nping/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "15" :
      url = "https://api.hackertarget.com/reversedns/"
      r = requests.get(url, params=data).text
      print r
      back()
      
    elif choose == "16" :
      url = "https://api.hackertarget.com/reverseiplookup/"
      r = requests.get(url, params=data).text
      print r
      back()
    elif choose == "17" :
      print "good bye"
      sys.exit(1)
      
    else:
      print "Wrong input"
      sys.exit(1)
  except:
    sys.exit(1)

    
menu()
main()


