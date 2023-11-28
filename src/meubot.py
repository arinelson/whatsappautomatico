from selenium import webdriver
import time

# Caminho para o WebDriver (ajuste conforme necessário)
driver_path = 'webdriver/chromedriver.exe'

# Lista de contatos (apenas 2 contatos neste caso)
contatos = ["Contato1", "Contato2"]

# Inicializa o navegador
driver = webdriver.Chrome(executable_path=driver_path)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Aguarda o usuário fazer o login manualmente
input("Faça o login manualmente no WhatsApp Web e pressione Enter após o login.")

# Exemplo de automação: envia uma mensagem para cada contato com um intervalo de 5 segundos
mensagem = "Sua mensagem aqui"
intervalo_entre_contatos = 5  # em segundos

for contato_nome in contatos:
    # Localiza o campo de pesquisa
    search_box = driver.find_element("xpath", "//div[@contenteditable='true']")
    search_box.send_keys(contato_nome)
    time.sleep(2)

    # Seleciona o contato
    contato = driver.find_element("xpath", "//span[contains(text(),'" + contato_nome + "')]")
    contato.click()
    time.sleep(2)

    # Digita e envia a mensagem
    input_box = driver.find_element("xpath", "//div[@contenteditable='true'][@data-tab='1']")
    input_box.send_keys(mensagem)
    input_box.send_keys("\n")

    # Aguarda o intervalo entre contatos
    time.sleep(intervalo_entre_contatos)

# Fecha o navegador após um tempo para observar a execução
time.sleep(5)
driver.quit()
