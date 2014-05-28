# coding: UTF-8
import fileinput
import io
from locale import str
import os

__author__ = 'lidong'


def getDirList( p ):
    p = p.replace( "/","\\")
    if p[ -1] != "\\":
        p = p+"\\"
    a = os.listdir( p )
    for x in a:
       if(os.path.isfile( p + x )):
           a, b = os.path.splitext( p + x )
           if(0<b.find("bak")):
             print (p + x)
             os.remove( p + x)
       elif(os.path.isdir( p + x )): #.svn
           if(0<( p + x ).find(".svn")):
              for (p,d,f) in os.walk( p + x):
                 if p.find('.svn')>0:
                      print (p + x)
                      os.popen('rd /s /q %s'%p)
           else :
               getDirList(p + x)

def createFile( f ):
    if(os.path.isfile(f)):
        a_file = io.open( f, encoding='utf-8')
        print(a_file.readline())
    else :

        return

while 1==1:
    print ( getDirList( "D:\project" ) )
