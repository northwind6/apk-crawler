#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Scrapy settings for channels project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
BOT_NAME = 'channels'

# redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

SPIDER_MODULES = ['channels.spiders']
NEWSPIDER_MODULE = 'channels.spiders'

ITEM_PIPELINES = ['channels.pipelines.MongoDBPipeline',
                  'scrapy_redis.pipelines.RedisPipeline',]

# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    'channels.middlewares.allow_phantomjs.AllowPhantomjsMiddlewares': 543,

    # 'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
    # 'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
    # 'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
    # 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
    # 'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
    # 'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
    # 'scrapy.contrib.downloadermiddleware.ajaxcrawl.AjaxCrawlMiddleware': 560,
    # 'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
    # 'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
    # 'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
    # 'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
    # 'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
    # 'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
    # 'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
}

# 下载器
# DOWNLOAD_HANDLERS = {
#                 'http': 'channels.handler.mydownloader.MyDownloadHandler'
# }

# 扩展模块
EXTENSIONS = {
    'channels.extensions.spiderDetails.SpiderDetails': 1000,
}


# mongodb数据库
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
# MONGODB_DB = "channels"
# MONGODB_DB_USERNAME = ""
# MONGODB_DB_PWD = ""
MONGODB_DB = "shield"
MONGODB_DB_USERNAME = "nqshield"
MONGODB_DB_PWD = "nqshield"
MONGODB_COLLECTION = "app_info"
MONGODB_COLLECTION_ERROR = "error_app_info"
MONGODB_APP_TASK_COLLECTION = "app_task"
# 异常类型
ERR_TYPES = {'0': u'xpath路径有误',
             '1': u'下载失败',
             '2': u'解析失败',
             '3': u'入库失败',}

# 下载延迟
DOWNLOAD_DELAY = 0.5



# 设置为 None 或 0 ， 则使用动态分配的端口
# TELNETCONSOLE_PORT = '6023'
TELNETCONSOLE_PORT = None
TELNETCONSOLE_HOST = '127.0.0.1'

CONCURRENT_REQUESTS = 100

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'


# 项目的所在目录, 在页面获取不到apk文件大小的时候，下载完成后os.path.getsize(dir)的时候需要绝对路径
# windows 下
# PROJECT_DIR = os.sep.join(['D:', 'workspace', BOT_NAME])
# linux 下
PROJECT_DIR = os.getcwd()


# 下载完成的apk文件的存储目录
APK_DOWNLOAD_DIR = 'app-download'

# apk图标保存目录
APK_IMAGE_DIR = 'images'

# aapt等工具的目录
TOOLS_DIR = 'tools'


DUPEFILTER_DEBUG = True


# 渠道中文名称，key对应channel_detail目录内每个文件的 app_channel，value为该渠道的中文名
CHANNELS_NAME_DICT = {'yingyongbao': u'应用宝',
                 'baidu': u'百度手机助手',
                 'wandoujia': u'豌豆荚',
                 'huawei': u'华为应用市场',
                 '360zhushou': u'360手机助手',
                 '91zhushou': u'91手机助手',
                 'lenovomm': u'乐商店',
                 'hiapk': u'安卓市场',
                 'hao123': u'hao123手机资源',
                 'sogou': u'搜狗市场',
                 'meizu': u'魅族',
                 'xiaomi': u'小米',
                 'duote': u'多特',
                 'suning': u'苏宁',
                 '25pp': u'25pp安卓资源站',
                 'uc': u'UC应用商店',
                 'm163': u'网易应用中心',
                 'mumayi': u'木蚂蚁',
                 'anzhi': u'安智市场',
                 'fengbao': u'风暴数码',
                 'gfan': u'机锋',
                 'zol': u'zol手机应用',
                 'coolan': u'酷安网',
                 'sina': u'新浪',
                 'leidian': u'雷电',
                 'meizumi': u'魅族迷',
                 'youyi': u'优亿市场',
                 'yingyongku': u'应用酷',
                 'anruan': u'安软',
                 'mogu': u'蘑菇市场',
                 'yiyonghui': u'易用汇',
                 'liqu': u'历趣',
                 'oppo': u'oppo软件商店',
                 'pconline': u'太平洋',
                 'paopaoche': u'跑跑车游戏网',
                 'coolpai': u'酷派',
                 'Nduo': u'N多网',
                 'zhushou2345': u'zhushou2345',
                 'anzhuo': u'安卓网',
                 'waptw': u'天网',
                 'anqi': u'安奇网',
                 'mm10086': u'移动MM',
                 'shouyou4355': u'4355手游网',
                 'nduo': u'N多网',
                 'dangle': u'当乐',
                 'apk520': u'安卓乐园',
                 'pc6': u'PC6安卓网',
                 'newhua': u'华军软件园',
                 'dongpo': u'东坡下载',
                 'cnmo': u'手机中国',
                 'sogouzhushou': u'搜狗助手',
                 '33lc': u'绿茶安卓网',
                 'ptbus': u'口袋巴士',
                 'bufan': u'不凡游戏',
                 'downza': u'下载之家',
                 'mooyy': u'摸鱼网,', #### Error infos: DedeCms错误警告：连接数据库失败，可能数据库密码不对或数据库服务器出错！
                 'tongyi3987': u'统一下载站',
                 'baifenbai': u'百分网',
                 'sjvip': u'手机VIP',
                 'zhuodown': u'捉蛋网',
                 '77l': u'齐齐乐',
                 'muzi': u'木子安卓',
                 'apkqu': u'安趣市场',
                 'anqu': u'安趣网',
                 'anzu': u'安族网',
                 'mumayibbs': u'木蚂蚁论坛',
                 'anzhuo2265': u'2265安卓网',
                 'ErEb': u'E人E本',
                 'sj4399': u'4399手机游戏网',
                 'anzhuo25': u'爱吾安卓',
                 'imobile': u'手机之家',
                 '7xz': u'七匣子',
                 '7230': u'7230手游网',
                 'itmop': u'it猫扑网',
                 'newasp': u'新云网络',
                 'zhuannet': u'赚网',
                 'ruan8': u'软吧',
                 'androidcn': u'安卓中国',
                 '958shop': u'百信众联',
                 'sjwyx': u'手游之家',
                 'yesky': u'天极网',
                 'ard9': u'Android之家',
                 'anzow': u'安卓软件园',
                 'shoujileyuan': u'手机乐园',
                 'cncrk': u'起点下载',
                 '3533': u'手机世界',
                 'gezila': u'格子啦',
                 '5577': u'我机网',
                 'hackhome': u'网侠手机站',
                 'veryhuo': u'最火软件',
                 'sz1001': u'1001下载乐园',
                 'apkke': u'安卓客',
                 'android155': u'手游天下',
                 'myapks': u'安卓之家',
                 'wishdown': u'心愿下载',
                 'cr173': u'西西软件园',
                 'bkill': u'比克尔下载',
                 '52z': u'飞翔下载',
                 '9ht': u'九号手游',
                 'srui': u'新锐下载',
                 'jb51': u'脚本之家',
                 'anfensi': u'安粉丝',
                 'skycn': u'天空下载',
                 'borpor': u'宝瓶',
                 'paojiao': u'泡椒网',
                 'youxibaba': u'安贝市场',
                 'fpwap': u'飞鹏网',
                 'tompda': u'tompda',
                 '8471': u'安卓地带',
                 'muzhiwan': u'拇指玩',
                 'androidmi': u'安致迷',
                 'pn66': u'六六软件园',
                 'softboxes': u'安卓库',
                 'dbtapk': u'安卓大不同',
                 'gamedog': u'游戏狗',
                 'shouyou520': u'手游520',
                 '9game': u'九游',
                 'anzhuoyuan': u'安卓园',
                 'appchina': u'应用汇',








                 'ccb': u'中国建设银行',
                 'icbc': u'中国工商银行',
                 'cmb': u'招商银行',
                 'cmbc': u'民生银行',
                 'abc': u'中国农业银行',
                 'bankofchina': u'中国银行',


}


# 渠道的搜索url--处理函数function 的字典

CHANNELS_URL_FUNCTION_DICT = {
    'http://www.wandoujia.com/search': ('wandoujia', 'send_wandoujia_request'),
    'http://android.myapp.com/myapp/searchAjax.htm': ('yingyongbao', 'send_yingyongbao_request'),
    'http://shouji.baidu.com/s': ('baidu', 'send_baidu_request'),
    'http://appstore.huawei.com/search/': ('huawei', 'send_huawei_request'),
    'http://zhushou.360.cn/search/index/': ('360zhushou', 'send_360_request'),
    'http://apk.91.com/soft/android/search/1_5_0_0_': ('91zhushou', 'send_91_request'),
    'http://www.lenovomm.com/search/index.html': ('lenovomm', 'send_lenovomm_request'),
    'http://apk.hiapk.com/search': ('hiapk', 'send_hiapk_request'),
    'http://mob.hao123.com/search': ('hao123', 'send_hao123_request'),
    'http://app.sogou.com/search': ('sogou', 'send_sogou_request'),
    'http://app.meizu.com/apps/public/search/page': ('meizu', 'send_meizu_request'),
    'http://www.duote.com/searchPhone.php': ('duote', 'send_duote_request'),
    'http://app.suning.com/android/search': ('suning', 'send_suning_request'),
    'http://android.25pp.com/search': ('25pp', 'send_25pp_request'),
    'http://m.163.com/search/multiform': ('m163', 'send_163_request'),
    'http://www.anzhi.com/search.php': ('anzhi', 'send_anzhi_request'),
    'http://www.coolapk.com/search': ('coolan', 'send_coolan_request'),
    'http://down.tech.sina.com.cn/3gsoft/softlist.php': ('sina', 'send_sina_request'),
    'http://www.leidian.com/s': ('leidian', 'send_leidian_request'),
    'http://www.eoemarket.com/search_.html': ('youyi', 'send_youyi_request'),
    'http://www.mgyapp.com/search/all/page1/': ('yingyongku', 'send_yingyongku_request'),
    'http://www.anruan.com/search.php': ('anruan', 'send_anruan_request'),
    'http://www.mogustore.com/search.html': ('mogu', 'send_mogu_request'),
    'http://www.anzhuoapk.com/search': ('yiyonghui', 'send_yiyonghui_request'),
    'http://os-android.liqucn.com/search/download/': ('liqu', 'send_liqu_request'),
    'http://store.oppomobile.com/search/do.html': ('oppo', 'send_oppo_request'),
    'http://ks.pconline.com.cn/download.shtml': ('pconline', 'send_pconline_request'),
    'http://s.paopaoche.net/cse/search?': ('paopaoche', 'send_paopaoche_request'),
    'http://www.meizumi.com/search.html': ('meizumi', 'send_meizumi_request'),
    'http://s.mumayi.com/index.php': ('mumayi', 'send_mumayi_request'),
    'http://www.nduoa.com/': ('Nduo', 'send_nduo_request'),
    'http://zhushou.2345.com/index.php': ('zhushou2345', 'send_zhushou2345_request'),
    'http://s.anzhuo.com/searchapp.php': ('anzhuo', 'send_anzhuo_request'),
    'http://android.waptw.com/search/': ('waptw', 'send_waptw_request'),
    'http://mm.10086.cn/searchapp': ('mm10086', 'send_mm10086_request'),
    'http://www.4355.com/e/search/?searchget=1&tbname=download&tempid=1&show=title,smalltext&keyboard=': ('shouyou4355', 'send_soft4355_request'),
    'http://android.d.cn/search/app/': ('dangle', 'send_dangle_request'),
    'http://s.pc6.com/cse/search?click=1&s=12026392560237532321&nsid=3&q=': ('pc6', 'send_pc6_request'),
    'http://search.520apk.com/cse/search?s=17910776473296434043&nsid=1&q=': ('apk520', 'send_apk520_request'),
    'http://search.newhua.com/search_list.php?searchsid=6&app=search&controller=index&action=search&type=news&searchname=': ('newhua', 'send_newhua_request'),
    'http://m.onlinedown.net/index.php?os=1&search=': ('newhua', 'send_newhua_request'),
    'http://so.uzzf.com/cse/search?s=17102071521441408655&nsid=5&q=': ('dongpo', 'send_dongpo_request'),
    'http://app.cnmo.com/search/c=a&p=2&f=1&s=': ('cnmo', 'send_cnmo_request'),
    'http://xiazai.zol.com.cn/search': ('zol', 'send_zol_request'),
    'http://www.fengbao.com/index.php': ('fengbao', 'send_fengbao_request'),
    'http://app.mi.com/search': ('xiaomi', 'send_xiaomi_request'),
    'http://apk.gfan.com/search': ('gfan', 'send_gfan_request'),
    'http://zhushou.sogou.com/apps/search.html': ('sogouzhushou', 'send_sogouzhushou_request'),
    'http://www.33lc.com/android/': ('33lc', 'send_lcrjy_request'),
    'http://www.ptbus.com/': ('ptbus', 'send_ptbus_request'),
    'http://games.bufan.com/search/': ('bufan', 'send_bufan_request'),
    'http://www.downza.cn/android/': ('downza', 'send_downza_request'),
    'http://www.byfby.com/So.aspx': ('baifenbai', 'send_baifenbai_request'),
    'http://www.77l.com/so/': ('77l', 'send_qiqile_request'),
    'http://www.muzisoft.com/plus/search.php': ('muzi', 'send_muzi_request'),
    'http://www.apkqu.com/page/search.html': ('apkqu', 'send_apkqu_request'),
    'http://m.anqu.com/Search/search_game.php': ('anqu', 'send_anqu_request'),
    'http://m.apkzu.com/e/search/index.php': ('anzu', 'send_anzu_request'),
    'http://bbs.mumayi.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1': ('mumayibbs', 'send_mumayibbs_request'),
    'http://www.2265.com/sea_{apk_name}.html': ('anzhuo2265', 'send_anzhuo2265_request'),
    'http://www1.eben.cn/search/list/?search=': ('ErEb', 'send_ereb_request'),
    'http://a.4399.cn/search.html': ('sj4399', 'send_sj4399_request'),
    'http://www.25az.com/game': ('anzhuo25', 'send_anzhuo25_request'),
    'http://search.imobile.com.cn/index.php': ('imobile', 'send_imobile_request'),
    'http://www.7xz.com/search': ('7xz', 'send_7xz_request'),
    'http://www.7230.com': ('7230', 'send_7230_request'),
    'http://www.itmop.com/search.asp': ('itmop', 'send_itmop_request'),
    'http://www.newasp.net/': ('newasp', 'send_newasp_request'),
    'http://apk.zhuannet.com/search/': ('zhuannet', 'send_zhuannet_request'),
    'http://www.ruan8.com/search.php': ('ruan8', 'send_ruan8_request'),
    'http://down.androidcn.com/search/q/': ('androidcn', 'send_androidcn_request'),
    'http://d.958shop.com/soft/': ('958shop', 'send_958shop_request'),
    'http://so.sjwyx.com/so/': ('sjwyx', 'send_sjwyx_request'),
    'http://search.yesky.com/searchdownload.do': ('yesky', 'send_yesky_request'),
    'http://www.ard9.com/index.html': ('ard9', 'send_ard9_request'),
    'http://m.app.uc.cn/apk/index.php': ('uc', 'send_uc_request'),
    'http://www.anzow.com/Search.shtml': ('anzow', 'send_anzow_request'),
    'http://soft.shouji.com.cn/sort/search.jsp': ('shoujileyuan', 'send_shoujileyuan_request'),
    'http://www.cncrk.com/search.asp': ('cncrk', 'send_cncrk_request'),
    'http://a.3533.com/search/': ('3533', 'send_3533_request'),
    'http://www.gezila.com/search?t=android&q=': ('gezila', 'send_gezila_request'),
    'http://www.5577.com/': ('5577', 'send_5577_request'),
    'http://www.hackhome.com/': ('hackhome', 'send_hackhome_request'),
    'http://www.sz1001.net/query.asp': ('sz1001', 'send_sz1001_request'),
    'http://www.aliexpress.com/': ('aliexpress', 'send_aliexpress_request'),
    'http://www.apkke.com/plus/search.php?': ('apkke', 'send_apkke_request'),
    'http://android.155.cn/search.php': ('android155', 'send_android155_request'),
    'http://www.myapks.com/': ('myapks', 'send_myapks_request'),
    'http://www.wishdown.com/search.asp': ('wishdown', 'send_wishdown_request'),
    'http://www.cr173.com/': ('cr173', 'send_cr173_request'),
    'http://www.bkill.com/d/search.php?searchType=&mod=do&n=1&keyword=': ('bkill', 'send_bkill_request'),
    'http://www.52z.com/search': ('52z', 'send_52z_request'),
    'http://www.9ht.com/': ('9ht', 'send_9ht_request'),
    'http://www.srui.cn/': ('srui', 'send_srui_request'),
    'http://www.jb51.net/': ('jb51', 'send_jb51_request'),
    'http://www.anfensi.com/': ('anfensi', 'send_anfensi_request'),
    'http://sj.skycn.com/s.php': ('skycn', 'send_skycn_request'),
    'http://www.borpor.com/class.php': ('borpor', 'send_borpor_request'),
    'http://www.paojiao.cn/search__{apk_name}_1.html': ('paojiao', 'send_paojiao_request'),
    'http://app.youxibaba.cn/search': ('youxibaba', 'send_youxibaba_request'),
    'http://www.fpwap.com': ('fpwap', 'send_fpwap_request'),
    'http://www.tompda.com/soft/0-7-1-0-1': ('tompda', 'send_tompda_request'),
    'http://www.8471.com/plus/search.php?orderby=pubdate&kwtype=0&searchtype=title&keyword={apk_name}': ('8471', 'send_8471_request'),
    'http://www.muzhiwan.com/common/search': ('muzhiwan', 'send_muzhiwan_request'),
    'http://www.androidmi.com/index.php?m=search&c=index&a=init&typeid=55&siteid=1&q=': ('androidmi', 'send_androidmi_request'),
    'http://www.pn66.com/e/search/index.php': ('pn66', 'send_pn66_request'),
    'http://www.softboxes.cn/index.php?tpl=search&q=': ('softboxes', 'send_softboxes_request'),
    'http://www.dbtapk.com/plus/search/': ('dbtapk', 'send_dbtapk_request'),
    'http://www.gamedog.cn/': ('gamedog', 'send_gamedog_request'),
    'http://www.shouyou520.com/game.php': ('shouyou520', 'send_shouyou520_request'),
    'http://www.9game.cn/search': ('9game', 'send_9game_request'),
    'http://anzhuoyuan.com/search': ('anzhuoyuan', 'send_anzhuoyuan_request'),
    'http://www.appchina.com/sou/': ('appchina', 'send_appchina_request'),
    'http://www.apkcn.com/search/': ('anqi', 'send_anqi_request'),







    'http://www.ccb.com/cn/home/index.html': ('ccb', 'send_ccb_request'),
    'http://www.icbc.com.cn/ICBC/%E7%94%B5%E5%AD%90%E9%93%B6%E8%A1%8C/%E7%94%B5%E5%AD%90%E9%93%B6%E8%A1%8C%E4%BA%A7%E5%93%81/%E9%87%91%E8%9E%8Da%E5%AE%B6%E4%BA%A7%E5%93%81/%E4%B8%AA%E4%BA%BA%E6%89%8B%E6%9C%BA%E9%93%B6%E8%A1%8C/Android%E6%89%8B%E6%9C%BA%E9%93%B6%E8%A1%8C/android%E6%89%8B%E6%9C%BA%E9%93%B6%E8%A1%8C.htm': ('icbc', 'send_icbc_request'),
    'http://www.cmbchina.com/MBankWeb/Download/DownloadDetail.aspx?os=android': ('cmb', 'send_cmb_request'),
    'http://www.cmbc.com.cn/cs/Satellite?c=Page&cid=1356495600898&currentId=1375342239458&pagename=cmbc%2FPage%2FTP_PindaoLayout#': ('cmbc', 'send_cmbc_request'),
    'http://mobile.abchina.com/download/clientDownload/zh_CN/startUpSessionAction.ebf': ('abc', 'send_abc_request'),
    'http://www.bankofchina.com/ebanking/bocmbs/': ('bankofchina', 'send_bankofchina_request'),





    'http://search.veryhuo.com/cse/search?q={apk_name}&click=1&s=2976565871270662586&nsid=2': ('veryhuo', 'send_veryhuo_request'),

    'http://www.zhuodown.com/a/yingyongruanjian/': ('zhuodown', 'send_zhuodown_request'),

    # 'http://app.3987.com/app/android.html': ('tongyi3987', 'send_tongyi3987_request'), # todo, 搜索s参数未获取

    # 'http://www.coolmart.net.cn/#id=search&key=': ('coolpai', 'send_coolpai_request'), # todo 无web页面版本
    # #http://app.taobao.com # todo 淘宝不支持搜索
    # 'http://www.sjvip.com'# todo 不支持搜索
}
