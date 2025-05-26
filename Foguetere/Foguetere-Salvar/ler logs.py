import json

def salvar_log(dados):
    with open('logs.json', 'a') as f:
        json.dump(dados, f)
        f.write('\\n')
