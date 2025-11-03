# 🔒 Gerador de Senhas Aleatórias (Python)

[![Status do Projeto](https://img.shields.io/badge/STATUS-Concluído-brightgreen)]()

## 📝 Descrição

Este projeto é uma ferramenta de linha de comando (CLI) em Python projetada para gerar **senhas fortes e verdadeiramente aleatórias**.

Ele oferece ao usuário controle total sobre os critérios da senha, permitindo definir o comprimento e selecionar quais tipos de caracteres serão incluídos: letras maiúsculas, minúsculas, números e símbolos.

### 💡 Conceitos em Destaque

Este projeto aborda e demonstra os seguintes conceitos de Python:

* Uso e manipulação dos módulos `random` e `string`.
* Estrutura de funções e tipagem (`type hinting`).
* Validação de entrada de dados (`try-except`).
* Uso opcional de bibliotecas externas (`pyperclip`).

## ✨ Funcionalidades

O gerador oferece as seguintes opções ao usuário:

* **Comprimento Personalizado:** Define o tamanho exato da senha.
* **Seleção de Caracteres:** Escolhe quais tipos de caracteres incluir (Maiúsculas, Minúsculas, Números, Símbolos).
* **Garantia de Tipos:** Garante que a senha gerada contenha pelo menos um caractere de cada tipo selecionado.
* **Cópia Automática:** Se o módulo `pyperclip` estiver instalado, a senha é automaticamente copiada para a área de transferência.
* **Loop de Execução:** Permite gerar múltiplas senhas sem precisar reiniciar o script.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3+
* **Módulos Padrão:** `random`, `string`
* **Módulo Opcional:** `pyperclip` (para cópia automática)

## ⚙️ Instalação e Execução

Siga os passos abaixo para baixar e rodar o gerador em sua máquina.

### Pré-requisitos

Você precisa ter o **Python 3** instalado em seu sistema operacional.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [[Link do seu Repositóri](https://github.com/btavolarogi/PROJETO_SENHA_ALEATORIA.git)o]
    ```
2.  **Acesse o diretório:**
    ```bash
    cd [PROJETO_SENHA_ALEATORIA]
    ```
3.  **Instale o módulo de cópia (Opcional):**
    Para ter a funcionalidade de cópia automática, instale o `pyperclip`:
    ```bash
    pip install pyperclip
    ```
4.  **Execute o script principal:**
    ```bash
    python3 [senha_aleatoria.py]
    ```

### ⌨️ Exemplo de Uso (CLI)

Ao executar o script, o usuário será guiado por prompts de entrada:

 ======Gerador de senhas aleatórias=========
Digite o tamanho da senha: 15 
Incluir letras maiusculas? (s/n): s 
Incluir letras minúsculas? (s/n): s 
Incluir números? (s/n): s 
Incluir símbolos? (s/n): n

Sua senha gerada é:

UvF9jK7tPzR4aB3 A senha foi copiada para a área de transferência!

## ⚠️ Tratamento de Erro

Se o usuário não selecionar **nenhum** tipo de caractere para inclusão, o programa irá exibir a mensagem de erro apropriada:

... Incluir símbolos? (s/n): n 
Erro: Você deve selecionar ao menos um tipo de caractere para gerar a senha.

## 👤 Autor

Desenvolvido por **[Giovanna Tavolaro]**

* **GitHub:** [@btavolarogi](https://github.com/btavolarogi)
* **[www.linkedin.com/in/giovanna-tavolaro-720517340]**

## 📜 Licença

Este projeto está sob a **Licença MIT** - veja o arquivo [LICENSE.md] para detalhes.
