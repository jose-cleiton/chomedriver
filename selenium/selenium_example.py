# importação do webdriver, que é o que possibilita a implementação para todos
# os principais navegadores da web
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# importação do webdriver, que é o que possibilita a implementação para todos


servico = Service(ChromeDriverManager().install())
# requisições para essa instância criada utilizando o método `get`
navegdor = webdriver.Chrome(service=servico)
