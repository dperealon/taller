# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os

from conexion import bd
from fpdf import FPDF

def imprimir(fac,mat,dni):
    pdf = FPDF()
    pdf.add_page()
    header(pdf,fac,mat,dni)
    precio = cuerpo(pdf,fac)
    footage(pdf,precio)
    pdf.output('factura.pdf','F')
    os.system('/usr/bin/evince factura.pdf')
    
        
def header(pdf,fac,mat,dni):
    pdf.set_font('Arial','B',12)
    pdf.cell(60,10,'TALLERAUTO',0,1,'C')
    pdf.set_font('Arial','',10)
    pdf.cell(60,10,'Calle Senra, 12  Marin (Pontevedra)',0,1,'L')
    pdf.cell(60,10,'36911 Tlfo: 986 882 211-656 565 918',0,1,'L')
    pdf.image('car.png',170,10,25,25,'png','')
    pdf.line(5,40,200,40)
    pdf.set_font('Times','B',12)
    pdf.cell(180,10,'Factura numero: %s ' % fac,0,1,'R')
    pdf.cell(60,10,'DATOS CLIENTE:',0,1,'L')
    cursor = bd.cursor()
    cursor.execute(""" SELECT dnicli, apelcli, nomcli, dircli, poblic, procli, cpcli FROM clientes WHERE dnicli=?""", (dni,))
    datos = cursor.fetchall()
    for fila in datos:
        pdf.cell(30,10,'%s' % fila[1],0,0,'L')
        pdf.cell(30,10,'%s' % fila[2],0,1,'L')
        pdf.cell(20,10,'%s' % fila[3],0,0,'L')
        pdf.cell(50,10,'%s' % fila[4],0,0,'R')
        pdf.cell(90,10,'Matricula Vehiculo: %s' %mat,0,1,'R')
        pdf.cell(30,10,'%s' % fila[6],0,0,'L')
        pdf.cell(60,10,'%s' % fila[5],0,0,'L')
    pdf.line(5,90,200,90)
    
    
def cuerpo(pdf,fac):
    pdf.cell(60,10,'',0,1,'L')
    pdf.cell(50,10,'ID Venta',0,0,'L')
    pdf.cell(100,10,'CONCEPTO',0,0,'C')
    pdf.cell(30,10,'IMPORTE',0,1,'R')
    pdf.line(5,90,200,90)
    cursor = bd.cursor()
    cursor.execute(""" SELECT * FROM ventas WHERE idfac=? """, (fac,))
    datos = cursor.fetchall()
    precios = 0
    for fila in datos:
        pdf.cell(50,10,'%s' % fila[0],1,0,'L')
        pdf.cell(100,10,'%s' % fila[2],1,0,'L')
        pdf.cell(30,10,'%s' % fila[3],1,1,'R')
        precio = int(fila[3])
        precios = precios+precio
    pdf.line(5,90,200,90)
    return precios
    
        
def calculoIva(precio):
    precio = (precio*23)/100
    return precio

def footage(pdf,precios):
    iva = calculoIva(precios)
    total = iva+precios
    pdf.cell(60,10,'',0,0,'L')
    pdf.cell(60,10,'',0,1,'L')
    pdf.line(5,90,200,90)
    pdf.cell(30,10,'TOTAL(sin iva)',0,0,'L')
    pdf.cell(30,10,'%s' % precios,0,0,'L')
    pdf.cell(30,10,'IVA(23%): ',0,0,'L')
    pdf.cell(30,10,'%s' % iva,0,0,'L')
    pdf.cell(30,10,'TOTAL',0,0,'L')
    pdf.cell(30,10,'%s' % total,0,1,'L')