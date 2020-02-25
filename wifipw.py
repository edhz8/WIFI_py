import os
import time
def main():
    currnet_wlan=os.popen("netsh wlan show interfaces")
    listOf_currnet_wlan=currnet_wlan.readlines() # 명령줄을 읽어서 sss에 리스트로 저장하는 부분 
    if listOf_currnet_wlan[0] == '무선 자동 구성 서비스(wlansvc)가 실행되고 있지 않습니다.\n':
        print("인터페이스를 불러올 수 없습니다.")
        return
    else:
        lineOf_current_wlan=listOf_currnet_wlan[8] # 명령줄중 현재 SSID를 알려주는줄 ex)SSID                   : Hollys_5G
        ssid_name=lineOf_current_wlan[29:(len(lineOf_current_wlan)-1)] # 윗줄에서 SSID의 이름부분만 추출 ex) "Hollys_5G" len(s)-1을 해야 엔터가 포함안된다.
        print("ID:"+ssid_name)
        
    comm="netsh wlan show profile name="+ssid_name+" key=clear" # 특정 네트워크의 프로필을 보여주는 명령어
    current_prof=os.popen(comm)# 윗부분과 비슷한 원리로 찾아감
    listOf_current_prof=current_prof.readlines()
    if listOf_current_prof[0][:5] == '시스템에서':
        print('패스워드를 찾을 수 없습니다.')
        return
    else:
        lineOf_current_prof=listOf_current_prof[32]
        password=lineOf_current_prof[23:(len(lineOf_current_prof)-1)]
        print("PW:"+password)
main()
os.system('pause')