from scrapy import Spider
from scrapy.selector import Selector
from datacrawler.items import DatacrawlerItem
import scrapy
class CrawlerSpider(Spider):
    name = "datacrawler"
    allowed_domains = ["fptshop.com.vn"]
    start_urls = [
        "https://fptshop.com.vn/dien-thoai/apple-iphone",
    ]

    def parse(self, response):
        san_pham = response.xpath('/html/body/section/div/div[2]/div[2]/div[3]/div')
        base_url = "https://fptshop.com.vn/"
        for item in san_pham[1:]:
            ten_dien_thoai = item.xpath('a/@href').get()
            link = base_url + ten_dien_thoai
            yield scrapy.Request(link, callback=self.crawldata)

    def crawldata(self, response):
        data = response.xpath('/html/body/div[7]/div/div/div[2]')
        items = DatacrawlerItem()
        items['cong_nghe_man_hinh'] = data.xpath('ul/li[2]/span/a/text()').extract_first()
        items['mau_man_hinh'] = data.xpath('ul/li[2]/span/a/text()').extract_first()
        items['chuan_man_hinh'] = data.xpath('ul/li[4]/span/text()').extract_first()
        items['do_phan_giai_man_hinh'] = data.xpath('ul/li[5]/span/text()').extract_first()
        items['kich_thuoc_man_hinh'] = data.xpath('ul/li[6]/span/text()').extract_first()
        items['do_phan_giai_cam_truoc'] = data.xpath('ul/li[9]/span/text()').extract_first()
        items['thong_tin_cam_truoc'] = data.xpath('ul/li[10]/span/text()').extract_first()
        items['do_phan_giai_cam_sau'] = data.xpath('ul/li[12]/span/text()').extract_first()
        items['quay_phim'] = data.xpath('ul/li[13]/span/text()').extract_first()
        items['den_flash'] = data.xpath('ul/li[14]/span/text()').extract_first()
        items['chup_anh_nang_cao'] = data.xpath('ul/li[15]/span/text()').extract_first()
        items['toc_do_cpu'] = data.xpath('ul/li[17]/span/text()').extract_first()
        items['so_nhan'] = data.xpath('ul/li[18]/span/text()').extract_first()
        items['chipset'] = data.xpath('ul/li[19]/span/text()').extract_first()
        items['ram'] = data.xpath('ul/li[20]/span/text()').extract_first()
        items['gpu'] = data.xpath('ul/li[21]/span/text()').extract_first()
        items['cam_bien'] = data.xpath('ul/li[22]/span/text()').extract_first()
        items['danh_ba_luu_tru'] = data.xpath('ul/li[24]/span/text()').extract_first()
        items['rom'] = data.xpath('ul/li[25]/span/text()').extract_first()
        items['bo_nho_con_lai'] = data.xpath('ul/li[26]/span/text()').extract_first()
        items['the_nho_ngoai'] = data.xpath('ul/li[27]/span/text()').extract_first()
        items['ho_tro_the_nho_toi_da'] = data.xpath('ul/li[28]/span/text()').extract_first()
        items['kieu_dang'] = data.xpath('ul/li[30]/span/text()').extract_first()
        items['kich_thuoc'] = data.xpath('ul/li[32]/span/text()').extract_first()
        items['trong_luong'] = data.xpath('ul/li[33]/span/text()').extract_first()
        items['kha_nang_chong_nuoc'] = data.xpath('ul/li[34]/span/text()').extract_first()
        items['loai_pin'] = data.xpath('ul/li[36]/span/text()').extract_first()
        items['dung_luong_pin'] = data.xpath('ul/li[37]/span/text()').extract_first()
        items['pin_co_the_thao_roi'] = data.xpath('ul/li[38]/span/text()').extract_first()
        items['che_do_sac_nhanh'] = data.xpath('ul/li[39]/span/text()').extract_first()
        items['loai_sim'] = data.xpath('ul/li[41]/span/text()').extract_first()
        items['khe_cam_sim'] = data.xpath('ul/li[42]/span/text()').extract_first()
        items['wifi'] = data.xpath('ul/li[43]/span/text()').extract_first()
        items['gps'] = data.xpath('ul/li[44]/span/text()').extract_first()
        items['bluetooth'] = data.xpath('ul/li[45]/span/text()').extract_first()
        items['gprs_edge'] = data.xpath('ul/li[46]/span/text()').extract_first()
        items['nfc'] = data.xpath('ul/li[47]/span/text()').extract_first()
        items['cong_sac'] = data.xpath('ul/li[48]/span/text()').extract_first()
        items['jack_ioput'] = data.xpath('ul/li[49]/span/text()').extract_first()
        items['he_dieu_hanh'] = data.xpath('ul/li[65]/span/text()').extract_first()
        yield items