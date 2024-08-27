import undetected_chromedriver as uc
from a_pandas_ex_css_selector_from_html import pd_add_css_selector_from_html
pd_add_css_selector_from_html()
import os
import pandas as pd

if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get(r"Site que queira adquirir o CSSselector")
    
    # Gerar o DataFrame ignorando as tags especificadas
    df = pd.Q_selector_from_html(driver.page_source, parser="html.parser", ignore_tags=("html","link","meta", "body","img","script", "button", "iframe","svg", "p", "path","ul","li")) #Aqui podemos tirar as coisas que nao sao necessarias no codigo 
    
    print(df)

    # Salvar o DataFrame no Excel usando openpyxl
    df.to_excel('Destino do arquivo', engine='openpyxl')
    os.startfile('Destino do arquivo')