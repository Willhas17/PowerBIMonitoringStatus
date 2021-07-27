
# PowerBI Monitoring Status

## Sobre

Código para monitar o status de todos relatórios do workspace do Power BI
- Monitoramento dinâmico dos relatórios
- Fácil configuração

## Como Funciona

O programa verifica a cada 5 minutos se os relatórios do workspace tem próxima hora de atualização agendada. Se houver próxima hora de atualização agendada, o relatório está "ok", e o status ficará verde, se não ficará vermelho.


## Instalação

PowerBIMonitoringStatus precisa do [Python](https://www.python.org/) v3 para executar.

Instalando as dependências.

 - [Chrome Driver](https://chromedriver.chromium.org/downloads)
 - [Azure Theme](https://github.com/rdbende/Azure-ttk-theme)

- [Tkinter]
```sh
pip install tkinter
```
- [Selenium]
```sh
pip install selenium
```

## Dicas

#### Criando um EXE

Instalando as blibiotecas:

```sh
pip install pyinstaller
```

Gerando o arquivo exe:

- Arquivo unico no exe:
```sh
pyinstaller --noconfirm --onefile --noconsole "'directory'/PowerBI.py"
```

- Arquivos separados:
```sh
pyinstaller --noconfirm --noconsole "'directory'/PowerBI.py"
```
## Desenvolvimento

Quer contribuir? Ótimo!

## Licença

**Código livre xD**

