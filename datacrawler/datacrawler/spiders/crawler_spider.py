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
        items['ten'] = response.xpath('/html/body/section/div/div[1]/div[1]/div/h1/text()').extract_first()
        items['url_img'] = response.xpath('/html/body/section/div/div[1]/div[2]/div[1]/div[1]//a[1]/@href').extract_first()
        items['cong_nghe_man_hinh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(2) > span *::text').extract_first()
        items['mau_man_hinh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(3) > span *::text').extract_first()
        items['chuan_man_hinh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(4) > span *::text').extract_first()
        items['do_phan_giai_man_hinh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(5) > span *::text').extract_first()
        items['kich_thuoc_man_hinh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(6) > span *::text').extract_first()
        items['mat_man_hinh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(7) > span *::text').extract_first()
        items['do_phan_giai_cam_truoc'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(9) > span *::text').extract_first()
        items['thong_tin_cam_truoc'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(10) > span *::text').extract_first()
        items['do_phan_giai_cam_sau'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(12) > span *::text').extract_first()
        items['quay_phim'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(13) > span *::text').extract_first()
        items['den_flash'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(14) > span *::text').extract_first()
        items['chup_anh_nang_cao'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(15) > span *::text').extract_first()
        items['toc_do_cpu'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(17) > span *::text').extract_first()
        items['so_nhan'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(18) > span *::text').extract_first()
        items['chipset'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(19) > span *::text').extract_first()
        items['ram'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(20) > span *::text').extract_first()
        items['gpu'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(21) > span *::text').extract_first()
        items['cam_bien'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(22) > span *::text').extract_first()
        items['danh_ba_luu_tru'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(24) > span *::text').extract_first()
        items['rom'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(25) > span *::text').extract_first()
        items['bo_nho_con_lai'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(26) > span *::text').extract_first()
        items['the_nho_ngoai'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(27) > span *::text').extract_first()
        items['ho_tro_the_nho_toi_da'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(28) > span *::text').extract_first()
        items['kieu_dang'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(30) > span *::text').extract_first()
        items['chat_lieu'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(31) > span *::text').extract_first()
        items['kich_thuoc'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(32) > span *::text').extract_first()
        items['trong_luong'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(33) > span *::text').extract_first()
        items['kha_nang_chong_nuoc'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(34) > span *::text').extract_first()
        items['loai_pin'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(36) > span *::text').extract_first()
        items['dung_luong_pin'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(37) > span *::text').extract_first()
        items['pin_co_the_thao_roi'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(38) > span *::text').extract_first()
        items['che_do_sac_nhanh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(39) > span *::text').extract_first()
        items['loai_sim'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(41) > span *::text').extract_first()
        items['khe_cam_sim'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(42) > span *::text').extract_first()
        items['wifi'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(43) > span *::text').extract_first()
        items['gps'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(44) > span *::text').extract_first()
        items['bluetooth'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(45) > span *::text').extract_first()
        items['gprs_edge'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(46) > span *::text').extract_first()
        items['nfc'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(47) > span *::text').extract_first()
        items['cong_sac'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(48) > span *::text').extract_first()
        items['jack_ioput'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(49) > span *::text').extract_first()
        items['xem_phim'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(51) > span *::text').extract_first()
        items['nghe_nhac'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(52) > span *::text').extract_first()
        items['ghi_am'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(53) > span *::text').extract_first()
        items['FM_radio'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(54) > span *::text').extract_first()
        items['den_pin'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(55) > span *::text').extract_first()
        items['chuc_nang_khac'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(56) > span *::text').extract_first()
        items['thoi_gian_bao_hanh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(58) > span *::text').extract_first()
        items['xuat_xu'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(60) > span *::text').extract_first()
        items['nam_san_xuat'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(61) > span *::text').extract_first()
        items['model_series'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(63) > span *::text').extract_first()
        items['he_dieu_hanh'] = response.css('#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(65) > span *::text').extract_first()
        if items['ten']:
            yield items
#PopTSKTLT > div > div > div.modal-body > ul > li:nth-child(28) > span