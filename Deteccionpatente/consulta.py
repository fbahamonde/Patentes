from selenium import webdriver

webpage = "http://consultawebvehiculos.carabineros.cl" 
uno="HY"
dos="VF"
tres="51"
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get(webpage)
sbox1 = driver.find_element_by_id("txtLetras")
sbox1.send_keys(uno)
sbox2 = driver.find_element_by_id("txtNumeros1")
sbox2.send_keys(dos)
sbox3 = driver.find_element_by_id("txtNumeros2")
sbox3.send_keys(tres)
element =driver.find_element_by_name("crear")
element.click()
pagina=driver.page_source
if pagina.find("PRESENTA ENCARGO POLICIAL")!=-1:
    print "auto robado"
else:
    print "auto sin encargo"