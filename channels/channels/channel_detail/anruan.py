#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.http import Request, Response, FormRequest
import os
from channels.conf import download, log_page, get_search_list, add_error_app_info
from channels.settings import APK_DOWNLOAD_DIR


def send_anruan_request(url, **kwargs):
    apk_name = kwargs['apk_name']
    return FormRequest(url,
                    formdata={'keyword': apk_name.encode('gbk'), 't': 'all'},
                    method='GET',
                    meta=kwargs,
                    callback=get_anruan_search_list)


def get_anruan_search_list(response):
    log_page(response, 'get_anruan_search_list.html')

    url_list_xpath = '//div[@id="divlist"]/div[@class="li"]/ul/li/a/@href'
    name_list_xpath = '//div[@id="divlist"]/div[@class="li"]/ul/li/a/@title'
    func = get_anruan_detail
    host = ''
    result = get_search_list(response, url_list_xpath, name_list_xpath, func, host)
    if type(result) == list:
        for r in result:
            yield r
    else:
        yield result

    # html = Selector(response)
    # detail_url = html.xpath('//div[@id="divlist"]/div[2]/a/@href').extract()[0]
    # yield Request(detail_url,
    #               meta=response.meta,
    #               callback=get_anruan_detail)


def get_anruan_detail(response):
    log_page(response, 'get_anruan_detail.html')
    html = Selector(response)

    # app_channel = 'anruan'
    app_channel = response.meta['app_channel']
    apk_name = response.meta['apk_name']
    app_name = apk_name
    try:
        app_link = html.xpath('//li[@class="app_down"]/a/@href').extract()[0]
    except:
        ## xpath有误。
        add_error_app_info(app_channel, app_name, '0')
        return None

    app_pn = ''
    app_version = ''
    app_size = ''
    save_dir = os.path.sep.join([APK_DOWNLOAD_DIR, apk_name])
    app_download_times = html.xpath('//div[@class="app_info"]/div/ul/li[7]/text()').extract()[0]


    params_dic = {} # 参数字典
    params_dic['app_channel'] = app_channel     # 渠道
    params_dic['app_detail_url'] = response.url # apk下载页面
    params_dic['app_download_times'] = app_download_times  # apk下载次数
    params_dic['app_link'] = app_link           # apk下载链接
    params_dic['save_dir'] = save_dir           # 下载apk保存的目录
    params_dic['app_name'] = app_name           # 要下载的apk的应用名称
    params_dic['app_pn'] = app_pn               # apk包名
    params_dic['app_version'] = app_version     # apk版本号
    params_dic['app_size'] = app_size           # apk文件的大小

    return download(**params_dic)