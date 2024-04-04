# gerenciador de contatos
# De forma resumida é um check-list.
def salvar_contato(contatos, nome, email, telefone):
  """Adiciona um novo contato à lista."""
  contato = {"nome": nome, "email": email, "telefone": telefone, "favorito": False}
  contatos.append(contato)
  print(f"Contato {nome} adicionado com sucesso!")
  return

def ver_contatos(contatos):
     print("\nLista de contatos:")
     for indice, contato in enumerate(contatos, start=1):
         status = "✓ favorito" if contato["favorito"] else " "
         print(f"{indice}. [{status}] {contato["nome"]} - {contato["email"]} - {contato["telefone"]}")
     return

def atualizar_contatos(contatos, indice_contato, novo_nome, novo_email, novo_telefone):
    indice_contato_ajustado = int(indice_contato) -1
    if indice_contato_ajustado >= 0 or indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["email"] = novo_email
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        print(f"\nContato {indice_contato} foi atualizada para {novo_nome} {novo_email} {novo_telefone} !")
    else:
        print("Indice não existe!")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) -1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"\ncontato {indice_contato} marcado como favorito!")
    return

def deletar_contatos(contatos, indice_contato):
    del contatos[indice_contato -1]
    print(f"\ncontato {indice_contato} deletada")
    return

contatos = []

while True:
    print("\nMenu da agenda:")
    print("1. Salvar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Deletar contato")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        email = input("Digite o email do contato: ")
        telefone = input("Digite o telefone do contato: ")
        salvar_contato(contatos, nome, email, telefone)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Selecione o contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome: ")
        novo_email = input("Digite o novo email: ")
        novo_telefone = input("Digite o novo telefone:")
        atualizar_contatos(contatos, indice_contato, novo_nome, novo_email, novo_telefone)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Escolha o contato que deseja marcar como favorito: ")
        favoritar_contato(contatos, indice_contato)
    elif escolha == "5":
        indice_contato = input("Escolha o contato que deseja deletar:")
        indice_contato = int(indice_contato)
        deletar_contatos(contatos, indice_contato)
        ver_contatos(contatos)
    elif escolha == "6":
        break
    
print("Programa finalizado")
