# py-util-crawlers

Conjunto de crawlers para monitoramento de informações úteis no dia-a-dia. O resultado da captura é enviado para os e-mails configurados no arquivo .env.

## Dependencies

I recommend you use pipenv

```
pipenv install
pipenv shell
```

## Execução

### Câmbio
Executar captura da cotação de moedas:

```
python cambio_crawler.py
```

### Rodizio Sanepar
Executar captura da agenda de rodizio de abastecimento de água e monitoramento dos níveis dos reservatórios da Sanepar na Região Metropolitada de Curitiba.
```
python sanepar_crawler.py
```

