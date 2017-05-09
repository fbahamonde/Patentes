from selenium import webdriver
def consulta(resultado,webpage):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get(webpage)
    uno=resultado[0:1]
    dos=resultado[3:4]
    tres=resultado[6:7]
    sbox1 = driver.find_element_by_id("txtLetras")
    sbox1.send_keys(uno)
    sbox2 = driver.find_element_by_id("txtNumeros1")
    sbox2.send_keys(dos)
    sbox3 = driver.find_element_by_id("txtNumeros2")
    sbox3.send_keys(tres)
    element =driver.find_element_by_name("crear")
    element.click()
    pagina=driver.page_source
    driver.quit()
    if pagina.find("PRESENTA ENCARGO POLICIAL")!=-1:
        return "Auto robado"
    else:
        return "Auto sin encargo"