#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.http import Request, Response, FormRequest
import os
from channels.conf import *
from channels.settings import APK_DOWNLOAD_DIR


def send_paojiao_request(url, **kwargs):
    apk_name = kwargs['apk_name']
    return FormRequest(url.format(apk_name=apk_name),
                    method='GET',
                    meta=kwargs,
                    callback=get_paojiao_search_list)


def get_paojiao_search_list(response):
    log_page(response, 'get_paojiao_search_list.html')

    url_list_xpath = '//ul[@class="recommend"]/li/div[@class="appinfo"]/div/a/@href'
    name_list_xpath = '//ul[@class="recommend"]/li/div[@class="appinfo"]/div/a/@title'
    func = get_paojiao_detail
    host = 'http://www.paojiao.cn'
    result = get_search_list(response, url_list_xpath, name_list_xpath, func, host)
    if type(result) == list:
        for r in result:
            yield r
    else:
        yield result

    # html = Selector(response)
    # detail_url = 'http://www.paojiao.com' + html.xpath('//div[@class="app_list border_three"]/ul/li[1]/div[2]/span/a/@href').extract()[0]
    # yield Request(detail_url, callback=get_paojiao_detail)


def get_paojiao_detail(response):
    log_page(response, 'get_paojiao_detail.html')
    html = Selector(response)

    # app_channel = 'paojiao'
    app_channel = response.meta['app_channel']
    apk_name = response.meta['apk_name']
    app_name = html.xpath('//div[@class="app-right"]/h2/span/text()').extract()
    if app_name:
        app_name = app_name[0]
    else:
        app_name = apk_name

    try:
        app_link_js = html.xpath('//a[@class="down"]/@onclick').extract()[0]

        params_list = app_link_js[app_link_js.find("(")+1: -2].split(',')

        app_link = 'http://www.paojiao.cn/download_{2}_{1}.html?url={0}'.format(params_list[0][1:-1],
                                                                                params_list[1][1:-1],
                                                                                params_list[2][1:-1],)


        # use_sys = html.xpath('//div[@class="info"]/ul[@class="right"]/li[3]/text()').extract()[0]
        #
        # if 'Android' not in use_sys:
        #     return None
    except:
        ## xpath有误。
        add_error_app_info(app_channel, app_name, '0')
        return None

    app_pn = ''
    app_version = ''
    app_size = ''
    save_dir = os.path.sep.join([APK_DOWNLOAD_DIR, apk_name])
    app_download_times = html.xpath('//div[@class="info"]/ul[@class="right"]/li[1]/text()').extract()
    if app_download_times:
        app_download_times = app_download_times[0].split('：')[1]
    else:
        app_download_times = ''


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
    # return None