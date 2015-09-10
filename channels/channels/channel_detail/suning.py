#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.http import Request, Response, FormRequest
import os
from channels.conf import download, log_page, get_search_list
from channels.settings import APK_DOWNLOAD_DIR


"""
    dont_filter，表明这个请求不应该由调度器过滤掉。默认False--过滤，Ture--不过滤。
    报错现象：
    2015-06-26 13:38:23+0800 [channels] DEBUG: Filtered duplicate request: <GET http
    ://app.suning.com/android/search?keywords=%E6%8B%9B%E5%95%86%E9%93%B6%E8%A1%8C>
    - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)

"""
def send_suning_request(url, **kwargs):
    apk_name = kwargs['apk_name']
    return FormRequest(url,
                  formdata={'keywords': apk_name},
                  method='GET',
                  dont_filter=True,
                  meta=kwargs,
                  callback=get_suning_search_list)


def get_suning_search_list(response):
    log_page(response, 'get_suning_search_list.html')

    url_list_xpath = '//div[@class="app-result"]/ul/li/dl/dd/div/h3/a/@href'
    name_list_xpath = '//div[@class="app-result"]/ul/li/dl/dd/div/h3/a/text()'
    func = get_suning_detail
    host = ''
    result = get_search_list(response, url_list_xpath, name_list_xpath, func, host)
    if type(result) == list:
        for r in result:
            yield r
    else:
        yield result


def get_suning_detail(response):
    log_page(response, 'get_suning_detail.html')
    html = Selector(response)

    # app_channel = 'suning'
    apk_name = response.meta['apk_name']
    app_channel = response.meta['app_channel']
    app_name = html.xpath('//dl[@class="detail-top fl"]/dd/h3/text()').extract()[0]
    app_link = html.xpath('//a[@class="dl2pc-btn"]/@href').extract()[0]
    app_pn = response.url.split('pack=')[1]
    app_version = html.xpath('//a[@class="vers"]/span/text()').extract()[0]
    app_size = ''
    save_dir = os.path.sep.join([APK_DOWNLOAD_DIR, apk_name])


    params_dic = {} # 参数字典
    params_dic['app_channel'] = app_channel     # 渠道
    params_dic['app_detail_url'] = response.url # apk下载页面
    params_dic['app_link'] = app_link           # apk下载链接
    params_dic['save_dir'] = save_dir           # 下载apk保存的目录
    params_dic['app_name'] = app_name           # 要下载的apk的应用名称
    params_dic['app_pn'] = app_pn               # apk包名
    params_dic['app_version'] = app_version     # apk版本号
    params_dic['app_size'] = app_size           # apk文件的大小

    return download(**params_dic)