import random
import string

try:
    import pyperclip
    COPIA_AUTOMATICA = True
except ImportError:
    COPIA_AUTOMATICA = False


def gerar_senha(tamanho: int, incluir_maiusculas: bool, incluir_minusculas: bool,
                incluir_numeros: bool, incluir_simbolos: bool) -> str:

    grupos = []

    if incluir_maiusculas:
        grupos.append(string.ascii_uppercase)
    if incluir_minusculas:
        grupos.append(string.ascii_lowercase)
    if incluir_numeros:
        grupos.append(string.digits)
    if incluir_simbolos:
        grupos.append(string.punctuation)

    if not grupos:
        raise ValueError('Você deve selecionar ao menos um tipo de caractere para gerar a senha.')

    # Garante pelo menos um caractere de cada tipo selecionado
    senha = [random.choice(grupo) for grupo in grupos]

    # Junta todos os tipos possíveis e completa o restante
    todos_caracteres = ''.join(grupos)
    senha += random.choices(todos_caracteres, k=tamanho - len(senha))

    # Embaralha a senha final para evitar padrões previsíveis
    random.shuffle(senha)

    return ''.join(senha)


def solicitar_tamanho() -> int:
    """ Solicite ao usuário o tamanho da senha com validação"""
    while True:
        try:
            tamanho = int(input('Digite o tamanho da senha: '))
            if tamanho > 0:
                return tamanho
            print('O tamanho deve ser maior que zero.')
        except ValueError:
            print('Por favor, digite um número inteiro válido.')


def solicitar_opcao(mensagem: str) -> bool:
    """Pergunta ao usuário se deseja incluir determinado tipo de caractere."""
    resposta = input(mensagem).strip().lower()
    return resposta == 's'


def main():
    """Função principal: coleta informações do usuário e exibe a senha gerada."""

    print('=' * 45)
    print('Gerador de senhas aleatórias'.center(45, '='))
    print('=' * 45)

    tamanho = solicitar_tamanho()
    incluir_maiusculas = solicitar_opcao('Incluir letras maiusculas? (s/n): ')
    incluir_minusculas = solicitar_opcao('Incluir letras minúsculas? (s/n): ')
    incluir_numeros = solicitar_opcao('Incluir números? (s/n): ')
    incluir_simbolos = solicitar_opcao('Incluir símbolos? (s/n): ')

    try:
        senha = gerar_senha(
            tamanho,
            incluir_maiusculas,
            incluir_minusculas,
            incluir_numeros,
            incluir_simbolos
        )

        print('\nSua senha gerada é:')
        print(f'>>> {senha}')

        if COPIA_AUTOMATICA:
            pyperclip.copy(senha)
            print("A senha foi copiada para a área de transferência!")
        else:
            print('(Instale o módulo "pyperclip" para copiar automaticamente)')

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == '__main__':
    while True:
        main()
        continuar = input('\nGerar outra senha? (s/n); ').strip().lower()
        if continuar != 's':
            print("\nSaindo... Obrigado por usar o Gerador de senhas!")
            break
