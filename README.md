# MultiExe

**MultiExe** é uma ferramenta em Python que permite agrupar vários arquivos `.exe` em um único executável, facilitando a distribuição e execução de múltiplos aplicativos como um único pacote. 

Ela extrai os arquivos executáveis individuais em tempo de execução e os executa em um ambiente temporário, criando um arquivo único autossuficiente.

## Funcionalidades

- Combina múltiplos arquivos `.exe` em um único arquivo executável.
- Extração e execução dos arquivos em tempo de execução, sem precisar de instalação adicional.
- Limpeza de arquivos temporários, como `.crdownload`, após a execução.
- Criação de executável sem interface de console (modo "noconsole").
- Caso o arquivo final seja grande, usa **UPX** (Ultimate Packer for eXecutables) para compactação.

## Como Funciona

1. Coloque seus arquivos `.exe` na pasta `executaveis`.
2. Execute o script para gerar o arquivo `.exe` final.
3. O arquivo gerado vai extrair e executar os arquivos `.exe` em tempo real.

## Requisitos

- Python 3.x
- PyInstaller
- [UPX](https://github.com/upx/upx/releases/). (opcional, para compactar o arquivo final caso seja muito grande)

## Como Usar

### Instalar as dependências:

1. Clone o repositório:
   ```bash
   git clone https://github.com/ImNotKurtz/MultiExe
   cd multiexe

## Authors

- [@Kurtz](https://github.com/ImNotKurtz)

