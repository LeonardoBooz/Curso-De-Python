nome_arquivo = input('Digite o nome do arquivo que deseja abrir(nome meu arquivo)')
arquivo_usuario = open(nome_arquivo)

print(len(arquivo_usuario.readlines()))