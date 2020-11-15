import xlsxwriter
from Distribuicoes import *

workbook = xlsxwriter.Workbook('dadosDistribuicoes.xlsx')
sheet = workbook.add_worksheet()

sheet.set_column('A:A', 30)
sheet.set_column('B:B', 30)
sheet.set_column('C:C', 30)
sheet.set_column('D:D', 30)
sheet.set_column('E:E', 30)

# Write some simple text.
sheet.write(0, 0, 'UniformeDiscreta(Via do Carro)')
sheet.write(0, 1, 'BinomialDiscreta(Tipo de Carro)')
sheet.write(0, 2, 'ExponencialContinua(Frequencia Carro)')
sheet.write(0, 3, 'UniformeContinua(Velocidade Carro)')
sheet.write(0, 4, 'NormalContinua(Salto Coelho)')

for i in range(1000):
    sheet.write(i+1, 0, uniformeDisc(0,5))
    sheet.write(i+1, 1, binomial(2, 0.4))
    sheet.write(i+1, 2, expo(300, 450))
    
    #se calhar e necessario gerar para cada via
    sheet.write(i+1, 3, uniformeCont(3, 3.2))
    
    sheet.write(i+1, 4, normal(300, 100))

workbook.close()

