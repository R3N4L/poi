from flask import *
import json,wikipedia,requests,datetime,random,os
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
        print(request.data)
        wikipedia.set_lang('id')
        cmd = json.loads(request.data.decode())['query']['message'].split(' ')
        if cmd[0] in ['!wikipedia','!wiki']:
                print(cmd[1])
                uw = cmd[1]
                aw = cmd[11:]
                try:
                        hasil=wikipedia.page(aw)
                        return json.dumps({'replies':[{'message':'%s\n\nsource : %s'%(hasil.summary,hasil.url)}]})
                except Exception as e:
                        return json.dumps({'replies':[{'message':'Error : %s'%e}]})
        elif cmd[0] in ['!covid','!corona']:
                print(cmd[0])
                js = requests.get('https://api.kawalcorona.com/indonesia/').json()
                negara = js[0]['name']
                positif = js[0]['positif']
                sembuh = js[0]['sembuh']
                mening = js[0]['meninggal']
                dirawat = js[0]['dirawat']
                hasil = f'Negara : {negara}\nPositif : {positif}\nSembuh : {sembuh}\nMeninggal : {mening}\nDirawat : {dirawat}'
                return json.dumps({'replies':[{'message':'%s'%hasil}]})
        elif cmd[0] in ['!time','!times']:
                print(cmd[0])
                now = datetime.datetime.now()
                hasil = f'Waktu lokal bot sekarang adalah : \n🗓 {now.ctime()}'
                return json.dumps({'replies':[{'message':'%s'%hasil}]})
        elif cmd[0] in ['!quote','!quotes']:
                print(cmd[0])
                quote=random.choice(open('bijak.txt').read().splitlines()).split('\n')[0]
                return json.dumps({'replies':[{'message':'%s'%quote}]})
        elif cmd[0] in ['!about','!tentang']:
                print(cmd[0])
                teks = '››››› [ About ] ‹‹‹‹‹\n» Created by : Muhamad Royyani\n» Contact : https://wa.me/6285693587969'
                return json.dumps({'replies':[{'message':'%s'%teks}]})
        elif cmd[0] in ['!help','!bantuan']:
                print(cmd[0])
                teks='››››› [ Commands ] ‹‹‹‹‹\n» !help - Menampilkan bantuan\n» !wiki <query>\n» !time - Untuk Melihat Waktu\n» !covid - Melihat Info Covid19 Indonesia\n» !quote - Quote² bijak\n» !about - About this bot'
                return json.dumps({'replies':[{'message':'%s'%teks}]})
        else:
                pass
app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=True)