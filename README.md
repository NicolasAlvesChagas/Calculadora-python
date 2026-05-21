# Calculadora em Python com Shell Script

## Como executar o arquivo .sh

1. Clone o repositório:
```
git clone <URL_DO_REPOSITORIO>
```

2. Acesse a pasta do projeto:
```
cd <NOME_DA_PASTA>
```

3. Dê permissão de execução ao script:
```
chmod +x calculadora_sh.sh
```

4. Execute o script:
```
./calculadora_sh.sh
```

---

## Executando no Windows com WSL

1. Abra o WSL/Ubuntu pelo menu iniciar

2. Navegue até a pasta onde o repositório foi clonado:
```
cd /mnt/c/Users/<SEU_USUARIO>/Downloads/<NOME_DA_PASTA>
```

3. Dê permissão de execução ao script:
```
chmod +x calculadora_sh.sh
```

4. Execute o script:
```
./calculadora_sh.sh


---

## Explicação do código em Python

O programa funciona como uma calculadora simples via terminal.

### Entrada de dados
O usuário informa dois valores inteiros utilizando a função `input()`. Esses valores são convertidos para `int`.

### Escolha da operação
Um laço `while` é utilizado para garantir que o usuário escolha uma opção válida entre:

- 1: adição
- 2: subtração
- 3: multiplicação
- 4: divisão

Se o valor informado for inválido, o programa solicita novamente.

### Processamento
Após a escolha da operação, o programa realiza o cálculo correspondente utilizando estruturas condicionais (`if` / `elif`).

### Saída
O resultado da operação é exibido no terminal com `print()`.

---

## Estrutura do projeto

calculadora.py → contém a lógica da calculadora  
calculadora.sh → script que executa o programa Python