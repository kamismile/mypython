# coding: UTF-8
import time

__author__ = 'Administrator'
import cPAMIE
class URL:
    def __login__( txtUserMemberID, txtUserPwd):
        ie = cPAMIE.PAMIE()
        # ie.navigate("http://www.huazhu.com/login.aspx");
        # time.sleep(15);
        # ie.buttonClick("ibtnlogin");
        ie.navigate("http://activity.huazhu.com/WorldCup2014");
        ie.imageClick("id1");
        ie.textBoxSet("userLoginName", txtUserMemberID) ;
        ie.textBoxSet("userLoginPwd", txtUserPwd);
        ie.linkClick("linkUserLogin");
        print(txtUserMemberID+"-------"+txtUserPwd);
        ie.imageClick("id1");
        # ie.quit();
    if __name__=="__main__":
        path="./log.csv";
        fp = open(path);
        for lines in fp.readlines():
            line1,line2=lines.split(',');
            __login__(line1,line2);
