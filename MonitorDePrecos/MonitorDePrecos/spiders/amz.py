import scrapy
import time
import smtplib

class AmzSpider(scrapy.Spider):
    name = 'amz'
    start_urls = ['https://www.amazon.com.br/Processador-AMD-Ryzen-5600X-Threads/dp/B08166SLDF']
    #start_urls = ['https://www.amazon.com.br/Processador-AMD-Ryzen-5800X-Threads/dp/B0815XFSGK/ref=pd_lpo_147_t_0/132-5001667-9461903?_encoding=UTF8&pd_rd_i=B0815XFSGK&pd_rd_r=71cea5f9-6931-417d-a27b-43891e56bf27&pd_rd_w=mOnQ5&pd_rd_wg=XgE5G&pf_rd_p=6102dabe-0e19-4db6-8e11-875a53ad30be&pf_rd_r=7808G504V3A06ZQZCT4A&psc=1&refRID=7808G504V3A06ZQZCT4A']
    
    
    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)          
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('viniciusmatos08@gmail.com', '573475vini10@')

        subject = 'O preço baixou!'
        body = 'Verifique o link https://www.amazon.com.br/Processador-AMD-Ryzen-5800X-Threads/dp/B0815XFSGK/re \
        f=pd_lpo_147_t_0/132-5001667-9461903?_encoding=UTF8&pd_rd_i=B0815XFSGK&pd_rd_r=71cea5f9-6931-417d-a27b-4 \
        3891e56bf27&pd_rd_w=mOnQ5&pd_rd_wg=XgE5G&pf_rd_p=6102dabe-0e19-4db6-8e11-875a53ad30be&pf_rd_r=7808G504V3A0\
        6ZQZCT4A&psc=1&refRID=7808G504V3A06ZQZCT4A'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'viniciusmatos08@gmail.com',
            'viniciusmatos08@gmail.com',
            msg
        )

        print('Email enviado com sucesso!')
    
    
    def parse(self, response, **kwargs):
        while(True):
            price = response.xpath('.//span[@class="a-size-medium a-color-price"]/text()').get()
            price = price.replace("\n","")
            product_name = response.xpath('.//span[@class="a-size-large product-title-word-break"]/text()').get()
            product_name = product_name.replace("\n","")


            yield{
                'price': price,
                'product_name': product_name
            }

            #print("ESTE E O PRECO: " + price)
            #print("ESTE E O nome: " + product_name)
            #time.sleep(10)




