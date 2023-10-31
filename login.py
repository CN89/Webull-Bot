from webull import webull # for paper trading import 'paper_webull' instead
import json
from webull.streamconn import StreamConn

def webull_login():
    #login to Webull
    wb = webull()
    loginInfo = False
    f = None
    try:
        f = open("token.txt", "r")
        loginInfo = json.load(f)
    except:
        print("First time login.")
    #If first time save login as token
    if not loginInfo:
        email = input('webull account email: ')
        password = input('webull account password: ')
        device = input('device linked to webull account: ')
        wb.get_mfa(email) #mobile number should be okay as well.
        code = input('Enter MFA Code : ')
        loginInfo = wb.login(email, password, device, code)
        f = open("token.txt", "w")
        f.write(json.dumps(loginInfo))
        f.close()
    else:
        wb.refresh_login()
        loginInfo = wb.login(email, password)

    conn = StreamConn(debug_flg=False)
    if not loginInfo['accessToken'] is None and len(loginInfo['accessToken']) > 1:
        conn.connect(loginInfo['uuid'], access_token=loginInfo['accessToken'])
    else:
        conn.connect(wb.did)






   