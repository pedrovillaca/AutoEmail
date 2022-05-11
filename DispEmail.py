import pyautogui as pg
import pyperclip
import time

#Enviar email de nota
#outlook = x=333, y=881
#enviar email = x=34, y=216
#pasta notas = x=276, y=886

pg.PAUSE = 1.2

start = pg.confirm(text='Iniciar criação de email automatico?', title='PYTHONAUTO', buttons=['Iniciar', 'Cancelar'])

if (start=='Iniciar'):

    pg.click(x=333, y=881) #icone de email, se necessario usar press win, write outlook, press enter
    pg.hotkey("ctrl", "n") #atalho pra criar novo email
    pg.write("contas") #primeiro email
    pg.press("enter")
    pg.press("tab")
    pg.write("leandro") #copy
    pg.press("enter")
    pg.press("tab")

    fornec = pg.prompt(text= 'FORNECEDOR ASSUNTO:', title= 'Assunto') #assunto do email

    pyperclip.copy(fornec)
    pg.hotkey("ctrl", "v")

    pg.press("tab")

    #corpo do email
    pg.typewrite("Prezados,\n\n Segue dados da nota para pagamento!\n\n N: " + pg.prompt(text= 'NUM') + "\n F: " +
                 pg.prompt(text= 'FORNEC') + "\n D: " + pg.prompt(text= 'DOC') + "\n V: " + pg.prompt(text= 'VENC') + "\n")

    pg.click(x=276, y=886) #pasta onde estão as notas
    pg.press("down")
    time.sleep(3) #time para selecionar mais um arquivo, se necessario
    pg.hotkey("ctrl", "c")
    pg.click(x=27, y=444) #click para voltar ao corpo do email
    pg.hotkey("ctrl", "v")

    conf = pg.confirm(text='ENVIAR EMAIL?', title='CONFERENCIA', buttons=['Enviar', 'Cancelar'])

    if (conf=='Enviar'):
        pg.click(x=34, y=232)
    else:
        exit()
else:
    exit()