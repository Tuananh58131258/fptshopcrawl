from scrapy import Spider
from scrapy.selector import Selector
from datacrawler.items import DatacrawlerItem
import scrapy
class CrawlerSpider(Spider):
    name = "datacrawler"
    allowed_domains = ["fptshop.com.vn"]
    start_urls = [
        "https://fptshop.com.vn/dien-thoai/samsung",
        "https://fptshop.com.vn/dien-thoai/oppo",
        "https://fptshop.com.vn/dien-thoai/apple-iphone",
        "https://fptshop.com.vn/dien-thoai/vsmart",
        "https://fptshop.com.vn/dien-thoai/xiaomi",
        "https://fptshop.com.vn/dien-thoai/realme",
        "https://fptshop.com.vn/dien-thoai/vivo",
        "https://fptshop.com.vn/dien-thoai/nokia",
        "https://fptshop.com.vn/dien-thoai/huawei",
        "https://fptshop.com.vn/dien-thoai/masstel",
        "https://fptshop.com.vn/dien-thoai/itel",
        "https://fptshop.com.vn/dien-thoai/energizer",
    ]

    def parse(self, response):
        page = response.css('body > section > div > div.fs-ctf-row.clearfix > div.fs-ctf-cr > div.f-cmtpaging > a::attr(data-page)').getall()
        if page:
            fp = int(page[0])
            lp = int(page[1]) + 1
            for i in range (fp,lp):
                customurl = response.url+'?sort=ban-chay-nhat&trang='+ str(i)
                yield scrapy.Request(customurl,callback=self.praseurl)        
        else:
            san_pham = response.css('body > section > div > div.fs-ctf-row.clearfix > div.fs-ctf-cr > div.fs-carow.clearfix.fs-row4phone.viewgrid > div >a::attr(href)').getall()
            base_url = "https://fptshop.com.vn/"
        # items = DatacrawlerItem()
            for item in san_pham:
            # items['ten'] = item
            # yield items
                link = base_url + item
                yield scrapy.Request(link, callback=self.crawldata)
            
    def praseurl(self, response):
        san_pham = response.css('body > section > div > div.fs-ctf-row.clearfix > div.fs-ctf-cr > div.fs-carow.clearfix.fs-row4phone.viewgrid > div >a::attr(href)').getall()
        base_url = "https://fptshop.com.vn/"
        # items = DatacrawlerItem()
        for item in san_pham:
            # items['ten'] = item
            # yield items
            link = base_url + item
            yield scrapy.Request(link, callback=self.crawldata)

    def crawldata(self, response):
        items = DatacrawlerItem()
        ten = response.xpath('/html/body/section/div/div[1]/div[1]/div/h1/text()').extract_first()
        items['ten'] = str(ten).strip(" ").strip('\n')
        urlimg = response.xpath('/html/body/section/div/div[1]/div[2]/div[1]/div[1]//a[1]/@href').extract_first()
        items['url_img'] = "https:"+str(urlimg)
        label = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li > label ::text').getall()
        temp_label = ""
        for item in label:
            item.strip(" ").strip('\n')
            temp_label = temp_label + item + "/"
        items['label'] = temp_label
        data = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li > span ::text').getall()
        temp_data = ""
        for item in data:
            item.strip(" ").strip('\n')
            temp_data = temp_data + item + "/"
        items['data'] = temp_data
        n = len(data)
        for i in range(0,n):
            if label[i].find("ROM") >-1:
                items['rom'] = data[i]
            if label[i].find("RAM") >-1:
                items['ram'] = data[i]
        gia_cu = response.css('body > section > div > div.fs-dtprodif.fs-dtbox > div.fs-dtbott > div.fs-dtckr > p.fs-dt-mtlis > a > strong > i::text').get()
        items['gia_cu'] = str(gia_cu).replace(".","").strip("₫")
        if response.css('body > section > div > div.fs-dtprodif.fs-dtbox > div.fs-dtbott > div.fs-dtinfo > div.fs-pr-box > p ::text').get():
            gia = response.css('body > section > div > div.fs-dtprodif.fs-dtbox > div.fs-dtbott > div.fs-dtinfo > div.fs-pr-box > p ::text').get()
            items['gia'] = str(gia).strip('\r\n').strip(" ").replace(".","").strip("₫")
        else:
            gia = response.css('body > section > div > div.fs-dtprodif.fs-dtbox > div.fs-dtbott > div.fs-dtinfo > div.fs-pr-box > ul > li:nth-child(1) > label > span > strong ::text').get()
            items['gia'] = str(gia).strip('\r\n').strip(" ").replace(".","").strip("₫")
            gia_online = response.css('body > section > div > div.fs-dtprodif.fs-dtbox > div.fs-dtbott > div.fs-dtinfo > div.fs-pr-box > ul > li:nth-child(2) > label > span > strong ::text').get()
            items['gia_online'] = str(gia_online).strip('\r\n').strip(" ").replace(".","").strip("₫")
        mau_sac = response.css('body > section > div > div.fs-dtprodif.fs-dtbox > div.fs-dtbott > div.fs-dtinfo > div.fs-dticolor.fs-dticolor-img > ul > li > span > i ::text').getall()
        temp_mausac = ""
        for item in mau_sac:
            item.strip(" ").strip('\n')
            temp_mausac = temp_mausac + item + "/"
        items['mau_sac'] = temp_mausac

        khuyen_mai = response.css('#km-detail > div > div ::text').getall()
        temp_km = ""
        for item in khuyen_mai:
            if item.find('\r\n') == -1:
                if item.find("Xem chi tiết") == -1:
                    temp_km = temp_km + item +'\n'
                else:
                    temp_km = temp_km + item
        items['khuyen_mai'] = temp_km
        if items['ten'] and items['ten'].find("Đồng hồ") == -1:
            yield items
#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(28) > span