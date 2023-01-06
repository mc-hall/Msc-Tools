import os, sys, socket, time, shutil, win32print, string, subprocess, wmi
from ctypes import windll
from time import sleep
from tqdm import tqdm
from pypsexec.client import Client


def error_log(e):
	error_copy_log = open('error_copy_log.txt', 'a')
	error_copy_log.write(str(e))
	error_copy_log.write('\n')
	error_copy_log.close()
	print(e) 
	time.sleep(8)	

def make_C():
	try:
		os.chdir('\\\\corp1\\users\\'+username+'\\')
		os.mkdir('_C')
	except Exception as e:
		error_log(e)
		print(e) 
		time.sleep(8)	


#Write IP address ; if 10.1.2.X = static
def copy_IP():
	os.chdir(net_dir)
	try:
		ip_addr = socket.gethostbyname(device_id)
		#if '1' in ip_addr[5]:
		text = open(ip_addr+'_'+device_id+'.txt', 'wb')
		text.close()
		#elif '2' in ip_addr[5]:
			#text = open(ip_addr+'_STATIC.txt', 'wb')
			#text.close()
	except Exception as e:
		error_log(e)
		print(e) 
		time.sleep(8)	


#get network drives
def network_drives():
	try:
		os.chdir(net_dir)
		net_drives = open('Network Drives.bat', 'a')
		net_drives.write('net use > MAPPED_DRIVES.txt \n')
		#installed_printers.write('xcopy C:\\Users\\%username%\\printer_attached.txt \\\\corp1\\users\\%username%\\C\\printer_attached.txt \n')
		net_drives.close()
		print('Network list created successfully')
		time.sleep(4)
	except Exception as e:
		error_log(e)
		print(e) 
		time.sleep(8)


#write printer bat
def get_printers():
	try:
		os.chdir(net_dir)
		installed_printers = open('Connected_printers.bat', 'a')
		installed_printers.write('wmic printer get name, default > PRINTERS_MAPPED.txt \n')
		#installed_printers.write('xcopy C:\\Users\\%username%\\printer_attached.txt \\\\corp1\\users\\%username%\\C\\printer_attached.txt \n')
		installed_printers.close()
		print('Printer list created successfully')
		time.sleep(4)
	except Exception as e:
		error_log(e)
		print(e) 
		time.sleep(8)

#run printer batch file
def run_printer_bat():
	bat = 'C:\\Users\\'+username+'\\Connected_printers.bat'
	try:
		c = Client(device_id, username='user', encrypt=False)
		print('Connecting to client...')
		c.connect()
		print('starting service...')
		c.create_service()
		stdout,stderr, rc=c.run_executable(bat)
		c.remove_service()
		c.disconnect()

		#subprocess.call(r'Connected_printers.bat')
	except Exception as e:
		error_log(e)
		print(e) 
		time.sleep(8)

#Copy Documents folder
def copy_documents():
	try:
		for items in os.listdir(local_dir):
			if items == 'Documents':
				print('Copying Documents folder...')
				shutil.copytree(os.path.join(local_dir,items),os.path.join(net_dir, items))
	except Exception as e:
		error_log(e)
		print(e) 
		time.sleep(8)


#Copy Desktop folder
def copy_desktop():
	try:
		for items in os.listdir(local_dir):
			if items == 'Desktop':
				for item in os.listdir('Desktop'):
					print('Copying',item)
				print('Copying Desktop folder...')
				shutil.copytree(os.path.join(local_dir,items),os.path.join(net_dir, items))
	except Exception as e:
		print(e) 
		time.sleep(8)


#Copy Favorites
def copy_favorites():
	try:
		for items in os.listdir(local_dir):
			if items == 'Favorites':
				print('Copying Favorites folder...')
				shutil.copytree(os.path.join(local_dir,items),os.path.join(net_dir, items))
	except Exception as e:
		print(e) 
		time.sleep(8)

#Copy Outlook archive
def copy_outlook_autocache():
	stream_file = 'Stream_Autocomplete'
	ol_ac_src = '\\\\'+device_id+'\\c$\\Users\\'+username+'\\AppData\\Local\\Microsoft\\Outlook\\RoamCache\\'
	ol_ac_dest = '\\\\corp1\\users\\'+username+'\\_C\\'
	try:
		for items in os.listdir(ol_ac_src):
			if items.startswith(stream_file):
				print('Copying Outlook Auto Complete...')
				shutil.copy(os.path.join(ol_ac_src,items), os.path.join(ol_ac_dest, items))
	except Exception as e:
		print(e) 
		time.sleep(8)


#Get mapped drives
def make_bat():
	try:
		#create bat file
		os.chdir(local_dir)
		net_drive = open('map_me.bat', 'a')
		net_drive.write('@echo off \n')
		net_drive.write('net use > mapped_drives.txt \n')
		net_drive.write('xcopy C:\\Users\\%username%\\mapped_drives.txt \\\\corp1\\users\\%username%\\_C\\mapped_drives.txt* /y \n')
		net_drive.write('del "C:\\Users\\%username%\\mapped_drives.txt" /y')
		net_drive.close()
		
	except Exception as e:
		print(e) 
		time.sleep(8)




device_id = input("Enter Computer Name: ")
username = input("Enter username: ")
local_dir = '\\\\'+device_id+'\\c$\\Users\\'+username+'\\'   #EX=> \\mine-5040\\c$\\Users\\mine\\
net_dir = '\\\\corp1\\users\\'+username+'\\_C\\'  		  #EX=> \\corp1\\users\\mine\\C\\
yes = ['yes','y']
no =['no','n']

make_C()
copy_IP()
get_printers()
network_drives()
copy_favorites()
copy_documents()
copy_outlook_autocache()
make_bat()
copy_desktop()

	
		



