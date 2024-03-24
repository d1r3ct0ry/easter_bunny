# -*- coding: cp1252 -*-
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("**************")
print("Sorteio de Amigo Oculto de Páscoa")
print("**************")

# Obter se existe orçamento:
budget = input("O seu amigo oculto tem um orçamento pré-definido (s/n)?  ").lower() 

# Obter o valor do orçamento:
if budget == 's':
    valor_budget = int(input("Qual o valor? ")) 

# Obter a quantidade de participantes
a = int(input("Quantidade de participantes: "))  

# Inicializar a lista de nomes e e-mails
participantes = []
for i in range(a):
    nome = input(f"Insira o nome do participante {i+1}: ")
    email = input(f"Insira o e-mail do participante {i+1}: ")
    participantes.append((nome, email))

# Embaralhar a lista de participantes
random.shuffle(participantes)

# Atribuir amigos ocultos
for i in range(a):
    amigo_oculto, email_amigo = participantes[(i + 1) % a]

    # Configurar o servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('theeasterbunny568@gmail.com', 'bbfc iika gele fupm')  # Substitua com suas credenciais

    # Criar a mensagem
    msg = MIMEMultipart()
    msg['From'] = 'seu_email@gmail.com'
    msg['To'] = email_amigo
    msg['Subject'] = 'Amigo Oculto de Páscoa'

    # Mensagem especial para a Páscoa
    if budget == 's':
        body = f"""\
        <html>
        <body>
            <p style="color: black;">Olá {amigo_oculto},</p>
            <p style="color: black;">Feliz Páscoa! Que este momento de renovação e esperança traga muita alegria e união para você e sua família. Que o verdadeiro significado da Páscoa esteja presente em nossos corações, celebrando a vitória do amor e da vida.</p>
            <p style="color: black;">Seu amigo oculto é: <b>{participantes[i][0]}</b></p>
            <p style="color: black;">O valor do amigo oculto é de: <b>R${valor_budget}</b></p>
            <p style="color: black;">Boas festas!</p>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSg4LughyIejzBertKuT6yjYq6PcFpf_uwLWvMfBmGnGZGHhBgq8gmYxnv5oY8joxsZR9g&usqp=CAU">
        </body>
        </html>
        """

        msg.attach(MIMEText(body, 'html'))
    else:
        body = f"""\
        <html>
        <body>
            <p style="color: black;">Olá {amigo_oculto},</p>
            <p style="color: black;">Feliz Páscoa! Que este momento de renovação e esperança traga muita alegria e união para você e sua família. Que o verdadeiro significado da Páscoa esteja presente em nossos corações, celebrando a vitória do amor e da vida.</p>
            <p style="color: black;">Seu amigo oculto é: <b>{participantes[i][0]}</b></p>
            <p style="color: black;">Boas festas!</p>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSg4LughyIejzBertKuT6yjYq6PcFpf_uwLWvMfBmGnGZGHhBgq8gmYxnv5oY8joxsZR9g&usqp=CAU">
        </body>
        </html>
        """

        msg.attach(MIMEText(body, 'html'))
    # Enviar o e-mail
    server.sendmail('seu_email@gmail.com', email_amigo, msg.as_string())
    server.quit()

    print(f"E-mail enviado para {amigo_oculto} ({email_amigo})")

print("Sorteio concluído! Verifique sua caixa de entrada.")
