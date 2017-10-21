class Nodo:
  def __init__(self,letra):
    self.pSig = None
    self.pAnt = None
    self.letra = letra
    self.occ = 0
    
  def setNext(self,p):
    self.pSig = p
  def setPrev(self,p):
    self.pAnt = p
  def getPSig(self):
    return self.pSig  
  def getLetra(self):
    return self.letra
  def getOcc4Sort(self):
    return self.occ  
  def getOcc(self):
    if self.occ == 0:
      return False
    else:
      return self.occ
  def InsertOcc(self):
    self.occ = self.occ + 1
  def DeleteOcc(self):
    self.occ = self.occ - 1

class Bag(object):
  def __init__(self):
    self.primero = None
    self.ultimo = None

  def Ordenar(self):
    aux = self.primero
    aux2 = self.primero.pSig
    while aux.pSig != None:
      if aux.getOcc4Sort() < aux2.getOcc4Sort():
        aux0 = aux2.pAnt
        aux.pAnt.pSig = aux.pSig
        aux2.pAnt = aux.pAnt
        aux.pAnt = aux.pSig
        aux.pSig = aux2.pSig
        aux2.pSig.pAnt = aux0
        aux2.pSig = aux0
        aux0 = None
      else:
        pass
      aux = aux.pSig
      aux2 = aux2.pSig

  def IsEmpty(self):
    self.Ordenar()
    if self.primero == self.ultimo == None:
      return True
    else:
      print ("Hay elementos en la Mochila")
      
  def Append(self,Nodo):
    if self.primero is None:
      self.primero=Nodo
      self.ultimo = self.primero
    else:
      self.ultimo.setNext(Nodo)
      Nodo.setPrev(self.ultimo)
      self.ultimo = Nodo
	
  def Buscar(self,letter):
    aux = self.primero
    while aux != None:
      if aux.getLetra() == letter:
        return aux
        break
      aux = aux.pSig

  def Insert (self,letter):    
    if self.Buscar(letter) == False:
      print ("Letra no encontrada")
    else:
      self.Buscar(letter).InsertOcc()
      self.Ordenar()

  def Ocurrences(self,letter):
    if self.Buscar(letter) == False:
      print ("0 Ocurrencias")
    else:
      print (self.Buscar(letter).getOcc())
    self.Ordenar()

  def Delete(self,letter):
    if self.Buscar(letter) == False:
      print ("Letra no encontrada")
    else:
      self.Buscar(letter).DeleteOcc()
    self.Ordenar()
     
  def DeleteNode(self,letter):
    if self.Buscar(letter) == False:
      print ("Letra no encontrada")
    else:
      y = self.Buscar(letter)
      y.pAnt.pSig = y.pSig
      y.pSig.pAnt = y.pAnt
      y.pSig = None
      y.pAnt = None
    self.Ordenar()

Mochila = Bag()

list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

for i in range(len(list)):
  Mochila.Append(Nodo(list[i]))

#Pasar argurento como char, EJ: Mochila.Insert('a')