
#############################################################################################################################
#   filename:dailyMeet.py                                                       
#   created: 2022-03-25                                                              
#   import your librarys below                                                    
#############################################################################################################################

import win32com.client as client

def dailyMeet():

    #connect with outlook
    outlook = client.Dispatch("outlook.application")

    #create a newcalendar 

    call_item = outlook.CreateItem(1)

    #subject
    call_item.subject = "Daily Meeting"
    #body
    local = input("Informe onde será realizado a reunião: ")
    call_item.body = f"Você está sendo convidado a participar de nossa Daily Meeting que ocorre a cada segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira no {local}"
    #location
    call_item.location = f"{local}"
    #date and time
    day = int(input("Escolha o dia da reunião: "))
    mouth = int(input("Escolha o mês da reunião: "))
    hr = int(input("Escolha a hora de inicio da reunião: "))
    mn = int(input("Escolha os minutos da reunião: "))
    dur = int(input("A duração (em minutos) da reunião: "))
    if hr < 12:
        time = "AM"
    else:
        time = "PM"
    call_item.start = f"{day}/{mouth}/2022 {hr}:{mn}:00 {time}"
    call_item.duration = dur
    #priority
    call_item.importance = 2
    #meeting status for validate
    call_item.MeetingStatus = 1

    #add peoples

    quant = int(input("Quantas pessoas deseja reunir na daily? "))
    for i in range(quant):
        name = input(f"Digite o e-mail nº{i+1}: ")
        call_item.Recipients.add(f"{name}").Type = 1

    #send ou view
    choice = int(input("""Escolha uma opção:
    [1] - Enviar Email Direto,
    [2] - Visualizar antes de enviar
    R: """))
    if choice == 1:
        call_item.send()
        print("Email enviado")
    else:
        call_item.display()
        print("Painel aberto no outlook")
    

     

    