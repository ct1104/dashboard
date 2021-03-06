# coding:utf-8
import tornado.web
import config

# 印尼
from api.user import IDUserHandler
from api.news import IDNewsHandler
from api.newsWithoutRelative import IDNewsWithoutRelativeHandler
from api.newsCrawled import IDNewsCrawledHandler
from api.newsPushed import IDNewsPushedHandler
from api.newsPushedNewClient import IDNewsPushedNewClientHandler
from api.newsPushedNewUser import IDNewsPushedNewUserHandler
from api.specialClickPosition import IDSpecialClickPositionHandler
from api.newsReadDuration import IDNewsReadDurationHandler
from api.newsTypeCtr import IDNewsTypeCtrHandler
from api.ctr import IDCtrHandler
from api.freshUsersCtr import IDFreshUsersCtrHandler
from api.hotNewsCtr import IDHotNewsCtrHandler
from api.newsCategoryCtr import IDNewsCategoryCtrHandler
from api.keywordSearchCountDesc import IDKeywordSearchCountDescHandler
from api.baseData import IDBaseDataQueryHandler
from api.latestDate import IDLatestDateHandler
from api.crawlFrequency import IDCrawlFrequencyHandler
from api.newsTitleSearch import IDNewsTitleSearchHandler
from api.bannerCtr import IDBannerCTRHandler
from api.operateNews import IDQueryNewsHandler
from api.operateNews import IDRemoveNewsHandler

from newspusher.pushserver import PushSingleHandler
from newspusher.pushserver import PushListHandler
from newspusher.pushserver import PromoteToNewsHandler

# 巴西
from api.user import BRUserHandler
from api.news import BRNewsHandler
from api.newsWithoutRelative import BRNewsWithoutRelativeHandler
from api.newsCrawled import BRNewsCrawledHandler
from api.newsPushed import BRNewsPushedHandler
from api.newsPushedNewClient import BRNewsPushedNewClientHandler
from api.newsPushedNewUser import BRNewsPushedNewUserHandler
from api.specialClickPosition import BRSpecialClickPositionHandler
from api.newsReadDuration import BRNewsReadDurationHandler
from api.newsTypeCtr import BRNewsTypeCtrHandler
from api.ctr import BRCtrHandler
from api.freshUsersCtr import BRFreshUsersCtrHandler
from api.hotNewsCtr import BRHotNewsCtrHandler
from api.newsCategoryCtr import BRNewsCategoryCtrHandler
from api.keywordSearchCountDesc import BRKeywordSearchCountDescHandler
from api.baseData import BRBaseDataQueryHandler
from api.latestDate import BRLatestDateHandler
from api.crawlFrequency import BRCrawlFrequencyHandler
from api.bannerCtr import BRBannerCTRHandler
from api.operateNews import BRQueryNewsHandler
from api.operateNews import BRRemoveNewsHandler

# 中东
from api.user import MEUserHandler
from api.news import MENewsHandler
from api.newsWithoutRelative import MENewsWithoutRelativeHandler
from api.newsCrawled import MENewsCrawledHandler
from api.newsPushed import MENewsPushedHandler
from api.newsPushedNewClient import MENewsPushedNewClientHandler
from api.newsPushedNewUser import MENewsPushedNewUserHandler
from api.specialClickPosition import MESpecialClickPositionHandler
from api.newsReadDuration import MENewsReadDurationHandler
from api.newsTypeCtr import MENewsTypeCtrHandler
from api.ctr import MECtrHandler
from api.freshUsersCtr import MEFreshUsersCtrHandler
from api.hotNewsCtr import MEHotNewsCtrHandler
from api.newsCategoryCtr import MENewsCategoryCtrHandler
from api.keywordSearchCountDesc import MEKeywordSearchCountDescHandler
from api.baseData import MEBaseDataQueryHandler
from api.latestDate import MELatestDateHandler
from api.crawlFrequency import MECrawlFrequencyHandler
from api.bannerCtr import MEBannerCTRHandler
from api.operateNews import MEQueryNewsHandler
from api.operateNews import MERemoveNewsHandler


class Application(tornado.web.Application):
    def __init__(self, debug=False):
        handlers = [

            (r"/dashboard/api/id/user", IDUserHandler),
            (r"/dashboard/api/id/news", IDNewsHandler),
            (r"/dashboard/api/id/newsWithoutRelative",
                IDNewsWithoutRelativeHandler),
            (r"/dashboard/api/id/newsCrawled", IDNewsCrawledHandler),
            (r"/dashboard/api/id/newsPushed", IDNewsPushedHandler),
            (r"/dashboard/api/id/newsPushedNewClient",
                IDNewsPushedNewClientHandler),
            (r"/dashboard/api/id/newsPushedNewUser",
                IDNewsPushedNewUserHandler),
            (r"/dashboard/api/id/specialClickPosition",
                IDSpecialClickPositionHandler),
            (r"/dashboard/api/id/newsWithoutRelative",
                IDNewsWithoutRelativeHandler),
            (r"/dashboard/api/id/newsCrawled", IDNewsCrawledHandler),
            (r"/dashboard/api/id/newsPushed", IDNewsPushedHandler),
            (r"/dashboard/api/id/newsPushedNewClient",
                IDNewsPushedNewClientHandler),
            (r"/dashboard/api/id/newsPushedNewUser",
                IDNewsPushedNewUserHandler),
            (r"/dashboard/api/id/specialClickPosition",
                IDSpecialClickPositionHandler),
            (r"/dashboard/api/id/newsReadDuration", IDNewsReadDurationHandler),
            (r"/dashboard/api/id/newsTypeCtr", IDNewsTypeCtrHandler),
            (r"/dashboard/api/id/ctr", IDCtrHandler),
            (r"/dashboard/api/id/freshUsersCtr", IDFreshUsersCtrHandler),
            (r"/dashboard/api/id/hotNewsCtr", IDHotNewsCtrHandler),
            (r"/dashboard/api/id/newsCategoryCtr", IDNewsCategoryCtrHandler),
            (r"/dashboard/api/id/newsTitleSearch", IDNewsTitleSearchHandler),
            (r"/dashboard/api/id/newspusher/pushsingle", PushSingleHandler),
            (r"/dashboard/api/id/newspusher/pushlist", PushListHandler),
            (r"/dashboard/api/id/newspusher/promoteToNews",
                PromoteToNewsHandler),
            (r"/dashboard/api/id/baseDataQuery", IDBaseDataQueryHandler),
            (r"/dashboard/api/id/keywordSearchCountDesc",
                IDKeywordSearchCountDescHandler),
            (r"/dashboard/api/id/latestDate", IDLatestDateHandler),
            (r"/dashboard/api/id/crawlFrequency", IDCrawlFrequencyHandler),
            (r"/dashboard/api/id/bannerCtr", IDBannerCTRHandler),
            (r"/dashboard/api/id/queryNews", IDQueryNewsHandler),
            (r"/dashboard/api/id/removeNews", IDRemoveNewsHandler),


            (r"/dashboard/api/br/user", BRUserHandler),
            (r"/dashboard/api/br/news", BRNewsHandler),
            (r"/dashboard/api/br/newsWithoutRelative",
                BRNewsWithoutRelativeHandler),
            (r"/dashboard/api/br/newsCrawled", BRNewsCrawledHandler),
            (r"/dashboard/api/br/newsPushed", BRNewsPushedHandler),
            (r"/dashboard/api/br/newsPushedNewClient",
                BRNewsPushedNewClientHandler),
            (r"/dashboard/api/br/newsPushedNewUser",
                BRNewsPushedNewUserHandler),
            (r"/dashboard/api/br/specialClickPosition",
                BRSpecialClickPositionHandler),
            (r"/dashboard/api/br/newsReadDuration", BRNewsReadDurationHandler),
            (r"/dashboard/api/br/newsTypeCtr", BRNewsTypeCtrHandler),
            (r"/dashboard/api/br/ctr", BRCtrHandler),
            (r"/dashboard/api/br/freshUsersCtr", BRFreshUsersCtrHandler),
            (r"/dashboard/api/br/hotNewsCtr", BRHotNewsCtrHandler),
            (r"/dashboard/api/br/newsCategoryCtr", BRNewsCategoryCtrHandler),
            (r"/dashboard/api/br/user", BRUserHandler),
            (r"/dashboard/api/br/news", BRNewsHandler),
            (r"/dashboard/api/br/newsWithoutRelative",
                BRNewsWithoutRelativeHandler),
            (r"/dashboard/api/br/newsCrawled", BRNewsCrawledHandler),
            (r"/dashboard/api/br/newsPushed", BRNewsPushedHandler),
            (r"/dashboard/api/br/newsPushedNewClient",
                BRNewsPushedNewClientHandler),
            (r"/dashboard/api/br/newsPushedNewUser",
                BRNewsPushedNewUserHandler),
            (r"/dashboard/api/br/specialClickPosition",
                BRSpecialClickPositionHandler),
            (r"/dashboard/api/br/newsReadDuration", BRNewsReadDurationHandler),
            (r"/dashboard/api/br/newsTypeCtr", BRNewsTypeCtrHandler),
            (r"/dashboard/api/br/ctr", BRCtrHandler),
            (r"/dashboard/api/br/freshUsersCtr", BRFreshUsersCtrHandler),
            (r"/dashboard/api/br/hotNewsCtr", BRHotNewsCtrHandler),
            (r"/dashboard/api/br/newsCategoryCtr", BRNewsCategoryCtrHandler),
            (r"/dashboard/api/br/baseDataQuery", BRBaseDataQueryHandler),
            (r"/dashboard/api/br/keywordSearchCountDesc",
                BRKeywordSearchCountDescHandler),
            (r"/dashboard/api/br/latestDate", BRLatestDateHandler),
            (r"/dashboard/api/br/crawlFrequency", BRCrawlFrequencyHandler),
            (r"/dashboard/api/br/bannerCtr", BRBannerCTRHandler),
            (r"/dashboard/api/br/queryNews", BRQueryNewsHandler),
            (r"/dashboard/api/br/removeNews", BRRemoveNewsHandler),


            (r"/dashboard/api/me/user", MEUserHandler),
            (r"/dashboard/api/me/news", MENewsHandler),
            (r"/dashboard/api/me/newsWithoutRelative",
                MENewsWithoutRelativeHandler),
            (r"/dashboard/api/me/newsCrawled", MENewsCrawledHandler),
            (r"/dashboard/api/me/newsPushed", MENewsPushedHandler),
            (r"/dashboard/api/me/newsPushedNewClient",
                MENewsPushedNewClientHandler),
            (r"/dashboard/api/me/newsPushedNewUser",
                MENewsPushedNewUserHandler),
            (r"/dashboard/api/me/specialClickPosition",
                MESpecialClickPositionHandler),
            (r"/dashboard/api/me/newsReadDuration", MENewsReadDurationHandler),
            (r"/dashboard/api/me/newsTypeCtr", MENewsTypeCtrHandler),
            (r"/dashboard/api/me/ctr", MECtrHandler),
            (r"/dashboard/api/me/freshUsersCtr", MEFreshUsersCtrHandler),
            (r"/dashboard/api/me/hotNewsCtr", MEHotNewsCtrHandler),
            (r"/dashboard/api/me/newsCategoryCtr", MENewsCategoryCtrHandler),
            (r"/dashboard/api/me/user", MEUserHandler),
            (r"/dashboard/api/me/news", MENewsHandler),
            (r"/dashboard/api/me/newsWithoutRelative",
                MENewsWithoutRelativeHandler),
            (r"/dashboard/api/me/newsCrawled", MENewsCrawledHandler),
            (r"/dashboard/api/me/newsPushed", MENewsPushedHandler),
            (r"/dashboard/api/me/newsPushedNewClient",
                MENewsPushedNewClientHandler),
            (r"/dashboard/api/me/newsPushedNewUser",
                MENewsPushedNewUserHandler),
            (r"/dashboard/api/me/specialClickPosition",
                MESpecialClickPositionHandler),
            (r"/dashboard/api/me/newsReadDuration", MENewsReadDurationHandler),
            (r"/dashboard/api/me/newsTypeCtr", MENewsTypeCtrHandler),
            (r"/dashboard/api/me/ctr", MECtrHandler),
            (r"/dashboard/api/me/freshUsersCtr", MEFreshUsersCtrHandler),
            (r"/dashboard/api/me/hotNewsCtr", MEHotNewsCtrHandler),
            (r"/dashboard/api/me/newsCategoryCtr", MENewsCategoryCtrHandler),
            (r"/dashboard/api/me/baseDataQuery", MEBaseDataQueryHandler),
            (r"/dashboard/api/me/keywordSearchCountDesc",
                MEKeywordSearchCountDescHandler),
            (r"/dashboard/api/me/latestDate", MELatestDateHandler),
            (r"/dashboard/api/me/crawlFrequency", MECrawlFrequencyHandler),
            (r"/dashboard/api/me/bannerCtr", MEBannerCTRHandler),
            (r"/dashboard/api/me/queryNews", MEQueryNewsHandler),
            (r"/dashboard/api/me/removeNews", MERemoveNewsHandler),

            (r"/dashboard/api/me/crawlFrequency", MECrawlFrequencyHandler),
        ]
        settings = {
            "template_path": config.TEMPLATE_PATH,
            "static_path": config.STATIC_PATH,
            "debug": debug,
            "cookie_secret": config.COOKIE_SECRET,
            "login_url": "/auth/login/",
        }
        tornado.web.Application.__init__(self, handlers, **settings)
