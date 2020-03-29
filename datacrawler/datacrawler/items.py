# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cong_nghe_man_hinh = scrapy.Field()
    mau_man_hinh = scrapy.Field()
    chuan_man_hinh = scrapy.Field()
    do_phan_giai_man_hinh = scrapy.Field()
    kich_thuoc_man_hinh = scrapy.Field()
    do_phan_giai_cam_truoc = scrapy.Field()
    thong_tin_cam_truoc = scrapy.Field()
    do_phan_giai_cam_sau = scrapy.Field()
    quay_phim = scrapy.Field()
    den_flash = scrapy.Field()
    chup_anh_nang_cao = scrapy.Field()
    toc_do_cpu = scrapy.Field()
    so_nhan = scrapy.Field()
    chipset = scrapy.Field()
    ram = scrapy.Field()
    gpu = scrapy.Field()
    cam_bien = scrapy.Field()
    danh_ba_luu_tru = scrapy.Field()
    rom = scrapy.Field()
    bo_nho_con_lai = scrapy.Field()
    the_nho_ngoai = scrapy.Field()
    ho_tro_the_nho_toi_da = scrapy.Field()
    kieu_dang = scrapy.Field()
    kich_thuoc = scrapy.Field()
    trong_luong = scrapy.Field()
    kha_nang_chong_nuoc = scrapy.Field()
    loai_pin = scrapy.Field()
    dung_luong_pin = scrapy.Field()
    pin_co_the_thao_roi = scrapy.Field()
    che_do_sac_nhanh = scrapy.Field()
    loai_sim = scrapy.Field()
    khe_cam_sim = scrapy.Field()
    wifi = scrapy.Field()
    gps = scrapy.Field()
    bluetooth = scrapy.Field()
    gprs_edge = scrapy.Field()
    nfc = scrapy.Field()
    cong_sac = scrapy.Field()
    jack_ioput = scrapy.Field()
    he_dieu_hanh = scrapy.Field()
    pass
