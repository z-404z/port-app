import socket


print("---------------------------------------------------------------")
print("--------------- Hello in 'Z-404 APP' --------------------------")
print("---------------------------------------------------------------")
print("\n")

ports_services = {
    "FTP": 20,
    "FTP": 21,
    "SSH": 22,
    "Telnet": 23,
    "SMTP": 25,
    "DNS": 53,
    "DHCP": 67,
    "DHCP": 68,
    "HTTP": 80,
    "POP3": 110,
    "NNTP": 119,
    "NTP": 123,
    "IMAP": 143,
    "SNMP": 161,
    "IRC": 194,
    "HTTPS": 443,
    "SMB": 445,
    "SMTPS": 465,
    "IMAPS": 993,
    "POP3S": 995,
    "MS SQL": 1433,
    "Oracle DB": 1521,
    "MySQL": 3306,
    "RDP": 3389,
    "PostgreSQL": 5432,
    "Redis": 6379,
    "HTTP": 8080
}
l1=[]
n=input('press "i" for any information : ')
if n =='i':
    print('Number Port press :   "1"')
    print('local ip press  :   "2"')
t=input("press number : ")

#todo###########################################################
if t=='1':
    
  while True:
    
     x = input("Enter Service Protocol Name: ")

     for key, value in ports_services.items():
        if x==key or x== value:
          print(f"The number port of {key} is :  {value}")
          l1.append(x)
          
     z=input("Do You Want Other Number Port 'y/n': ")   
     if z=='n':
      break   
  print("You Search About : ")

  for i in l1:
     print(f"{i}")

#todo##############################################################
elif  t=='2':
   hostname = input("enter host name ex: google.com : ")


   local_ip = socket.gethostbyname(hostname)
   print(f"Host Name is : {hostname} >>>: IP Is {local_ip} ")

   
