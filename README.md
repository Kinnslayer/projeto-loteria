<h1>Projeto Loteria</h1>
Projeto onde o usuário escolhe entre três modos de jogos distintos, e o programa irá entregar números aleatórios de acordo com a escolha do jogo.


<h2>O Usuário Tem Três Escolhas de Jogo:</h2>

- Lotofácil
- Quina
- Megasena

<h2>Diferença Entre os Jogos:</h2>

- Lotofácil: Entrega 15 números aleatórios entre 1 e 25
- Quina: Entrega 5 números aleatórios entre 1 e 80
- Megasena: Entrega 6 números aleatórios entre 1 e 60

<h2>Tecnologias Utilizadas:</h2>

- Python
- Flask
- Javascript
- HTML
- CSS

<h2>Requisitos Para Utilizar o Programa</h2>

- Python versão 3.X
- Flask 
- IDE de sua preferência

<h2>Como Utilizar o Programa</h2>

Após fazer o clone do código, faça a instalação do Flask no seu prompt de comando:

```

$ pip install -U Flask

```

Posteriormente faça a importação do Flask na sua IDE:

```

from flask import Flask, render_template

```
Obs: O render_template é o que vai fazer o programa ser renderizado na página HTML.



Dentro do arquivo, execute o site_loteria.py:

![image](https://user-images.githubusercontent.com/119972623/213568526-11eb8917-5a2b-4a87-ba3c-7c45f2b347a1.png)

Na parte inferior no terminal, estará indicando que o programa está rodando neste endereço:

```

* Running on http://127.0.0.1:5000

```

Após selecionar a página o programa será aberto e estará com esse layout:


![image](https://user-images.githubusercontent.com/119972623/213570070-738de84c-5789-478d-bf4f-c946088b4a1e.png)




Agora é se divertir gerando os números e torcendo para um deles ser premiado. Enjoy it!!
