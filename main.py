def verificaEmail(email): #1
    valid_extensions = [".com", ".com.br", ".cc", ".org"]
    prefix = True
    domain = False
    duplo = False

    if not list(email)[0].isalnum() or not list(email)[-1].isalnum():
        return False

    for letra in list(email):
        if prefix:
            if letra.isalnum():
                if duplo:
                    duplo = False
                continue
            elif letra in "._-":
                if duplo:
                    return False
                else:
                    duplo = True
                    continue
            elif letra == "@" and not duplo:
                prefix = False
                domain = True
                continue
            else:
                return False
        elif domain:
            if letra.isalnum():
                if duplo:
                    duplo = False
                continue
            elif letra in "._-":
                if duplo:
                    return False
                else:
                    duplo = True
                    continue
            else:
                return False

    if prefix or not email.endswith(tuple(valid_extensions)):
        return False
    else:
        return True


def validaData(data): #2

    try:

        if "/" in data: #dd/mm/aaaa
            data = data.split("/")
        elif "-" in data: #dd-mm-aaaa
            data = data.split("-")
        elif "." in data: #dd.mm.aaaa
            data = data.split(".")
        else:
            return False

        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])

        if ano < 0 or mes < 0 or mes > 12 or dia < 0:
            return False

        if mes in [1,3,5,7,8,10] and dia > 31:
            return False
        elif mes in [4,6,9,11] and dia > 30:
            return False
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    return False
                elif dia > 28:
                    return False
        else:
            return True
    except:
        return False


def stringtoInt(palavra): #3

    try:
        retorno = int("{:.0f}".format(float(palavra)))
        return retorno
    except:
        return False


if __name__ == '__main__':
    # --------------- 01 Verificar se o email está correto --------------------
    invalid_emails = ["abc-@mail.com","abc..def@mail.com",".abc@mail.com","abc#def@mail.com","abc.def@mail.c","abc.def@mail#archive.com","abc.def@mail","abc.def@mail..com"]
    valid_emails = ["abc-d@mail.com", "abc.def@mail.com", "abc@mail.com", "abc_def@mail.com", "abc.def@mail.cc", "abc.def@mail-archive.com", "abc.def@mail.org", "abc.def@mail.com"]

    print("\nEmails Inválidos")
    for email in invalid_emails:
        resposta = "É VÁLIDO" if verificaEmail(email) else "NÃO É VÁLIDO"
        print(email, ": ", resposta)

    print("\nEmails Válidos")
    for email in valid_emails:
        resposta = "É VÁLIDO" if verificaEmail(email) else "NÃO É VÁLIDO"
        print(email, ": ", resposta)

    print("\n")


    # --------------- 02 Verificar se a data está correta (dd/mm/aaaa) --------------------
    lista_data = ["05/01/1992", "03-05-2001", "15.11.2018", "01/10/1998", "03012003", "20 de Desembro de 2017", "04/24/1986", "-29/03/2007"]

    print("Verificar Datas")
    for data in lista_data:
        resposta = "É VÁLIDA" if validaData(data) else "NÃO É VÁLIDA"
        print(data, ": ", resposta)

    print("\n")


    # --------------- 03 converter String para inteiro --------------------
    lista_string = ["1", "47", "12.99", "14.a", "abc", "1a"]

    print("Converter String para Inteiro")
    for s in lista_string:
        s_int = stringtoInt(s)
        resposta = " NÃO PODE SER CONVERTIDA EM INTEIRO" if not s_int else f" EM INTEIRO é {s_int}"
        print(s, resposta, f"Tipo({type(s_int)})")