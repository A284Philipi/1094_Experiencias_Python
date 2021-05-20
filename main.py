total = int(0)
coelhos = int(0)
sapos = int(0)
ratos = int(0)
perc_coelho = float()
perc_rato = float()
perc_sapo = float()
casos = int(input())
for x in range(0, casos):
    a, b = input().split(" ")
    numero = int(a)
    tipo = str(b)
    if (tipo[0] == 'C'):
        coelhos = coelhos + numero
    elif (tipo[0] == 'R'):
        ratos = ratos + numero
    else:
        sapos = sapos + numero
total = sapos + ratos + coelhos
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
perc_coelho = (coelhos * 100) / total
perc_rato = (ratos * 100) / total
perc_sapo = (sapos * 100) / total
print("Percentual de coelhos: %.2f"%(perc_coelho) + " %")
print("Percentual de ratos: %.2f"%(perc_rato) + " %")
print("Percentual de sapos: %.2f"%(perc_sapo) + " %")