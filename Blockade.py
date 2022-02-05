import copy

def proveraDimenzija(brVrsta:int,brKolona:int):
    if brVrsta<11:
        brVrsta=11
    elif brVrsta>22:
        brVrsta=22
    if brKolona<14:
        brKolona=14
    elif brKolona>28:
        brKolona=28
    return(brVrsta,brKolona)


def pocetno(brVrsta:int,brKolona:int,listaPozicja:list[tuple[int,int]],brZidova:int):
   (vrsta,kolona)= proveraDimenzija(brVrsta,brKolona)
   if brZidova<0 or brZidova>18:
       brZidova=9
   stanje=dict()
   listaPesaka=["X1","X2","O1","O2"]
   #oznaka pocetnih stanja
   listaPesaka1=["pX1","pX2","pO1","pO2"]

   stanje["sledeci"] = "X"
   
   for i in range(len(listaPozicja)):
       stanje[listaPesaka1[i]]=listaPozicja[i]
       stanje[listaPesaka[i]]=listaPozicja[i]
    
   stanje["dimX"]=vrsta
   stanje["dimY"]=kolona
   stanje["zidoviPlaviX"]=brZidova
   stanje["zidoviZeleniX"]=brZidova
   stanje["zidoviPlaviO"]=brZidova
   stanje["zidoviZeleniO"]=brZidova

   for i in range(vrsta):
       stanje[i]=dict()
  
  
   return stanje


def prikaziStanje(stanje:dict):
    matrica=[]
    for i in range(stanje["dimX"]*2-1):
        matrica.append([])
       
        for j in range(stanje["dimY"]*2-1):
            if i%2==0 and j%2==0:
                daLiJePrazno=True
                if(stanje["X1"]==(i/2,j/2) or stanje["X2"]==(i/2,j/2)):
                    matrica[i].append("x")
                    daLiJePrazno=False
                if(stanje["O1"]==(i/2,j/2) or stanje["O2"]==(i/2,j/2)):
                    matrica[i].append("o")
                    daLiJePrazno=False
                if daLiJePrazno:
                     matrica[i].append(" ")

            elif i%2==0 and j%2==1:
                
                 if str((j-1)//2)+'v' in stanje[i//2]:
                     
                     matrica[i].append("ǁ")

                 else :
                    matrica[i].append("|")
            elif i%2==1 and j%2==0:

                if str(j//2)+'h' in stanje[(i-1)//2] :
                    matrica[i].append("=")
                else:
                 matrica[i].append("-")
            else:
                 matrica[i].append(" ")

    prikaziMatricu(matrica)      
    
def daLiJeKraj(stanje:dict):
    if stanje["X1"]==stanje["pO1"] or stanje["X1"]==stanje["pO2"] or stanje["X2"]==stanje["pO1"] or stanje['X2']==stanje["pO2"]:
        return 1 #pobednik je x
    elif stanje["O1"]==stanje["pX1"] or stanje["O1"]==stanje["pX2"] or stanje["O2"]==stanje["pX1"] or stanje['O2']==stanje["pX2"]:
        return 2 #pobednik je o
    return 0 #nije kraj

def prikaziMatricu(matrica:list[list[str]]):
    print("   ",end="")
    for i in range(len(matrica[0])):
        if i==0:
            print("0",end="")
        if(i%2==0):
            print(str(hex(i//2).lstrip("0x")),end="")
        else:
            print(" ",end="")
    print()
    print("   ",end="")
    for i in range(len(matrica[0])):
        if i%2==0:
            print("=",end="")
        else:
            print(" ",end="")
    print()


    for i in range(len(matrica)):
        if i==0:
            print("0 ǁ",end="")
        elif i%2==0:
            print(str(hex(i//2).lstrip("0x"))+" ǁ",end="")
        else:
            print("   ",end="")
        for j in range(len(matrica[i])):
            print(matrica[i][j], end="")
        if i==0:
            print("ǁ 0",end="")
        elif i%2==0:
            print("ǁ "+str(hex(i//2).lstrip("0x")),end="")
            
        print()
    print("   ",end="")
    for i in range(len(matrica[0])):
        if i%2==0:
            print("=",end="")
        else:
            print(" ",end="")
    print()
    print("   ",end="")
    for i in range(len(matrica[0])):
        if i==0:
            print("0",end="")
        if(i%2==0):
            print(str(hex(i//2).lstrip("0x")),end="")
        else:
            print(" ",end="")
    print()
            
def koIgraPrvi(prvi, stanje):
    if prvi == True:
        stanje["covek"] = "X"
        stanje["racunar"] = "O"
    else:
        stanje["racunar"] = "X"
        stanje["covek"] = "O"


def promeniStanje(stanje:dict,pion:tuple[str,int],novaPozicija:tuple[int,int],noviZid:tuple[str,int,int]):
    if(daLiJePotezValidan(stanje,pion,novaPozicija,noviZid)):
       pesak=str(pion[0]).upper()+str(pion[1])
       stanje[pesak]=novaPozicija
       if (str(pion[0]).upper() == "X"):
            stanje["sledeci"] = "O"
       else: stanje["sledeci"] = "X"

       if(len(noviZid)==0):
           prikaziStanje(stanje)
           return stanje
       
       if(str(noviZid[0]).upper()=='Z'): #vertikalni
           if(stanje["zidoviZeleni"+str(pion[0]).upper()]>0):
               stanje[noviZid[1]][str(noviZid[2])+'v']=stanje["zidoviZeleni"+str(pion[0]).upper()]
               stanje[noviZid[1]+1][str(noviZid[2])+'v']=stanje["zidoviZeleni"+str(pion[0]).upper()]
               stanje["zidoviZeleni"+str(pion[0]).upper()]-=1
       elif(str(noviZid[0]).upper()=='P'): 
           if(stanje["zidoviPlavi"+str(pion[0]).upper()]>0):
               stanje[noviZid[1]][str(noviZid[2])+'h']=stanje["zidoviPlavi"+str(pion[0]).upper()]
               stanje[noviZid[1]][str(noviZid[2]+1)+'h']=stanje["zidoviPlavi"+str(pion[0]).upper()]
               stanje["zidoviPlavi"+str(pion[0]).upper()]-=1

    prikaziStanje(stanje)
   
    return stanje

        
def daLiJePotezValidan(stanje:dict,pion:tuple[str,int],novaPozicija:tuple[int,int],noviZid:tuple[str,int,int]):
    if stanje["sledeci"]!=pion[0]:
        return False
    if daLiJeNoviPionValidan(stanje,pion,novaPozicija)==False:
        return False
    if daLiJeNoviZidValidan(stanje,pion[0],noviZid)==False:
        return False
    potencijalnoStanje=kreirajNovoStanje(stanje,pion,novaPozicija,noviZid)
    if len(noviZid)>0 and brojKontakataZida(stanje,noviZid)>=2:
       
        if daLiJeNekoPocetnoPoljeBlokirano(potencijalnoStanje)==True:
             return False
   
    return True

def daLiSuGraniceTabelePrekoracene(stanje:dict,x:int,y:int):
    if x<0 or x>=stanje["dimX"] or y<0 or y>=stanje["dimY"]:
        return True
    return False


def daLiJeNoviPionValidan(stanje:dict,pion:tuple[str,int],novaPozicija:tuple[int,int]):
    novoX,novoY=novaPozicija
    #da li nova pozicija premasuje dimenzije table
    if novoX>=stanje["dimX"] or novoX<0 or novoY>=stanje["dimY"] or novoY<0:
        return False
    #da li pion pokusava da stane na zauzeto polje koje nije pocetno protivnicko polje
    if daLiJePionNaPolju(stanje,(novoX,novoY)) and not daLiJePoljeProtivnickoPocetno(pion[0],stanje,(novoX,novoY)):
        return False
    staroX,staroY=stanje[pion[0]+str(pion[1])]
    if novoX>staroX:
        directionX=1
    elif novoX==staroX:
        directionX=0
    else:
        directionX=-1
    if novoY>staroY:
        directionY=1
    elif novoY==staroY:
        directionY=0
    else:
        directionY=-1
    distance= abs(novoX-staroX)+abs(novoY-staroY)
    #da li pion pokusava da se pomeri za vise od dva polja
    if distance>2:
        return False
    #pion moze da se pomeri za jedno polje samo ako je blokiran od strane drugog presaka ili je to polje protivnicko pocetno
    #ako nije ispunjen jedan od ova dva uslova, potez je nelegalan
    elif distance==1:
        
        if not daLiJePionNaPolju(stanje,(novoX+directionX,novoY+directionY)) and not daLiJePoljeProtivnickoPocetno(pion[0],stanje,(novoX,novoY)):
            return False
    #provera da li do novog polja piona blokira zid
    offsetX=novoX-staroX
    offsetY=novoY-staroY
    #ako je novo polje dijagonalno od trenutnog
    if abs(offsetX)==1 and abs(offsetY)==1:
        if(daLiJeDijagonalnoPoljeBlokirano(stanje,(staroX,staroY),(novoX,novoY))):
            return False
    elif distance==1:
        if(daLiJeSusednoPoljeBlokirano(stanje,(staroX,staroY),(novoX,novoY))):
            return False
    elif distance==2:
       
        if daLiJeSusednoPoljeBlokirano(stanje,(staroX,staroY),(staroX+directionX,staroY+directionY)) or daLiJeSusednoPoljeBlokirano(stanje,(staroX+directionX,staroY+directionY),(novoX,novoY)):
            return False
    return True




def daLiJePionNaPolju(stanje:dict,polje:tuple[int,int]):
    if stanje["X1"]==polje or stanje["X2"]==polje or stanje["O1"]==polje or stanje["O2"]==polje:
        return True
    return False

def daLiJePoljeProtivnickoPocetno(igrac:str,stanje:dict,polje:tuple[int,int]):
    protivnix='pX' if igrac=='O' else 'pO'
    if stanje[protivnix+str(1)]==polje or stanje[protivnix+str(2)]==polje:
        return True
    return False

def daLiJeNoviZidValidan(stanje:dict,igrac:str,noviZid:tuple[str,int,int]):
    
   
    key1="zidoviPlavi"+igrac.upper()
    key2="zidoviZeleni"+igrac.upper()
    #igrac ima pravo da ne postavi zid samo ukoliko nema nijedan preostali
    if len(noviZid)==0:
        if stanje[key1]==0 and stanje[key2]==0:
            return True
        else:
            return False
    tip,x,y=noviZid
    tip=tip.lower()
    key=key1 if tip=='p' else key2
    tip='v' if tip=='z' else 'h'
    #igrac ne moze da postavi zid ukoliko ga nema
    if stanje[key]==0:
        return False
    #nextX i nextY su koordinate 'nastavka zida' posto zid zauzima dva polja
    nextX=x if tip=='h' else x+1
    nextY=y if tip=='v' else y+1
    if daLiSuGraniceTabelePrekoracene(stanje,x,y) or daLiSuGraniceTabelePrekoracene(stanje,nextX,nextY):
        return False
    #ukoliko na zeljenom mestu vec postoji zid, nije moguce tu postaviti zid
    if str(y)+tip in stanje[x] or str(nextY)+tip in stanje[nextX]:
        return False
    #ne sme se postaviti horizontalni preko vertikalnog zida (i obrnuto) tako da formiraju +
    x1=x
    y1=y
    zid1='v' if tip=='h' else 'h'
    x2=x if tip=='v' else x+1
    y2=y if tip=='h' else y+1
    zid2='v' if tip=='h' else 'h'
    if x1 in stanje and x2 in stanje and str(y1)+zid1 in stanje[x1] and str(y2)+zid2 in stanje[x2] and stanje[x1][str(y1)+zid1]==stanje[x2][str(y2)+zid2]:
        return False
    return True


def daLiJeSusednoPoljeBlokirano(stanje:dict,polje:tuple[int,int],susednoPolje:tuple[int,int]):
    x,y=polje
    sx,sy=susednoPolje
    offsetX=sx-x
    offsetY=sy-y
    if abs(offsetX)+abs(offsetY)!=1:
        return "polje nije susedno"
    zid='h' if abs(offsetX)>0 else 'v'
    zidX=x if offsetX>=0 else x-1
    zidY=y if offsetY>=0 else y-1
   
    if zidX in stanje and str(zidY)+zid in stanje[zidX]:
        return True
    return False

def daLiJeDijagonalnoPoljeBlokirano(stanje:dict,polje:tuple[int,int],dijagonalnoPolje:tuple[int,int]):
     x,y=polje
     sx,sy=dijagonalnoPolje
     offsetX=sx-x
     offsetY=sy-y
     if abs(offsetX)!=1 and abs(offsetY)!=1:
        return "polje nije susedno"
     zid='h' if abs(offsetX)>0 else 'v'
     zidX=x if offsetX>=0 else x-1
     zidY=y if offsetY>=0 else y-1
     
     #1. slucaj
     zid1X=x
     zid1Y=y if offsetY>=0 else y-1
     zid1='v'
     zid2X=x+offsetX
     zid2Y=y if offsetY>=0 else y-1
     zid2='v'

     if zid1X in stanje and str(zid1Y)+zid1 in stanje[zid1X] and zid2X in stanje and str(zid2Y)+zid2 in stanje[zid2X]:
         return True

     #2. slucaj
     zid1X=x if offsetX>=0 else x-1
     zid1Y=y
     zid1='h'
     zid2X=x if offsetX>=0 else x-1
     zid2Y=y+offsetY
     zid2='h'
     if zid1X in stanje and zid2X in stanje and str(zid1Y)+zid1 in stanje[zid1X] and str(zid2Y)+zid2 in stanje[zid2X]:
         return True

     #3. slucaj
     zid1X=x+offsetX
     zid1Y=y if offsetY>=0 else y-1
     zid1='v'
     zid2X=x if offsetX>=0 else x-1
     zid2Y=y+offsetY
     zid2='h'
     if zid1X in stanje and zid2X in stanje and str(zid1Y)+zid1 in stanje[zid1X] and str(zid2Y)+zid2 in stanje[zid2X]:
         return True
     #4. slucaj
     zid1X=x if offsetX>=0 else x-1
     zid1Y=y
     zid1='h'
     zid2X=x
     zid2Y=y if offsetY>=0 else y-1
     zid2='v'
     if zid1X in stanje and zid2X in stanje and str(zid1Y)+zid1 in stanje[zid1X] and str(zid2Y)+zid2 in stanje[zid2X]:
         return True
     return False

def kopirajStanje(stanje:dict):
    novostanje=dict()
    novostanje["dimX"]=stanje["dimX"]
    novostanje["dimY"]=stanje["dimY"]
    novostanje["zidoviPlaviX"]= stanje["zidoviPlaviX"]
    novostanje["zidoviZeleniX"]= stanje["zidoviZeleniX"]
    novostanje["zidoviPlaviO"]=stanje["zidoviPlaviO"]
    novostanje["zidoviZeleniO"]=stanje["zidoviZeleniO"]
    keys=["pX1","pX2","pO1","pO2","X1","X2","O1","O2","covek","racunar","sledeci"]
    for key in keys:
        novostanje[key]=stanje[key]
    for i in range(stanje["dimX"]):
       novostanje[i]=dict(stanje[i])
       #novostanje[i]=stanje[i].copy()
    #novostanje=stanje
    return novostanje   

def kreirajNovoStanje(stanje:dict,pion:tuple[str,int],novaPozicija:tuple[int,int],noviZid:tuple[str,int,int]):
    #novoStanje=dict()
    novoStanje=kopirajStanje(stanje)
    pesak=str(pion[0]).upper()+str(pion[1])

    novoStanje[pesak]=novaPozicija
    if (str(pion[0]).upper() == "X"):
        novoStanje["sledeci"] = "O"
    else: novoStanje["sledeci"] = "X"

    if len(noviZid)==0:
        return novoStanje

    if(str(noviZid[0]).upper()=='Z'): #vertikalni
         if(novoStanje["zidoviZeleni"+str(pion[0]).upper()]>0):
             novoStanje[noviZid[1]][str(noviZid[2])+'v']=novoStanje["zidoviZeleni"+str(pion[0]).upper()]
             novoStanje[noviZid[1]+1][str(noviZid[2])+'v']=novoStanje["zidoviZeleni"+str(pion[0]).upper()]
             novoStanje["zidoviZeleni"+str(pion[0]).upper()]-=1
    elif(str(noviZid[0]).upper()=='P'): 
        if(novoStanje["zidoviPlavi"+str(pion[0]).upper()]>0):
            novoStanje[noviZid[1]][str(noviZid[2])+'h']=novoStanje["zidoviPlavi"+str(pion[0]).upper()]
            novoStanje[noviZid[1]][str(noviZid[2]+1)+'h']=novoStanje["zidoviPlavi"+str(pion[0]).upper()]
            novoStanje["zidoviPlavi"+str(pion[0]).upper()]-=1

   

    #prikaziStanje(novoStanje)
    return novoStanje
def imaLiPionJosZidova(stanje:dict,pion:str):
    if stanje['zidoviPlavi'+pion.upper()]==0 and stanje['zidoviZeleni'+pion.upper()]==0:
        return False
    return True
def ListaMogucihStanjaBezZidova(stanje:dict,pion:str):
   
    svaStanja=list()
   
    pioni=[1,2]
  
   
    for igrac in pioni:
            x=stanje[pion.upper()+str(igrac)][0] #x
            y=stanje[pion.upper()+str(igrac)][1] #y
            moguciPokreti=[(x+2,y),(x,y+2),(x-2,y),(x,y-2),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1),(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
            for pokret in moguciPokreti:
                if daLiJeNoviPionValidan(stanje,(pion,igrac),pokret):
                     svaStanja.append(kreirajNovoStanje(stanje,(pion,igrac),pokret,()))
           
    return svaStanja
    
def ListaMogucihStanja(stanje:dict,pion:str):
    if not imaLiPionJosZidova(stanje,pion):
        return ListaMogucihStanjaBezZidova(stanje,pion)
    svaStanja=list()
    
    zidovi=['P','Z']
    pioni=[1,2]
 
    for xZ in range(stanje['dimX']):
        for yZ in range(stanje['dimY']):
            for z in zidovi:
                if not daLiJeNoviZidValidan(stanje,pion,(z,xZ,yZ)):# proveri da li je zid validan ako nije preskace se cela iteracija
                    # ako jeste onda se pokusava sa pesacima sve moguce pozicije
                    continue
                if brojKontakataZida(stanje,(z,xZ,yZ))>=2:#ako zid ima vise od dva kontakta proverava se da li zatvaraju neki put ili pocteno polje
                    potencijalnoStanje=kreirajNovoStanje(stanje,(pion,1),stanje[pion+str('1')],(z,xZ,yZ))
                    if daLiJeNekoPocetnoPoljeBlokirano(potencijalnoStanje)==True:
                       
                        continue
               
                for igrac in pioni:
                        x=stanje[pion.upper()+str(igrac)][0] #x
                        y=stanje[pion.upper()+str(igrac)][1] #y
                        moguciPokreti=[(x+2,y),(x,y+2),(x-2,y),(x,y-2),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1),(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
                        for pokret in moguciPokreti:
                            if daLiJeNoviPionValidan(stanje,(pion,igrac),pokret):
                                svaStanja.append(kreirajNovoStanje(stanje,(pion,igrac),pokret,(z,xZ,yZ)))

           
    return svaStanja

   

    return lista
def daLiPionMozeSticiDoTacke(obidjeni:set,krajnjaTacka,stanje,pion):
    trenutnaTacka=stanje[pion[0]+str(pion[1])]
    if trenutnaTacka==krajnjaTacka:
        return True
    if trenutnaTacka in obidjeni:
        return False
    #obidjeniN=obidjeni.copy()
    obidjeni.add(trenutnaTacka)
    #print(trenutnaTacka)
    x,y=trenutnaTacka
    moguciPokreti=[(x+2,y),(x,y+2),(x-2,y),(x,y-2),(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1)]
    for pozicija in moguciPokreti:
        novoStanje=copy.deepcopy(stanje)
        novoStanje[pion[0]+str(pion[1])]=pozicija
        if daLiJeNoviPionValidan(stanje,pion,pozicija):
            
             #print(moguciPokreti)
             if daLiPionMozeSticiDoTacke(obidjeni,krajnjaTacka,novoStanje,pion):
                return True
    return False

def daLiJeNekoPocetnoPoljeBlokirano(stanje):
    pioni=[('X',1),('X',2),('O',1),('O',2)]
    pocetna=[stanje["pX1"],stanje["pX2"],stanje["pO1"],stanje["pO2"]]
    for pion in pioni:
            if pion[0]=='X':
                ind1=2
                ind2=3
            else:
                ind1=0
                ind2=1
            if daLiPionMozeSticiDoTacke(set(),pocetna[ind1],stanje,pion)==False:
                
                return True
            if daLiPionMozeSticiDoTacke(set(),pocetna[ind2],stanje,pion)==False:
              
                return True
    return False

def brojKontakataZida(stanje:dict, zid:tuple[str,int,int]):
    kontakti=0
    tip,i,j=zid
    if zid[0]=='P':
        if(  str(j-1)+'h' in stanje[i]): #levo
            kontakti=kontakti+1
        if(str(j+2)+'h' in stanje[i]): #desno
            kontakti=kontakti+1
        if(i-1>=0 and str(j-1)+'v' in stanje[i-1]): #gore levo
            kontakti=kontakti+1
        if(i-1>=0 and str(j)+'v' in stanje[i-1]): #gore sredina
            kontakti=kontakti+1
        if(i-1>=0 and str(j+1)+'v' in stanje[i-1]): #gore desno
            kontakti=kontakti+1
        if(i+1<stanje["dimX"] and str(j-1)+'v' in stanje[i+1]): #dole levo
            kontakti=kontakti+1
        if(i+1<stanje["dimX"] and str(j)+'v' in stanje[i+1]): #dole sredina
            kontakti=kontakti+1
        if(i+1<stanje["dimX"] and str(j+1)+'v' in stanje[i+1]): #dole desno
            kontakti=kontakti+1
        if(j==0 or j==stanje["dimY"]-2): #granice table
            kontakti=kontakti+1
    if tip.upper()=='Z':
        if(i-1>=0 and str(j)+'v' in stanje[i-1]):
            kontakti=kontakti+1
        if(i+2<stanje["dimX"] and str(j)+'v' in stanje[i+2]):
             kontakti=kontakti+1
        if(i-1>=0  and str(j)+'h' in stanje[i-1]):
             kontakti=kontakti+1
        if(i-1>=0 and str(j+1)+'h' in stanje[i-1]):
            kontakti=kontakti+1
        if( str(j)+'h' in stanje[i]):
            kontakti=kontakti+1
        if(str(j+1)+'h' in stanje[i]):
             kontakti=kontakti+1
        if(i+1<stanje["dimX"] and str(j)+'h' in stanje[i+1]):
             kontakti=kontakti+1
        if(i+1<stanje["dimX"] and str(j+1)+'h' in stanje[i+1]):
            kontakti=kontakti+1
        if(i==0 or i==stanje["dimX"]-2):
            kontakti=kontakti+1
    return kontakti
    
    
import math
def nadjiNajboljiPotez(stanje,dubina):
    bestScore=math.inf if stanje["racunar"]=="O" else -math.inf
    bestState=None
   
    for s in ListaMogucihStanja(stanje,stanje["racunar"]):
      
        score=minimax(s,dubina-1,stanje["covek"],-math.inf,+math.inf)
      
        if stanje["racunar"]=='X' and score>bestScore:
            bestScore=score
            bestState=s

        elif stanje["racunar"]=='O' and score<bestScore:
            bestScore=score
            bestState=s
    return bestState

def minimax(stanje, dubina, pion:str, alpha , beta ):
    if(pion=='X'):
        moj_potez=True
    else:
        moj_potez=False
    if moj_potez:
        return max_value(stanje,pion, dubina, alpha, beta)
    else:
        return min_value(stanje,pion, dubina, alpha, beta)

def max_value(stanje,pion, dubina, alpha, beta):
    bestVal=-1000
    if dubina == 0 or daLiJeKraj(stanje):
        #print(stanje,(heuristika(stanje)))
        return heuristika(stanje)
    else:
        
        for s in ListaMogucihStanja(stanje,pion):
            noviPion='X' if pion=='O' else 'O'
          
            
            
            value = max(alpha,min_value(s,noviPion, dubina - 1, alpha, beta))
            bestVal=max(value,bestVal)
            alpha=max(alpha,bestVal)
            if alpha<= beta:
                break
    return bestVal

def min_value(stanje,pion, dubina, alpha, beta):
    #print(dubina)
    bestVal=+1000
    if dubina == 0 or daLiJeKraj(stanje):
        #print(stanje,(heuristika(stanje)))
        return heuristika(stanje)
    else:
        for s in ListaMogucihStanja(stanje,pion):
            noviPion='X' if pion=='O' else 'O'
         
            value = min(beta,max_value(s,noviPion, dubina - 1, alpha, beta))
            bestVal=min(bestVal,value)
            beta=min(bestVal,beta)
            if beta <= alpha:
                break
    return bestVal

import random
def proceni_stanje(stanje):
   
    #tapl=(stanje,random.randint(0,100))
    #print(tapl)
    return random.randint(0,100)

def krajIgre(stanje:dict, igrac):
    if(igrac == stanje["racunar"]):
        print("The game is over! Computer won. Better luck next time!")
    else: print("The game is over! You won! Congratulations!")

def covekProtivCoveka(stanje):
    stanje['covek']='X'
    stanje['racunar']='O'
    prikaziStanje(stanje)
    m=daLiJeKraj(stanje)
    igrac='X'
    stanje['sledeci']='X'
    while not m:
        print("Na redu je: "+stanje['sledeci'])
        print("Enter which pion you would like to move:")
        pesak = int(input())
        print("Enter row of pion:")
        pozicijaPesakaX = int(input())
        print("Enter column of pion:")
        pozicijaPesakaY = int(input())
        if imaLiPionJosZidova(stanje,igrac):
                    print("Enter which wall to put:")
                    tipZida = str(input())
                    print("Enter row of wall:")
                    pozicijaZidaX = int(input())
                    print("Enter column of wall:")
                    pozicijaZidaY = int(input())
                    noviZid=(tipZida, pozicijaZidaX, pozicijaZidaY)
                    validan=daLiJePotezValidan(stanje,(igrac,pesak),(pozicijaPesakaX,pozicijaPesakaY),noviZid)
                    promeniStanje(stanje, (igrac, pesak), (pozicijaPesakaX,pozicijaPesakaY), (tipZida, pozicijaZidaX, pozicijaZidaY))
        
        else:
                     noviZid=()
                     validan=daLiJePotezValidan(stanje,(igrac,pesak),(pozicijaPesakaX,pozicijaPesakaY),noviZid)
                     promeniStanje(stanje, (igrac, pesak), (pozicijaPesakaX,pozicijaPesakaY), ())
        if not validan:
            print("Potez nije validan, morate ponovo uneti potez")
        else:
            igrac='X' if igrac=='O' else 'O'
        m=daLiJeKraj(stanje)
    if m==1:
        print("pobedio je X igrac!")
    else:
        print("pobedio je O igrac!")       

def startujIgricuSaRacunarom(stanje):

    print("Do you want to play first? y/n")
    unos = str(input())
    if (unos == "y" or unos == "Y"):
        koIgraPrvi(True, stanje)
    else: koIgraPrvi(False, stanje)
    prikaziStanje(stanje)
    x = daLiJeKraj(stanje)
    while(x == 0):
        igrac = stanje["sledeci"]
        print(igrac)
        if(stanje["racunar"] != igrac):
            print("...It's your turn....")
            print("Enter which pion you would like to move:")
            pesak = int(input())
            print("Enter row of pion:")
            pozicijaPesakaX = int(input())
            print("Enter column of pion:")
            pozicijaPesakaY = int(input())
               
            if imaLiPionJosZidova(stanje,stanje['covek']):
                    print("Enter which wall to put:")
                    tipZida = str(input())
                    print("Enter row of wall:")
                    pozicijaZidaX = int(input())
                    print("Enter column of wall:")
                    pozicijaZidaY = int(input())
                    noviZid=(tipZida, pozicijaZidaX, pozicijaZidaY)
                    validan=daLiJePotezValidan(stanje,(igrac,pesak),(pozicijaPesakaX,pozicijaPesakaY),noviZid)
                    promeniStanje(stanje, (igrac, pesak), (pozicijaPesakaX,pozicijaPesakaY), (tipZida, pozicijaZidaX, pozicijaZidaY))
            else:
                     noviZid=()
                     validan=daLiJePotezValidan(stanje,(igrac,pesak),(pozicijaPesakaX,pozicijaPesakaY),noviZid)
                     promeniStanje(stanje, (igrac, pesak), (pozicijaPesakaX,pozicijaPesakaY), ())
                     
            while (not validan):
                print("The values ​​entered are not valid, please enter ​​again")
                print("Enter row of pion:")
                pozicijaPesakaX = int(input())
                print("Enter column of pion:")
                pozicijaPesakaY = int(input())
               
                if imaLiPionJosZidova(stanje,stanje['covek']):
                    print("Enter which wall to put:")
                    tipZida = str(input())
                    print("Enter row of wall:")
                    pozicijaZidaX = int(input())
                    print("Enter column of wall:")
                    pozicijaZidaY = int(input())
                    noviZid=(tipZida, pozicijaZidaX, pozicijaZidaY)
                    validan=daLiJePotezValidan(stanje,(igrac,pesak),(pozicijaPesakaX,pozicijaPesakaY),noviZid)
                    promeniStanje(stanje, (igrac, pesak), (pozicijaPesakaX,pozicijaPesakaY), (tipZida, pozicijaZidaX, pozicijaZidaY))
                else:
                     noviZid=()
                     validan=daLiJePotezValidan(stanje,(igrac,pesak),(pozicijaPesakaX,pozicijaPesakaY),noviZid)
                     promeniStanje(stanje, (igrac, pesak), (pozicijaPesakaX,pozicijaPesakaY), ())
                   

        else:
            print("...It's the computer's turn...") 
            if imaLiPionJosZidova(stanje,stanje['racunar']):
                novoStanje = nadjiNajboljiPotez(stanje, 1)
            else:
                novoStanje=nadjiNajboljiPotez(stanje,3)
            
            stanje = novoStanje
            prikaziStanje(stanje)
        x = daLiJeKraj(stanje)
        print(x)
        print(stanje)
    krajIgre(stanje, igrac)

def heuristika(stanje:dict): 
    #ako je X(max igrac) pobednik heuristika vraca +100, ako je O(min igrac) pobedio vraca -100
    if daLiJeKraj(stanje)==1:
        return +100
    elif daLiJeKraj(stanje)==2:
        return -100
  #pioni
    heuristika=0
    pioni=['X1','X2','O1','O2']
    for p in pioni:
        (x,y)=stanje[p]
        moguciPokreti=[(x+2,y),(x,y+2),(x-2,y),(x,y-2),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1),(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
        for pokret in moguciPokreti:
            if daLiJeNoviPionValidan(stanje,(p[0],p[1]),pokret):
                distance=abs(x-pokret[0])+abs(y-pokret[1])
                znak=1 if p[0]=='X' else -1
                if(daLiJePoljeProtivnickoPocetno(p[0],stanje,pokret)):
                    distance*=10
                heuristika+=znak*distance

    return heuristika
def ListaSvihstanjaBezZidova(stanje:dict,pion:str):
    sortingkeySign=0 if stanje['sledeci']=='X' else 1
    lista=ListaMogucihStanjaBezZidova(stanje,(pion,1))+ListaMogucihStanjaBezZidova(stanje,(pion,2))
    return lista.sort(False if sortingkeySign else True,heuristika)


    

stanje1=pocetno(11,14,[(4,4),(8,4),(4,11),(8,11)],3)
startujIgricuSaRacunarom(stanje1)
#covekProtivCoveka(stanje1)