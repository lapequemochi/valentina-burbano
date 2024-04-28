class Curso:
    
  
    """---------------
    #Metodos
    ---------------"""
    

    __notas=[ 4, 5, 3, 2 ,3.5 ,1 ,0 , 4, 5, 5, 5, 4.3, 4.2 ]
    
    def TotalNotas(self):
        return len(self.nota)

    def estudiantesAprobados(self):
        
        indice=0
        
        while indice <12:
            if self.nota[indice] >= 3.0:
                indice +=1
            else:
                self.nota[indice] <= 5.0
                indice +=1
        else:
            self.nota[indice]
            indice += 1
            
    def promedioNotas(self):
        suma=0.0
        indice=0
        while indice<12:
            suma+=self.__notas[indice]
            indice+=1
        return suma/indice
    
    def CalcularMayorNota(self):
        notaMayor=0
        notaMenor=0
        for nota in self.__notas:
            if nota > notaMayor:
                notaMenor = notaMayor
        return notaMayor
    
    def HacerCurva(self):
        limite = self.__notas < 4.75
        for nota in range(12):
            if self.__notas <= limite:
                nota == self.notas * 0.5
        return print("se aumenta el 0.5 a todas las notas sin que pase de 5.0")
    
    def CalcularCantidadAprobados(self):
        aprobados =0
        indice=0
        while indice<12:
            if(self.__notas[indice]>=3.0)and(self.__notas[indice]>=5.0):
                aprobados+=1
            indice+=1
            
        return aprobados
    
    def CalcularCantidadAprobados2(self):
        aprobados = 0
        
        for indice in range(12):
            if(self.__notas[indice]>=3.0)and(self.__notas[indice]>=5.0):
                aprobados+=1
            
        return aprobados
    
    def CalcularCantidadAprobados3(self):
        aprobados=0
        for nota in self.__notas:
            if nota >=3.0 and nota <=5.0:
                aprobados+=1
        return aprobados
    
    def CambiarNotas(self):
        notasModificadas = 0
        for nota in self.__notas:
            if nota >= 4.0:
                nota = nota - 0.5
            elif nota < 2.0:
                nota = nota + 0.5
            notasModificadas= notasModificadas =+ [nota]
        return notasModificadas
    
    def darMenorNota(self):
        menorNota = nota[0]
        for nota in self.__notas:
            if nota < menorNota:
                menorNota = nota   
        return menorNota
    
    def darRangoConMasNotas(self):
        rango1 = 0
        rango2 = 0
        rango3 = 0
        for nota in self.__notas:
            if 0.0 < nota < 2.0:
                rango1 = rango1 + 1
            elif 2.0 <= nota < 3.5:
                rango2 = rango2 + 1
            elif 3.5 <= nota <= 5.0:
                rango3 = rango3 + 1
                
        if rango1 > rango2 and rango1 > rango3:
            return 1
        elif rango2 > rango1 and rango2 > rango3:
            return 2
        elif rango3 > rango1 and rango3 > rango2:
            return 3
        else:
            
            return None
        
    def HayAlgunCinco_uno(self):
        i=0
        hayCinco = False
        
        while (i < len(self.__notas)) and not hayCinco:
            if (self.notas[i] ==5):
                hayCinco=True
                
            i+=1
            
        return hayCinco
    
    def HayAlgunCinco_dos(self):
        hayCinco = False
        
        for i in range(len(self.__notas)):
            if (self.__notas[1]== 5):
                hayCinco=True
                break
        
        return hayCinco
    
    def HayAlgunCinco_tres(self):
        hayCinco =False
        for nota in self.__notas:
            if nota ==5:
                hayCinco=True
                break
            
        return hayCinco

    def Nota(self):
        indice=0
        notasIguales = 2.5
        while indice <12: 
            if self.__nota[indice] == 1.5:
               self.__notas[indice] = notasIguales
            indice+=1
            
        return notasIguales
    
    def Posicion(self):
        indice=0
        for i in range(len(self.__notas)):
            if self.__notas[i] == 5:
                indice+=1
            if indice ==3:
                return 1
        
            return -1
                
    def RemplazarNotas(self):
        for i in range(len(self.__notas)):
            if self.__notas[i] == 0.0:
                self.__notas[i] > 3.0
                break
    
    def CalcularMinimoNotas(self):
        suma=0
        minimoNotas=0
        for nota in self.__notas:
                suma += nota
                minimoNotas += 1
                if suma > 30:
                    return minimoNotas
                
        return -1
            
    def NotaMasRecurrente(self):
        notaMasRecurrente = 0
        cantidadOcurrencias=0
        for nota in self.__notas:
            contador=0
            for nota2 in self.__notas:
                if nota2 == nota:
                    contador+=1
                
            if contador >cantidadOcurrencias:
                notaMasRecurrente=nota
                cantidadOcurrencias=contador
                
        return notaMasRecurrente
    
    def CalcularNota(self):
        notaMedia=0
        cantidad = (len(self.__notas)/2)
        for nota in self.__notas:
            calcular=0
            for nota2 in self.__notas:
                if nota2 == nota:
                    calcular+=1
                
            if cantidad == nota:
                notaMedia = nota
                notaMedia >= self.__notas
        return notaMedia
            