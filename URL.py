# coding: UTF-8
import time

__author__ = 'Administrator'
import cPAMIE
class URL:
    def __login__( txtUserMemberID, txtUserPwd,fp1):
        ie = cPAMIE.PAMIE()
        # ie.navigate("http://www.huazhu.com/login.aspx");
        # time.sleep(15);
        # ie.buttonClick("ibtnlogin");
        ie.navigate("http://activity.huazhu.com/WorldCup2014");
        ie.imageClick("id1");
        ie.textBoxSet("userLoginName", txtUserMemberID) ;
        ie.textBoxSet("userLoginPwd", txtUserPwd);
        ie.linkClick("linkUserLogin");
        ie.imageClick("id1");
        ie.imageClick("buttoncf_r1_c1");
        if(ie.divExists("voteSuccess")):
            fp1.write (txtUserMemberID+","+txtUserPwd);
        ie.navigate("http://www.huazhu.com/logout.aspx");
        ie.quit();
    if __name__=="__main__":
        path="./log.csv";
        path1="./login.csv";
        fp = open(path);
        fp1 = open(path1,'a');
        for lines in fp.readlines():
            line1,line2=lines.split(',');
            __login__(line1,line2,fp1);
        fp1.close();