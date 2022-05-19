# from ctypes import alignment
from tkinter import *
from turtle import color

import numpy as np
import matplotlib.pyplot as plt

# from tkinter import ttk


# from turtle import bgcolor
# from reportlab.pdfgen import canvas
vetor_final = list()

def soma_fluxo_caixa():
    blank.delete(0, END)

    ############################ Função Caixa 1

    soma_venda_final = 0
    soma_salario_final = 0
    soma_impostos_final = 0
    soma_fornecedores_final = 0

    soma_ativos_final = 0
    soma_aquisicao_ativos_final = 0
    soma_dividendos_final = 0

    soma_emprestimo_final = 0
    soma_pagamento_dividendos_final = 0
    soma_amortizacao_final = 0


    # Saldo inicial que começará o programa
    saldo_inicial1 = saldo_anterior1.get()
    if saldo_inicial1 == '':
        saldo_inicial1 = 0

    saldo_inicial_periodo1['text'] = saldo_inicial1
    resultado_final_TOTAL_INICIAL['text'] = saldo_inicial1
    total_anterior_final['text'] = saldo_inicial1

    vendas = vendas1.get()
    salarios = salarios1.get()
    fornecedores = fornecedores1.get()
    impostos = impostos1.get()

    # Este é para caso a entrada esteja limpa
    if vendas == '':
        vendas = 0
    if salarios == '':
        salarios = 0
    if fornecedores == '':
        fornecedores = 0
    if (impostos) == '':
        impostos = 0

    ############ Variáveis para impressões dos valores finais
    soma_venda_final += float(vendas)
    soma_salario_final += float(salarios)
    soma_impostos_final += float(impostos)
    soma_fornecedores_final += float(fornecedores)

    #############################################
    soma_saldo_fo1 = float(vendas) - float(salarios) - float(fornecedores) - float(impostos)
    
    saldo_caixa1["text"] = f'{soma_saldo_fo1}'

    vendas_ativos = vendas_ativos1.get()
    aquisicao_ativos = aquisicao_ativos1.get()
    recebimentos_dividendos = recebimentos_dividendos1.get()

    if vendas_ativos == '':
        vendas_ativos = 0
    if aquisicao_ativos == '':
        aquisicao_ativos = 0
    if recebimentos_dividendos == '':
        recebimentos_dividendos = 0
    
    soma_ativos_final += float(vendas_ativos)
    soma_aquisicao_ativos_final += float(aquisicao_ativos)
    soma_dividendos_final += float(recebimentos_dividendos)

    soma_saldo_fi1 = float(vendas_ativos) - float(aquisicao_ativos) + float(recebimentos_dividendos)
    saldo_investimentos1["text"] = f'{soma_saldo_fi1}'

    aquisicao_emprestimo = aquisicao_emprestimo1.get()
    pagamentos_dividendos = pagamentos_dividendos1.get()
    amortizacao = amortizacao1.get()

    if aquisicao_emprestimo == '':
        aquisicao_emprestimo = 0
    if pagamentos_dividendos == '':
        pagamentos_dividendos = 0
    if amortizacao == '':
        amortizacao = 0

    soma_emprestimo_final += float(aquisicao_emprestimo)
    soma_pagamento_dividendos_final += float(pagamentos_dividendos)
    soma_amortizacao_final += float(amortizacao)

    soma_saldo_ff1 = float(aquisicao_emprestimo) - float(pagamentos_dividendos) - float(amortizacao)
    saldo_financiamento1["text"] = f'{soma_saldo_ff1}'

    somas_saldos_fluxos1 = soma_saldo_fo1 + soma_saldo_fi1 + soma_saldo_ff1
    saldo_final_periodo1["text"] = f'{somas_saldos_fluxos1}'

    resultado_periodo1 = float(somas_saldos_fluxos1) + float(saldo_inicial1)
    resultado_final_periodo1['text'] = f'{resultado_periodo1}'

    ############################ Função Caixa 2

    # Saldo inicial que começará o valor do período 1

    saldo_inicial2 = resultado_periodo1
    if saldo_inicial2 == '':
        saldo_inicial2 = 0

    saldo_anterior2['text'] = saldo_inicial2
    saldo_inicial_periodo2['text'] = saldo_inicial2

    vendas = vendas2.get()
    salarios = salarios2.get()
    fornecedores = fornecedores2.get()
    impostos = impostos2.get()

    # Este é para caso a entrada esteja limpa
    if vendas == '':
        vendas = 0
    if salarios == '':
        salarios = 0
    if fornecedores == '':
        fornecedores = 0
    if (impostos) == '':
        impostos = 0
    
    ############ Variáveis para impressões dos valores finais
    soma_venda_final += float(vendas)
    soma_salario_final += float(salarios)
    soma_impostos_final += float(impostos)
    soma_fornecedores_final += float(fornecedores)
    
    #############################################
    soma_saldo_fo2 = float(vendas) - float(salarios) - float(fornecedores) - float(impostos)
    saldo_caixa2["text"] = f'{soma_saldo_fo2}'

    vendas_ativos = vendas_ativos2.get()
    aquisicao_ativos = aquisicao_ativos2.get()
    recebimentos_dividendos = recebimentos_dividendos2.get()

    if vendas_ativos == '':
        vendas_ativos = 0
    if aquisicao_ativos == '':
        aquisicao_ativos = 0
    if recebimentos_dividendos == '':
        recebimentos_dividendos = 0
    
    soma_ativos_final += float(vendas_ativos)
    soma_aquisicao_ativos_final += float(aquisicao_ativos)
    soma_dividendos_final += float(recebimentos_dividendos)

    soma_saldo_fi2 = float(vendas_ativos) - float(aquisicao_ativos) + float(recebimentos_dividendos)
    saldo_investimentos2["text"] = f'{soma_saldo_fi2}'

    aquisicao_emprestimo = aquisicao_emprestimo2.get()
    pagamentos_dividendos = pagamentos_dividendos2.get()
    amortizacao = amortizacao2.get()

    if aquisicao_emprestimo == '':
        aquisicao_emprestimo = 0
    if pagamentos_dividendos == '':
        pagamentos_dividendos = 0
    if amortizacao == '':
        amortizacao = 0
    
    soma_emprestimo_final += float(aquisicao_emprestimo)
    soma_pagamento_dividendos_final += float(pagamentos_dividendos)
    soma_amortizacao_final += float(amortizacao)

    soma_saldo_ff2 = float(aquisicao_emprestimo) - float(pagamentos_dividendos) - float(amortizacao)
    saldo_financiamento2["text"] = f'{soma_saldo_ff2}'

    somas_saldos_fluxos2 = soma_saldo_fo2 + soma_saldo_fi2 + soma_saldo_ff2
    saldo_final_periodo2["text"] = f'{somas_saldos_fluxos2}'

    resultado_periodo2 = float(somas_saldos_fluxos2) + float(saldo_inicial2)
    resultado_final_periodo2['text'] = f'{resultado_periodo2}'

    ############################ Função Caixa 3

    # Saldo inicial recebido do período 2

    saldo_inicial3 = resultado_periodo2
    if saldo_inicial3 == '':
        saldo_inicial3 = 0

    saldo_anterior3['text'] = saldo_inicial3
    saldo_inicial_periodo3['text'] = saldo_inicial3

    vendas = vendas3.get()
    salarios = salarios3.get()
    fornecedores = fornecedores3.get()
    impostos = impostos3.get()

    # Este é para caso a entrada esteja limpa
    if vendas == '':
        vendas = 0
    if salarios == '':
        salarios = 0
    if fornecedores == '':
        fornecedores = 0
    if (impostos) == '':
        impostos = 0

    ############ Variáveis para impressões dos valores finais
    soma_venda_final += float(vendas)
    soma_salario_final += float(salarios)
    soma_impostos_final += float(impostos)
    soma_fornecedores_final += float(fornecedores)
    #############################################
    soma_saldo_fo3 = float(vendas) - float(salarios) - float(fornecedores) - float(impostos)
    saldo_caixa3["text"] = f'{soma_saldo_fo3}'

    vendas_ativos = vendas_ativos3.get()
    aquisicao_ativos = aquisicao_ativos3.get()
    recebimentos_dividendos = recebimentos_dividendos3.get()

    if vendas_ativos == '':
        vendas_ativos = 0
    if aquisicao_ativos == '':
        aquisicao_ativos = 0
    if recebimentos_dividendos == '':
        recebimentos_dividendos = 0
    
    soma_ativos_final += float(vendas_ativos)
    soma_aquisicao_ativos_final += float(aquisicao_ativos)
    soma_dividendos_final += float(recebimentos_dividendos)

    soma_saldo_fi3 = float(vendas_ativos) - float(aquisicao_ativos) + float(recebimentos_dividendos)
    saldo_investimentos3["text"] = f'{soma_saldo_fi3}'

    aquisicao_emprestimo = aquisicao_emprestimo3.get()
    pagamentos_dividendos = pagamentos_dividendos3.get()
    amortizacao = amortizacao3.get()

    if aquisicao_emprestimo == '':
        aquisicao_emprestimo = 0
    if pagamentos_dividendos == '':
        pagamentos_dividendos = 0
    if amortizacao == '':
        amortizacao = 0

    soma_emprestimo_final += float(aquisicao_emprestimo)
    soma_pagamento_dividendos_final += float(pagamentos_dividendos)
    soma_amortizacao_final += float(amortizacao)


    soma_saldo_ff3 = float(aquisicao_emprestimo) - float(pagamentos_dividendos) - float(amortizacao)
    saldo_financiamento3["text"] = f'{soma_saldo_ff3}'

    somas_saldos_fluxos3 = soma_saldo_fo3 + soma_saldo_fi3 + soma_saldo_ff3
    saldo_final_periodo3["text"] = f'{somas_saldos_fluxos3}'

    resultado_periodo3 = float(somas_saldos_fluxos3) + float(saldo_inicial3)
    resultado_final_periodo3['text'] = f'{resultado_periodo3}'

    ############################ Função Caixa 4

    # Saldo inicial recebido do período 3

    saldo_inicial4 = resultado_periodo3
    if saldo_inicial4 == '':
        saldo_inicial4 = 0

    saldo_anterior4['text'] = saldo_inicial4
    saldo_inicial_periodo4['text'] = saldo_inicial4

    vendas = vendas4.get()
    salarios = salarios4.get()
    fornecedores = fornecedores4.get()
    impostos = impostos4.get()

    # Este é para caso a entrada esteja limpa
    if vendas == '':
        vendas = 0
    if salarios == '':
        salarios = 0
    if fornecedores == '':
        fornecedores = 0
    if impostos == '':
        impostos = 0

    ############ Variáveis para impressões dos valores finais
    soma_venda_final += float(vendas)
    soma_salario_final += float(salarios)
    soma_impostos_final += float(impostos)
    soma_fornecedores_final += float(fornecedores)
    
    #############################################

    soma_saldo_fo4 = float(vendas) - float(salarios) - float(fornecedores) - float(impostos)
    saldo_caixa4["text"] = f'{soma_saldo_fo4}'

    vendas_ativos = vendas_ativos4.get()
    aquisicao_ativos = aquisicao_ativos4.get()
    recebimentos_dividendos = recebimentos_dividendos4.get()

    if vendas_ativos == '':
        vendas_ativos = 0
    if aquisicao_ativos == '':
        aquisicao_ativos = 0
    if recebimentos_dividendos == '':
        recebimentos_dividendos = 0
    
    soma_ativos_final += float(vendas_ativos)
    soma_aquisicao_ativos_final += float(aquisicao_ativos)
    soma_dividendos_final += float(recebimentos_dividendos)

    soma_saldo_fi4 = float(vendas_ativos) - float(aquisicao_ativos) + float(recebimentos_dividendos)
    saldo_investimentos4["text"] = f'{soma_saldo_fi4}'

    aquisicao_emprestimo = aquisicao_emprestimo4.get()
    pagamentos_dividendos = pagamentos_dividendos4.get()
    amortizacao = amortizacao4.get()

    if aquisicao_emprestimo == '':
        aquisicao_emprestimo = 0
    if pagamentos_dividendos == '':
        pagamentos_dividendos = 0
    if amortizacao == '':
        amortizacao = 0

    soma_emprestimo_final += float(aquisicao_emprestimo)
    soma_pagamento_dividendos_final += float(pagamentos_dividendos)
    soma_amortizacao_final += float(amortizacao)

    soma_saldo_ff4 = float(aquisicao_emprestimo) - float(pagamentos_dividendos) - float(amortizacao)
    saldo_financiamento4["text"] = f'{soma_saldo_ff4}'

    somas_saldos_fluxos4 = soma_saldo_fo4 + soma_saldo_fi4 + soma_saldo_ff4
    saldo_final_periodo4["text"] = f'{somas_saldos_fluxos4}'

    resultado_periodo4 = float(somas_saldos_fluxos4) + float(saldo_inicial4)
    resultado_final_periodo4['text'] = f'{resultado_periodo4}'


############################ Somas Finais
    vendas_caixafinal['text'] = f'{soma_venda_final}'
    salarios_caixafinal['text'] = f'{soma_salario_final}'
    fornecedores_caixafinal['text'] = f'{soma_fornecedores_final}'
    impostos_caixafinal['text'] = f'{soma_impostos_final}'
    
    aquisicao_ativosfinal['text']  = f'{soma_aquisicao_ativos_final}'
    vendas_ativofinal['text'] = f'{soma_ativos_final}'
    recebimento_dividendofinal['text'] = f'{soma_dividendos_final}'

    aquisicao_emprestimofinal['text'] = f'{soma_emprestimo_final}'
    pagamentos_dividendosfinal['text'] = f'{soma_pagamento_dividendos_final}'
    amortizacaofinal['text'] = f'{soma_amortizacao_final}'

    soma_saldo_caixafinal = soma_venda_final - soma_salario_final - soma_fornecedores_final - soma_impostos_final
    soma_saldo_investimentofinal2 = soma_ativos_final - soma_aquisicao_ativos_final + soma_dividendos_final
    soma_saldo_investimentofinal = soma_emprestimo_final - soma_pagamento_dividendos_final - soma_amortizacao_final

  
    saldo_caixafinal['text'] = f'{soma_saldo_caixafinal}'
    saldo_investimentofinal2['text'] = f'{soma_saldo_investimentofinal2}'
    saldo_investimentofinal['text'] = f'{soma_saldo_investimentofinal}'

    soma_resultado_final_TOTAL_PERIODO = soma_saldo_caixafinal + soma_saldo_investimentofinal2 + soma_saldo_investimentofinal
    soma_teste = soma_saldo_caixafinal + soma_saldo_investimentofinal2 + soma_saldo_investimentofinal
  
    soma_resultado_final_TOTAL2 = float(saldo_inicial1) + soma_teste
  
    resultado_final_TOTAL_PERIODO['text'] = f'{soma_resultado_final_TOTAL_PERIODO}'
    resultado_final_TOTAL['text'] = f'{soma_resultado_final_TOTAL2}'

    vetor_final.append([soma_saldo_fo1, soma_saldo_fo2, soma_saldo_fo3, soma_saldo_fo4])
    vetor_final.append([soma_saldo_ff1, soma_saldo_ff2, soma_saldo_ff3, soma_saldo_ff4])
    vetor_final.append([soma_saldo_fi1, soma_saldo_fi2, soma_saldo_fi3, soma_saldo_fi4])

    

##################################### Gráficos
def graficos():
    # set width of bars
    barWidth = 0.25
 
    # set heights of bars
    bars1 = vetor_final[0]
    bars2 = vetor_final[1]
    bars3 = vetor_final[2]
 
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    ax = plt.gca()
    ax.set_xticklabels([])
    # remove the extra tick on the negative bar
    ax.set_xticks([idx for (idx, x) in enumerate(bars1) if x > 0])
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
 
    # Make the plot
    plt.bar(r1, bars1, color='#3089DB', width=barWidth, edgecolor='white',  label='Fluxo de Caixa Operacional')
    plt.bar(r2, bars2, color='#DB9A30', width=barWidth, edgecolor='white', label='Fluxo de Investimentos')
    plt.bar(r3, bars3, color='#8F5F11', width=barWidth, edgecolor='white', label='Fluxo de Financiamento')
 
    # Add xticks on the middle of the group bars
    plt.title('Resultado do Fluxo de Caixa por Período' )
    for bars in ax.containers:
        ax.bar_label(bars)
 
    # Create legend & Show graphic
    plt.legend()
    plt.show()
    
# função para zerar
def limpar_dados():
    for nome in lista_nome:
        nome.delete(0, END)

    for nome1 in listaL:
        nome1["text"] = f'{0.0}'
    #positivo_negativo()

# fluxo de caixa    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


main = Tk()
main.title('Fluxo de Caixa')
main.geometry('900x700')
main.resizable(False, False)

############Saldo Anterior e período ###################################

saldo_anterior = Label(main, text="Saldo Anterior", fg="black", bg = '#09E3B0', width=22, anchor=W, font=("Arial", 8))
saldo_anterior.grid(column=0, row=1, padx=13, pady=4)

saldo_anterior1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
saldo_anterior1.grid(column=1, row=1, padx=13, pady=4)
saldo_anterior2 = Label(main, text=f'0.0', bg = '#09E3B0', justify=CENTER, font=("Arial", 8), width=15)
saldo_anterior2.grid(column=2, row=1, padx=13, pady=4)
saldo_anterior3 = Label(main, text=f'0.0', bg = '#09E3B0', justify=CENTER, font=("Arial", 8), width=15)
saldo_anterior3.grid(column=3, row=1, padx=13, pady=4)
saldo_anterior4 = Label(main, text=f'0.0', bg = '#09E3B0', justify=CENTER, font=("Arial", 8), width=15)
saldo_anterior4.grid(column=4, row=1, padx=13, pady=4)

total_anterior = Label(main, text="Total", fg="black", bg="#FF3333", justify=CENTER, width=15, font=("Arial", 8))
total_anterior.grid(column=5, row=0, padx=13, pady=4)
############ Fluxo de Caixa ###################################


fluxo_caixa = Label(main, text="Fluxo de Caixa Operacional", fg="black", bg='#018E72', width=22, anchor=W,
                    font=("Arial", 8))
fluxo_caixa.grid(column=0, row=2, padx=13, pady=4)
periodo1 = Label(main, text="1° Período", bg= '#007A62', width=15, font=("Arial", 8))
periodo1.grid(column=1, row=0, pady=4, padx=13)
periodo2 = Label(main, text="2° Período", bg= '#007A62', width=15, font=("Arial", 8))
periodo2.grid(column=2, row=0, pady=4, padx=13)
periodo3 = Label(main, text="3° Período", bg= '#007A62', width=15, font=("Arial", 8))
periodo3.grid(column=3, row=0, pady=4, padx=13)
periodo4 = Label(main, text="4° Período", bg= '#007A62', width=15, font=("Arial", 8))
periodo4.grid(column=4, row=0, pady=4, padx=13)

Label(main, text=" Vendas ", fg="black", bg="#e6e6e6", width=22, anchor=W, font=("Arial", 8)).grid(row=3, sticky=W,
                                                                                                   pady=4, padx=13)
Label(main, text=" Salários ", fg="black", bg="#99CCFF", width=22, anchor=W, font=("Arial", 8)).grid(row=4, sticky=W,
                                                                                                     pady=4, padx=13)
Label(main, text=" Fornecedores ", fg="black", bg="#99CCFF", width=22, anchor=W, font=("Arial", 8)).grid(row=5,
                                                                                                         sticky=W,
                                                                                                         pady=4,
                                                                                                         padx=13)
Label(main, text=" Impostos", fg="black", bg="#99CCFF", width=22, anchor=W, font=("Arial", 8)).grid(row=6, sticky=W,
                                                                                                    pady=4, padx=13)
Label(main, text=" Saldo Fluxo Operacional", fg="black", bg = '#09E3B0', width=22, anchor=W, font=("Arial", 8)).grid(
    row=7, sticky=W, pady = 10, padx=13)

############################################################ 1° PERÍODO ENTRADAS
vendas1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas1.grid(column=1, row=3, padx=13, pady=4)
salarios1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
salarios1.grid(column=1, row=4, padx=13, pady=4)
fornecedores1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
fornecedores1.grid(column=1, row=5, padx=13, pady=4)
impostos1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
impostos1.grid(column=1, row=6, padx=13, pady=4)

saldo_caixa1 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_caixa1.grid(column=1, row=7, padx=13, pady = 10)

############################################################################# 2° PERÍODO ENTRADAS
vendas2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas2.grid(column=2, row=3, padx=13, pady=4)
salarios2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
salarios2.grid(column=2, row=4, padx=13, pady=4)
fornecedores2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
fornecedores2.grid(column=2, row=5, padx=13, pady=4)
impostos2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
impostos2.grid(column=2, row=6, padx=13, pady=4)

saldo_caixa2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_caixa2.grid(column=2, row=7, padx=13, pady = 10)

############################################################################# 3° PERÍODO ENTRADAS

vendas3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas3.grid(column=3, row=3, padx=13, pady=4)
salarios3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
salarios3.grid(column=3, row=4, padx=13, pady=4)
fornecedores3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
fornecedores3.grid(column=3, row=5, padx=13, pady=4)
impostos3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
impostos3.grid(column=3, row=6, padx=13, pady=4)

saldo_caixa3 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_caixa3.grid(column=3, row=7, padx=13, pady = 10)

############################################################################# 4° PERÍODO ENTRADAS

vendas4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas4.grid(column=4, row=3, padx=13, pady=4)
salarios4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
salarios4.grid(column=4, row=4, padx=13, pady=4)
fornecedores4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
fornecedores4.grid(column=4, row=5, padx=13, pady=4)
impostos4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
impostos4.grid(column=4, row=6, padx=13, pady=4)

saldo_caixa4 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_caixa4.grid(column=4, row=7, padx=13, pady = 10)

############### totais finais #

vendas_caixafinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
vendas_caixafinal.grid(column=5, row=3, padx=13, pady=4)
salarios_caixafinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
salarios_caixafinal.grid(column=5, row=4, padx=13, pady=4)
fornecedores_caixafinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
fornecedores_caixafinal.grid(column=5, row=5, padx=13, pady=4)
impostos_caixafinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
impostos_caixafinal.grid(column=5, row=6, padx=13, pady=4)
saldo_caixafinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
saldo_caixafinal.grid(column=5, row=7, padx=13, pady=10)

total_anterior_final = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
total_anterior_final.grid(column=5, row=1, padx=13, pady=4)

############ Fluxo de Investimentos  ###################################

fluxo_investimento = Label(main, text="Fluxo de Investimentos", fg="black", bg='#018E72', width=22, anchor=W,
                           font=("Arial", 8))
fluxo_investimento.grid(column=0, row=10, padx=13, pady=4)

Label(main, text=" Venda de Ativos", fg="black", bg="#e6e6e6", width=22, anchor=W, font=("Arial", 8)).grid(row=11,
                                                                                                           sticky=W,
                                                                                                           pady=4,
                                                                                                           padx=13)
Label(main, text=" Aquisição de Ativos ", fg="black", bg="#99CCFF", width=22, anchor=W, font=("Arial", 8)).grid(row=12,
                                                                                                                sticky=W,
                                                                                                                pady=4,
                                                                                                                padx=13)
Label(main, text=" Recebimentos de dividendos", fg="black", bg="#e6e6e6", width=22, anchor=W, font=("Arial", 8)).grid(
    row=13, sticky=W, pady=4, padx=13)
Label(main, text=" Saldo Fluxo Investimentos", fg="black", bg = '#09E3B0', width=22, anchor=W, font=("Arial", 8)).grid(
    row=14, sticky=W, pady = 10, padx=13)

##################################################################### 1° PERIODO ENTRADA

vendas_ativos1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas_ativos1.grid(column=1, row=11, padx=13, pady=4)
aquisicao_ativos1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_ativos1.grid(column=1, row=12, padx=13, pady=4)
recebimentos_dividendos1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
recebimentos_dividendos1.grid(column=1, row=13, padx=13, pady=4)
saldo_investimentos1 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_investimentos1.grid(column=1, row=14, padx=13, pady = 10)

vendas_ativofinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
vendas_ativofinal.grid(column=5, row=11, padx=13, pady=4)
aquisicao_ativosfinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
aquisicao_ativosfinal.grid(column=5, row=12, padx=13, pady=4)
recebimento_dividendofinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
recebimento_dividendofinal.grid(column=5, row=13, padx=13, pady=4)
saldo_investimentofinal2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
saldo_investimentofinal2.grid(column=5, row=14, padx=13, pady=10)

##################################################################### 2° PERIODO ENTRADA

vendas_ativos2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas_ativos2.grid(column=2, row=11, padx=13, pady=4)
aquisicao_ativos2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_ativos2.grid(column=2, row=12, padx=13, pady=4)
recebimentos_dividendos2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
recebimentos_dividendos2.grid(column=2, row=13, padx=13, pady=4)
saldo_investimentos2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_investimentos2.grid(column=2, row=14, padx=13, pady = 10)

##################################################################### 3° PERIODO ENTRADA

vendas_ativos3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas_ativos3.grid(column=3, row=11, padx=13, pady=4)
aquisicao_ativos3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_ativos3.grid(column=3, row=12, padx=13, pady=4)
recebimentos_dividendos3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
recebimentos_dividendos3.grid(column=3, row=13, padx=13, pady=4)
saldo_investimentos3 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_investimentos3.grid(column=3, row=14, padx=13, pady = 10)

##################################################################### 4° PERIODO ENTRADA

vendas_ativos4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
vendas_ativos4.grid(column=4, row=11, padx=13, pady=4)
aquisicao_ativos4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_ativos4.grid(column=4, row=12, padx=13, pady=4)
recebimentos_dividendos4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
recebimentos_dividendos4.grid(column=4, row=13, padx=13, pady=4)
saldo_investimentos4 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_investimentos4.grid(column=4, row=14, padx=13, pady = 10)

############ Fluxo de Financiamento ###################################

fluxo_financiamento = Label(main, text="Fluxo de Financiamento", fg="black", bg='#018E72', width=22, anchor=W, font=("Arial", 8))
fluxo_financiamento.grid(column=0, row=18, padx=13, pady=4)
Label(main, text=" Aquisição de Empréstimos", fg="black", bg="#e6e6e6", width=22, anchor=W, font=("Arial", 8)).grid(
    row=19, sticky=W, pady=4, padx=13)
Label(main, text=" Pagamento de Dividendos ", fg="black", bg="#99CCFF", width=22, anchor=W, font=("Arial", 8)).grid(
    row=20, sticky=W, pady=4, padx=13)
Label(main, text=" Amortização", fg="black", bg="#99CCFF", width=22, anchor=W, font=("Arial", 8)).grid(row=21, sticky=W,
                                                                                                       pady=4, padx=13)
Label(main, text=" Saldo Fluxo Financiamento", fg="black", bg = '#09E3B0', width=22, anchor=W, font=("Arial", 8)).grid(
    row=22, sticky=W, pady = 10, padx=13)

##################################################################### 1° PERIODO ENTRADA

aquisicao_emprestimo1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_emprestimo1.grid(column=1, row=19, padx=13, pady=4)
pagamentos_dividendos1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
pagamentos_dividendos1.grid(column=1, row=20, padx=13, pady=4)
amortizacao1 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
amortizacao1.grid(column=1, row=21, padx=13, pady=4)
saldo_financiamento1 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_financiamento1.grid(column=1, row=22, padx=13, pady = 10)

##################################################################### 2° PERIODO ENTRADA

aquisicao_emprestimo2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_emprestimo2.grid(column=2, row=19, padx=13, pady=4)
pagamentos_dividendos2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
pagamentos_dividendos2.grid(column=2, row=20, padx=13, pady=4)
amortizacao2 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
amortizacao2.grid(column=2, row=21, padx=13, pady=4)
saldo_financiamento2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_financiamento2.grid(column=2, row=22, padx=13, pady = 10)

##################################################################### 3° PERIODO ENTRADA

aquisicao_emprestimo3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_emprestimo3.grid(column=3, row=19, padx=13, pady=4)
pagamentos_dividendos3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
pagamentos_dividendos3.grid(column=3, row=20, padx=13, pady=4)
amortizacao3 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
amortizacao3.grid(column=3, row=21, padx=13, pady=4)
saldo_financiamento3 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_financiamento3.grid(column=3, row=22, padx=13, pady = 10)

##################################################################### 4° PERIODO ENTRADA

aquisicao_emprestimo4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
aquisicao_emprestimo4.grid(column=4, row=19, padx=13, pady=4)
pagamentos_dividendos4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
pagamentos_dividendos4.grid(column=4, row=20, padx=13, pady=4)
amortizacao4 = Entry(main, justify=CENTER, font=("Arial", 8), width=15)
amortizacao4.grid(column=4, row=21, padx=13, pady=4)
saldo_financiamento4 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#09E3B0')
saldo_financiamento4.grid(column=4, row=22, padx=13, pady = 10)

################ Finais

aquisicao_emprestimofinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
aquisicao_emprestimofinal.grid(column=5, row=19, padx=13, pady=4)
pagamentos_dividendosfinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
pagamentos_dividendosfinal.grid(column=5, row=20, padx=13, pady=4)
amortizacaofinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
amortizacaofinal.grid(column=5, row=21, padx=13, pady=4)
saldo_investimentofinal = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E68865')
saldo_investimentofinal.grid(column=5, row=22, padx=13, pady=10)

############################################## Saldos Finais ############################################

saldo_inicial_periodo = Label(main, text="Saldo Inicial Periodo", fg="black", bg="#FF3333", width=22, anchor=W,
                              font=("Arial", 8))
saldo_inicial_periodo.grid(column=0, row=25, padx=13, pady=10)

saldo_inicial_periodo1 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_inicial_periodo1.grid(column=1, row=25, padx=13, pady=10)
saldo_inicial_periodo2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_inicial_periodo2.grid(column=2, row=25, padx=13, pady=10)
saldo_inicial_periodo3 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_inicial_periodo3.grid(column=3, row=25, padx=13, pady=10)
saldo_inicial_periodo4 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_inicial_periodo4.grid(column=4, row=25, padx=13, pady=10)

saldo_final_periodo = Label(main, text="Saldo Final Periodo", fg="black", bg="#FF3333", width=22, anchor=W,
                            font=("Arial", 8))
saldo_final_periodo.grid(column=0, row=26, padx=13, pady=10)

saldo_final_periodo1 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_final_periodo1.grid(column=1, row=26, padx=13, pady=10)
saldo_final_periodo2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_final_periodo2.grid(column=2, row=26, padx=13, pady=10)
saldo_final_periodo3 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_final_periodo3.grid(column=3, row=26, padx=13, pady=10)
saldo_final_periodo4 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
saldo_final_periodo4.grid(column=4, row=26, padx=13, pady=10)

resultado_final_periodo = Label(main, text="Resultado Final Periodo", fg="black", bg="#FF3333", width=22, anchor=W,
                                font=("Arial", 8))
resultado_final_periodo.grid(column=0, row=27, padx=13, pady=4)

resultado_final_periodo1 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_periodo1.grid(column=1, row=27, padx=13, pady=4)
resultado_final_periodo2 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_periodo2.grid(column=2, row=27, padx=13, pady=4)
resultado_final_periodo3 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_periodo3.grid(column=3, row=27, padx=13, pady=4)
resultado_final_periodo4 = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_periodo4.grid(column=4, row=27, padx=13, pady=4)

resultado_final_TOTAL_INICIAL = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_TOTAL_INICIAL.grid(column=5, row=25, pady=4)
resultado_final_TOTAL_PERIODO = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_TOTAL_PERIODO.grid(column=5, row=26, pady=4)
resultado_final_TOTAL = Label(main, text=f'0.0', justify=CENTER, font=("Arial", 8), width=15, bg = '#E63427')
resultado_final_TOTAL.grid(column=5, row=27, padx=13, pady=4)

lista_nome = [saldo_anterior1, vendas1, salarios1, fornecedores1, impostos1, vendas2,
              salarios2, fornecedores2, impostos2, vendas3, salarios3, fornecedores3, impostos3,
              vendas4, salarios4, fornecedores4, impostos4, vendas_ativos1, aquisicao_ativos1,
              recebimentos_dividendos1, vendas_ativos2, aquisicao_ativos2,
              recebimentos_dividendos2, vendas_ativos3, aquisicao_ativos3,
              recebimentos_dividendos3, vendas_ativos4, aquisicao_ativos4,
              recebimentos_dividendos4, aquisicao_emprestimo1, pagamentos_dividendos1,
              amortizacao1, aquisicao_emprestimo2, pagamentos_dividendos2,
              amortizacao2, aquisicao_emprestimo3, pagamentos_dividendos3,
              amortizacao3, aquisicao_emprestimo4, pagamentos_dividendos4,
              amortizacao4]
listaL = [saldo_anterior2, saldo_anterior3, saldo_anterior4, saldo_caixa1, saldo_caixa2,
         saldo_caixa3, saldo_caixa4, vendas_caixafinal, salarios_caixafinal, fornecedores_caixafinal,
         impostos_caixafinal, saldo_caixafinal, total_anterior_final, vendas_ativofinal,
         aquisicao_ativosfinal, recebimento_dividendofinal, saldo_investimentofinal2, saldo_financiamento1,
         saldo_financiamento2, saldo_financiamento3, saldo_financiamento4, aquisicao_emprestimofinal,
         pagamentos_dividendosfinal, amortizacaofinal, saldo_investimentofinal, saldo_inicial_periodo1,
         saldo_inicial_periodo2, saldo_inicial_periodo3, saldo_inicial_periodo4, saldo_final_periodo1,
         saldo_final_periodo2, saldo_final_periodo3, saldo_final_periodo4, resultado_final_periodo1,
         resultado_final_periodo2, resultado_final_periodo3, resultado_final_periodo4, resultado_final_TOTAL_INICIAL,
         resultado_final_TOTAL_PERIODO, resultado_final_TOTAL, saldo_investimentos1, saldo_investimentos2,
          saldo_investimentos3, saldo_investimentos4]

############################################ Botões finais

PNC1 = Entry(main)
blank = Entry(main)

Button(main, text='Resultado', command=soma_fluxo_caixa, bg='#e6e6e6', font=("Arial", 8), width=15).grid(row=28,
                                                                                                         column=2,
                                                                                                         pady=5,
                                                                                                         padx=10,
                                                                                                         sticky=W)
btnRead = Button(main, width=15, text="Limpar", command=limpar_dados, bg='#e6e6e6', font=("Arial", 8)).grid(row=28, column=3, pady=5, padx=10,
                                                                                      sticky=W)

btnFunction = Button(main, width=15, text="Graficos", command = graficos, bg='#e6e6e6', font=("Arial", 8)).grid(row=28, column=4, pady=5, padx=10,
                                                                                      sticky=W)
mainloop()
"""
if str(saldo_anterior1.get()).isalpha() or str(vendas1.get()).isalpha() or \
            str(salarios1.get()).isalpha() or str(fornecedores1.get()).isalpha() or \
            str(impostos1.get()).isalpha() or str(vendas2.get()).isalpha() or \
            str(salarios2.get()).isalpha() or str(fornecedores2.get()).isalpha() or \
            str(impostos2.get()).isalpha() or str(vendas3.get()).isalpha() or \
            str(salarios3.get()).isalpha() or str(fornecedores3.get()).isalpha() or \
            str(impostos3.get()).isalpha() or str(vendas4.get()).isalpha() or \
            str(salarios4.get()).isalpha() or str(fornecedores4.get()).isalpha() or \
            str(impostos4.get()).isalpha():
            resultado_final_TOTAL_PERIODO["text"] = "Valores Inválidos"
            resultado_final_TOTAL_PERIODO.configure(bg="#e6e6e6", fg="red")
            blank.insert(0, 0)

    elif str(vendas_ativos1.get()).isalpha() or str(recebimentos_dividendos1.get()).isalpha() or \
            str(saldo_investimentos1.get()).isalpha() or str(vendas_ativos2.get()).isalpha() or str(recebimentos_dividendos2.get()).isalpha() or \
            str(saldo_investimentos2.get()).isalpha() or str(vendas_ativos3.get()).isalpha() or str(recebimentos_dividendos3.get()).isalpha() or \
            str(saldo_investimentos3.get()).isalpha() or str(vendas_ativos4.get()).isalpha() or str(recebimentos_dividendos4.get()).isalpha() or \
            str(saldo_investimentos4.get()).isalpha():

            resultado_final_TOTAL_PERIODO["text"] = "Valores Inválidos"
            resultado_final_TOTAL_PERIODO.configure(bg="#e6e6e6", fg="red")
            blank.insert(0, 0)
    elif str(aquisicao_emprestimo1.get()).isalpha() or str(pagamentos_dividendos1.get()).isalpha() or \
            str(amortizacao1.get()).isalpha() or str(aquisicao_emprestimo2.get()).isalpha() or str(pagamentos_dividendos2.get()).isalpha() or \
            str(amortizacao2.get()).isalpha() or str(aquisicao_emprestimo3.get()).isalpha() or str(pagamentos_dividendos3.get()).isalpha() or \
            str(amortizacao3.get()).isalpha() or str(aquisicao_emprestimo4.get()).isalpha() or str(pagamentos_dividendos4.get()).isalpha() or \
            str(amortizacao4.get()).isalpha():
            resultado_final_TOTAL_PERIODO["text"] = "Valores Inválidos"
            resultado_final_TOTAL_PERIODO.configure(bg="#e6e6e6", fg="red")
            blank.insert(0, 0)

    else:
"""