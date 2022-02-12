aux, fibo, quant = 1, 0, int(input('Quantidades de números na sequência: '))
for cont in range(0, quant):
   print(fibo, end=', ' if cont != quant-1 else '.\n')
   fibo, aux = fibo+aux, fibo  
