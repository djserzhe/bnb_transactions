# Вывод транзакций BNB
 
Для запуска нужно поместить в корневую директорию файл `.env` с переменными:

- BNB_TRANS_URL (URL вида https://go.getblock.io/<токен>/)
- BNB_TRANS_REQUEST_INTERVAL (интервал в секундах, через который получать транзакции)

# Зависимости

```
pip install python-dotenv 
pip install web3
```