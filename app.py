#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:06:39 2019
@author: steven
"""

from firebase import firebase
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pyknow import * 

app = Flask(__name__)
Bootstrap(app)

#Se conecta al dataset de firebase

def get_connection():
    data = firebase.FirebaseApplication('https://enfermedadesdb-3b95a.firebaseio.com/', None)
    return data
    

#Obtiene los datos de la Enfermedad --> Gripa

def get_Gripa():
    con = get_connection()
    dataset = con.get('/Enfermedades/0', None)
    return dataset
def get_GripaSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/0/Sintomas', None)
    return dataset

#Obtiene los datos de la Enfermedad --> Neumonia

def get_Neumonia():
    con = get_connection()
    dataset = con.get('/Enfermedades/1', None)
    return dataset
def get_NeumoniaSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/1/Sintomas', None)
    return dataset

#Obtiene los datos de la Enfermedad --> Tuberculosis

def get_Tuberculosis():
    con = get_connection()
    dataset = con.get('/Enfermedades/2', None)
    return dataset
def get_TuberculosisSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/2/Sintomas', None)
    return dataset

#Obtiene los datos de la Enfermedad --> Diabetes

def get_Diabetes():
    con = get_connection()
    dataset = con.get('/Enfermedades/3', None)
    return dataset
def get_DiabetesSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/3/Sintomas', None)
    return dataset

#Obtiene los datos de la Enfermedad --> Gastritis

def get_Gastritis():
    con = get_connection()
    dataset = con.get('/Enfermedades/4', None)
    return dataset
def get_GastritisSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/4/Sintomas', None)
    return dataset
    
#==================================Definimos los hechos============================================

class Sintoma(Fact):
    pass

class Enfermedad(Fact):
    pass


#===========================Se Obtienen las enfermedades y sintomas=======================================

Gripa = get_Gripa()
GripaSint = get_GripaSint()

e100 = Gripa['100']
s101 = GripaSint['101']
s102 = GripaSint['102']
s103 = GripaSint['103']
s104 = GripaSint['104']
s105 = GripaSint['105']
r100 = Gripa['http']


Neumonia = get_Neumonia()
NeumoniaSint = get_NeumoniaSint()

e200 = Neumonia['200']
s201 = NeumoniaSint['201']
s202 = NeumoniaSint['202']
s203 = NeumoniaSint['203']
s204 = NeumoniaSint['204']
s205 = NeumoniaSint['205']
r200 = Neumonia['http']

Tuberculosis = get_Tuberculosis()
TuberculosisSint = get_TuberculosisSint()

e300 = Tuberculosis['300']
s301 = TuberculosisSint['301']
s302 = TuberculosisSint['302']
s303 = TuberculosisSint['303']
s304 = TuberculosisSint['304']
s305 = TuberculosisSint['305']
r300 = Tuberculosis['http']

Diabetes = get_Diabetes()
DiabetesSint = get_DiabetesSint()

e400 = Diabetes['400']
s401 = DiabetesSint['401']
s402 = DiabetesSint['402']
s403 = DiabetesSint['403']
s404 = DiabetesSint['404']
s405 = DiabetesSint['405']
r400 = Diabetes['http']

Gastritis = get_Gastritis()
GastritisSint = get_GastritisSint()

e500 = Gastritis['500']
s501 = GastritisSint['501']
s502 = GastritisSint['502']
s503 = GastritisSint['503']
s504 = GastritisSint['504']
s505 = GastritisSint['505']
r500 = Gastritis['http']



class DiagnosticoEnfermedades(KnowledgeEngine):
    
            
    @Rule(Sintoma(descripcion= s101 and s102 and s103 or s104 or s105 or s504 or s304 or s202 or s303))
    def enfermedad_1(self):
        self.declare(Enfermedad(codigo=100, recom=r100, tipo=e100))  
        
        
        
    @Rule(Sintoma(descripcion= s201 and s202 and s203 or s204 or s205  or s301 or s504 or s303 or s102))
    def enfermedad_2(self):
        self.declare(Enfermedad(codigo=200, recom=r200, tipo=e200)) 
        
        
        
    @Rule(Sintoma(descripcion= s301 and s302 and s303 or s304 or s305 or s504 or s104 or s201 or s202))
    def enfermedad_3(self):
        self.declare(Enfermedad(codigo=300, recom=r300, tipo=e300)) 
        
        
        
    @Rule(Sintoma(descripcion= s401 and s402 and s403 and s404 and s405))
    def enfermedad_4(self):
        self.declare(Enfermedad(codigo=400, recom=r400, tipo=e400))
        
        
        
    @Rule(Sintoma(descripcion= s501 and s502 and s503 or s504 or s505 or s305 or s102 or s303 or s202))
    def enfermedad_5(self):
        self.declare(Enfermedad(codigo=500, recom=r500, tipo=e500)) 
        



@app.route('/')
def index():
    return render_template('index.html')

    

@app.route('/diagnostico', methods=['POST'])
def Diagnostico():
    
    #===========================Capturamos de los selects=======================================
    
    sinto1 = request.form['sint1']


    sinto2 = request.form['sint2']

    
    sinto3 = request.form['sint3']

    
    sinto4 = request.form['sint4']
        

    sinto5 = request.form['sint5']
    
    set2 = set()

    set2.add(sinto1)
    set2.add(sinto2)
    set2.add(sinto3)
    set2.add(sinto4)
    set2.add(sinto5)
    
    
    set2=list(set2)
    
    
    """for i in range(len(set2)):
        a = set2[i]
        print(a)"""
    
    #lista1 = [sinto1, sinto2, sinto3, sinto4, sinto5]
    
    if (len(set2) == 1):
        sinto1 = set2[0]
    elif (len(set2) == 2):
        sinto1 = set2[0]
        sinto2 = set2[1]
    elif (len(set2) == 3):
        sinto1 = set2[0]
        sinto2 = set2[1]
        sinto3 = set2[2]
    elif (len(set2) == 4):
        sinto1 = set2[0]
        sinto2 = set2[1]
        sinto3 = set2[2]
        sinto4 = set2[3]
    else:
        sinto1 = set2[0]
        sinto2 = set2[1]
        sinto3 = set2[2]
        sinto4 = set2[3]
        sinto5 = set2[4]
    
    
    print('-----------------------------------------------------------------------------------------------')
    
    
    for i in range(len(set2)):
        print('Síntoma ',i + 1, ': ' + set2[i])
        
    
    print('-----------------------------------------------------------------------------------------------')
    
    
    print(set2)
    
    
    #===========================Se cargan los sintomas a los hechos =======================================
       
    watch('RULES', 'FACTS')
    diagnostico = DiagnosticoEnfermedades()
    diagnostico.reset()
    

    diagnostico.declare(Sintoma(descripcion=sinto1))
    diagnostico.declare(Sintoma(descripcion=sinto2))
    diagnostico.declare(Sintoma(descripcion=sinto3))
    diagnostico.declare(Sintoma(descripcion=sinto4))
    diagnostico.declare(Sintoma(descripcion=sinto5))

    
    diagnostico.run()
    enfermedad = diagnostico.facts

    for d in enfermedad:
        if (type(enfermedad[d]) == Enfermedad):
            tipo = enfermedad[d]['tipo']
            recomendacion = enfermedad[d]['recom']
            resultado = {'resul':tipo}  
            recom = {'reco':recomendacion}
            
    
    print('La enfermedad es: ' + tipo)
       

    return render_template('diagnostico.html', resultado=resultado, recom=recom)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500

if __name__ == '__main__':
    app.run()
