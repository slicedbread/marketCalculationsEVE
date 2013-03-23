import urllib2

#################################
#THIS IS A WORK IN PROGRESS
#I'm learning to use XML, Python, Git, and to a lesser extent Ubuntu while writing this.
#
#if you are a fellow EVE player shoot "Rosenrot x" or "Slicedbread x" a message in game
#and I can help explain how to use the code/would love to hear your feedback!
#
#
#disclaimer: I'm not responsible for loss of ISK if something goes wrong! 
#(IDK if a disclamer is necessary, but I guess it doesn't hurt.)
#
#################################

#http://dev.eve-central.com/evec-api/start
#forge code 10000002 

#tri=34,pye=35,mex=36,iso=37,nocx=38,meg=40,zyd=39
#set of mineral prices
#http://api.eve-central.com/api/marketstat?typeid=34&typeid=35&&typeid=36&typeid=37&typeid=38&typeid=40&typeid=39&usesystem=30000142


#Veldspar=1230, Scordite=1228, Pyroxeres=1224, Plagioclase=18, Omber=1227, Kernite=20, Jaspet=1226, Hemorphite=1231, Gneiss=1229, Arkonor=22

#ore
#http://api.eve-central.com/api/marketstat?typeid=1230&typeid=1228&typeid=1224&typeid=18&typeid=1227&typeid=20&typeid=1226&typeid=1231&typeid=1229&typeid=22&usesystem=30000142

#ore@
#http://api.eve-central.com/api/marketstat?typeid=17471&typeid=17464&typeid=17460&typeid=17456&typeid=17868&typeid=17453&typeid=17449&typeid=17445&typeid=17866&typeid=17426&usesystem=30000142

#ore#
#http://api.eve-central.com/api/marketstat?typeid=17470&typeid=17463&typeid=17459&typeid=17455&typeid=17867&typeid=17452&typeid=17448&typeid=17444&typeid=17865&typeid=17425&usesystem=30000142


#these needed to be hardcoded because there wasnt a good way to mathmatically calculate the values









#constants

mineralPerOre=[#devide the mineral amounts by the ore batch size
# tritanium    pyerite     mexallon    isogen      nocxium     megacyte    zydrine
[
[(1000.0/333),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0)],#Veldspar 0
[( 833.0/333),(416.0/333),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0)],#Scordite 1
[( 844.0/333),( 59.0/333),(120.0/333),(      0.0),( 11.0/333),(      0.0),(      0.0)],#Pyroxeres 2
[( 256.0/333),(512.0/333),(256.0/333),(      0.0),(      0.0),(      0.0),(      0.0)],#Plagioclase 3
[( 307.0/500),(123.0/500),(      0.0),(307.0/500),(      0.0),(      0.0),(      0.0)],#Omber 4
[( 386.0/400),(      0.0),(773.0/400),(386.0/400),(      0.0),(      0.0),(      0.0)],#Kernite 5
[( 259.0/500),(259.0/500),(518.0/500),(      0.0),(259.0/500),(      0.0),(  8.0/500)],#Jaspet 6
[( 212.0/500),(      0.0),(      0.0),(212.0/500),(424.0/500),(      0.0),( 28.0/500)],#Hemorphite 7
[( 171.0/400),(      0.0),(171.0/400),(343.0/400),(      0.0),(      0.0),(171.0/400)],#Gneiss 8
[( 300.0/200),(      0.0),(      0.0),(      0.0),(      0.0),(333.0/200),(166.0/200)],#Arkonor 9
],

[
[(1050.0/333),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0)],#Veldspar 0
[( 875.0/333),(437.0/333),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0)],#Scordite 1
[( 886.0/333),( 62.0/333),(126.0/333),(      0.0),( 12.0/333),(      0.0),(      0.0)],#Pyroxeres 2
[( 269.0/333),(538.0/333),(269.0/333),(      0.0),(      0.0),(      0.0),(      0.0)],#Plagioclase 3
[( 322.0/500),(129.0/500),(      0.0),(322.0/500),(      0.0),(      0.0),(      0.0)],#Omber 4
[( 405.0/400),(      0.0),(812.0/400),(405.0/400),(      0.0),(      0.0),(      0.0)],#Kernite 5
[( 272.0/500),(272.0/500),(544.0/500),(      0.0),(272.0/500),(      0.0),(  8.0/500)],#Jaspet 6
[( 223.0/500),(      0.0),(      0.0),(223.0/500),(445.0/500),(      0.0),( 29.0/500)],#Hemorphite 7
[( 180.0/400),(      0.0),(180.0/400),(360.0/400),(      0.0),(      0.0),(180.0/400)],#Gneiss 8
[( 315.0/200),(      0.0),(      0.0),(      0.0),(      0.0),(350.0/200),(175.0/200)],#Arkonor 9
],

[
[(1100.0/333),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0)],#Veldspar 0
[( 916.0/333),(458.0/333),(      0.0),(      0.0),(      0.0),(      0.0),(      0.0)],#Scordite 1
[( 928.0/333),( 65.0/333),(133.0/333),(      0.0),( 13.0/333),(      0.0),(      0.0)],#Pyroxeres 2
[( 282.0/333),(563.0/333),(282.0/333),(      0.0),(      0.0),(      0.0),(      0.0)],#Plagioclase 3
[( 338.0/500),(135.0/500),(      0.0),(338.0/500),(      0.0),(      0.0),(      0.0)],#Omber 4
[( 424.0/400),(      0.0),(850.0/400),(424.0/400),(      0.0),(      0.0),(      0.0)],#Kernite 5
[( 259.0/500),(285.0/500),(570.0/500),(      0.0),(285.0/500),(      0.0),(  9.0/500)],#Jaspet 6
[( 233.0/500),(      0.0),(      0.0),(233.0/500),(466.0/500),(      0.0),( 31.0/500)],#Hemorphite 7
[( 188.0/400),(      0.0),(188.0/400),(377.0/400),(      0.0),(      0.0),(188.0/400)],#Gneiss 8
[( 330.0/200),(      0.0),(      0.0),(      0.0),(      0.0),(366.0/200),(183.0/200)],#Arkonor 9
]]

oreName=[
"Veldspar   ",
"Scordite   ",
"Pyroxeres  ",
"Plagioclase",
"Omber      ",
"Kernite    ",
"Jaspet     ",
"Hemorphite ",
"Gneiss     ",
"Arkonor    "]

salesTax=.009
brokerFee=.005799



#escape char?
char = '%'

#end constants


#variable arrays

#             tri  pye  mex  iso  nocx mega zyd 
mineralPrice=[0.00,0.00,0.00,0.00,0.00,0.00,0.00]

rawProfitPerOre=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

oreSellMin=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

oreBuyMax=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

oreSellMinOrder=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

brokerFeePerOre=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

netProfit=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

netProfitBroker=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

#end variable arrays

def populateMinerals():
  "Pulls mineral prices and removes sales tax"
  data = urllib2.urlopen('http://api.eve-central.com/api/marketstat?typeid=34&typeid=35&&typeid=36&typeid=37&typeid=38&typeid=40&typeid=39&usesystem=30000142&minQ=1000')
  import xml.etree.ElementTree as ET
  tree = ET.parse(data)
  root = tree.getroot()
  for i in range(0,7):
    mineralPrice[i]=float(root[0][i][0].find('max').text)
    mineralPrice[i]-=(mineralPrice[i]*salesTax)    
  print "taxed minerals populated"
 

def populateRawProfit():
  "populates profits without taking into account ore prices"
  for t in range(0,3): 
    for i in range(0,10):
      for m in range(0,7):
        rawProfitPerOre[t][i]+=(mineralPerOre[t][i][m]*mineralPrice[m])
  print "raw profit populated"


def populateOrePrices():
  "populates ore prices"
  #this url is reeaaallyyy long
  data = urllib2.urlopen('http://api.eve-central.com/api/marketstat?typeid=1230&typeid=1228&typeid=1224&typeid=18&typeid=1227&typeid=20&typeid=1226&typeid=1231&typeid=1229&typeid=22&typeid=17470&typeid=17463&typeid=17459&typeid=17455&typeid=17867&typeid=17452&typeid=17448&typeid=17444&typeid=17865&typeid=17425&typeid=17471&typeid=17464&typeid=17460&typeid=17456&typeid=17868&typeid=17453&typeid=17449&typeid=17445&typeid=17866&typeid=17426&usesystem=30000142&minQ=1000')
  import xml.etree.ElementTree as ET
  tree = ET.parse(data)
  root = tree.getroot()

  for i in range(0,10):
    oreSellMin[0][i%10]=float(root[0][i][1].find('min').text)
  for i in range(10,20):
    oreSellMin[1][i%10]=float(root[0][i][1].find('min').text)
  for i in range(20,30):
    oreSellMin[2][i%10]=float(root[0][i][1].find('min').text)
  print "ore prices populated"


  for i in range(0,10):
    oreBuyMax[0][i%10]=float(root[0][i][0].find('max').text)
  for i in range(10,20):
    oreBuyMax[1][i%10]=float(root[0][i][0].find('max').text)
  for i in range(20,30):
    oreBuyMax[2][i%10]=float(root[0][i][0].find('max').text)
  print "buy max populated"


  for i in range(0,10):
    brokerFeePerOre[0][i%10]=oreBuyMax[0][i%10]*brokerFee
  for i in range(10,20):
    brokerFeePerOre[1][i%10]=oreBuyMax[1][i%10]*brokerFee
  for i in range(20,30):
    brokerFeePerOre[2][i%10]=oreBuyMax[2][i%10]*brokerFee
  print "broker fee helper array"


#  for i in range(0,10):
#    oreBuyMax[0][i%10]=oreBuyMax[0][i%10]+oreBuyMax[0][i%10]
#  for i in range(10,20):
#    oreBuyMax[1][i%10]=oreBuyMax[1][i%10]+oreBuyMax[1][i%10]
#  for i in range(20,30):
#    oreBuyMax[2][i%10]=oreBuyMax[2][i%10]+oreBuyMax[2][i%10]
#  print "ore price brokered populated"  


def populateNetProft():
  "populates net profits"
  for x in range (0,3):
    for i in range (0,10):
      netProfit[x][i]=rawProfitPerOre[x][i]-oreSellMin[x][i]
      netProfitBroker[x][i]=rawProfitPerOre[x][i]-oreBuyMax[x][i]-brokerFeePerOre[x][i]

  print "net profits populated"


def printTheShit(array):
  "this prints all of the lines"
  for i in range(0,10):
    print oreName[i]+"=   %.3f \t 5"%(array[0][i])+char+"=%.3f \t10"%(array[1][i])+char+"=%.3f"%(array[2][i])    

def populateAll():
  "Calls all the populate methods"
  populateMinerals()
  populateRawProfit()
  populateOrePrices()
  populateNetProft()

  print "all populated"





print "\n"
populateAll()
print "\nraw profit"
printTheShit(rawProfitPerOre)
print "\nore buy max"
printTheShit(oreBuyMax)
print "\nnet profit brokered"
printTheShit(netProfitBroker)

print "\n\nend of new code\n\n"




