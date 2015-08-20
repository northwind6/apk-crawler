#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.http import Request, Response, FormRequest
import os
from channels.conf import *
from channels.settings import APK_DOWNLOAD_DIR

def send_dongpo_request(url, **kwargs):
    apk_name = kwargs['apk_name']
    url = url + apk_name + '&'
    return FormRequest(url,
                  method='GET',
                  meta=kwargs,
                  callback=get_dongpo_search_list)


def get_dongpo_search_list(response):
    log_page(response, 'get_dongpo_search_list.html')

    url_list_xpath = '//*[@id="results"]/div/h3/a/@href'
    name_list_xpath = '//*[@id="results"]/div/h3/a/text()'
    func = get_dongpo_detail
    host = ''
    result = get_search_list(response, url_list_xpath, name_list_xpath, func, host)
    if type(result) == list:
        for r in result:
            yield r
    else:
        yield result


def get_dongpo_detail(response):
    log_page(response, 'get_dongpo_detail.html')
    html = Selector(response)

    apk_name = response.meta['apk_name']

    # app_channel = 'dongpo'
    app_channel = response.meta['app_channel']
    app_name = html.xpath('//h1[@class="app-title"]/text()').extract()
    if app_name:
        app_name = app_name[0]
    else:
        app_name = ''

    print apk_name not in app_name,'88888888'*10

    # 判断apk_name 是否存在于app_name中，不存在就返回None
    if apk_name not in app_name:
        return None

    try:
        app_link = html.xpath('//ul[@id="db-w"]/li[1]/a/@href').extract()[0]
    except:
        ## xpath有误。
        add_error_app_info(app_channel, app_name, '0')
        return None

    app_pn = ''
    app_version = ''
    app_size = ''
    save_dir = os.path.sep.join([APK_DOWNLOAD_DIR, apk_name])


    params_dic = {} # 参数字典
    params_dic['app_channel'] = app_channel     # 渠道
    params_dic['app_link'] = app_link           # apk下载链接
    params_dic['save_dir'] = save_dir           # 下载apk保存的目录
    params_dic['app_name'] = app_name           # 要下载的apk的应用名称
    params_dic['app_pn'] = app_pn               # apk包名
    params_dic['app_version'] = app_version     # apk版本号
    params_dic['app_size'] = app_size           # apk文件的大小

    return download(**params_dic)