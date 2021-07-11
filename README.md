# BRASA
## É python, só que em português...

## Como Rodar:
```sh

$ git clone https://github.com/psicopython/Brasa.git
$
$ cd brasa
$
$ python -m venv .venv
$
$ source .venv/bin/activate
$
$ pip install -r requirements
$
$ python -m brasa --help
Usage: python -m brasa [OPTIONS]

Options:
  -o, --opção TEXT    Compile ou Execute
  -e, --entrada TEXT  Arquivo a ser compilado
  -s, --saida TEXT    Arquivo após a compilação
  --help              Show this message and exit.

```
## Agora vamos escrever um pouquinho de codigo

```sh
do flask importe Flask

app = Flask("app")

@app.route("/")
@app.route("/<nome>")
função index ( nome = Nada ):
    se nome não é Nada :
        retorne f"Olá { nome }"
    senão:
        retorne f"Olá Estranho"

se __nome__ == "__main__":
    app.run()
```

## Salve isso no arquivo exemplo.br e em seguida rode:
```sh
$ python -m brasa -o execute -e exemplo.br 
```
## Oque deverá resultar na seguinte saida
```sh
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```