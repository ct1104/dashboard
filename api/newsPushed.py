import json
import arrow
import asyncio
from dashboard.model.DB import DB
from dashboard.config import DBCONFIG
from dashboard.config import DATABASE
from dashboard.config import IDLOCAL
from dashboard.config import BRLOCAL
from dashboard.config import MELOCAL
from dashboard.handler.basehandler import BaseHandler


class IDNewsPushedHandler(BaseHandler):

    LOCAL = IDLOCAL

    async def getNewsToPush(self):
        # 推送新闻数
        # 总推送数
        # 推送阅读数
        ret = {}
        table = '{}_pushCtrNews'.format(self.LOCAL)

        sql = '''
            SELECT
                COUNT(pushNews) AS newsToPush,
                CAST(SUM(pushNews) AS UNSIGNED)
            AS
                totalPushCount,
                CAST(SUM(pushNewsRead) AS UNSIGNED)
            AS
                totalPushReadCount
            FROM
                {db}.{table}
            WHERE
                date = {date}
        '''.format(
                db=DATABASE,
                table=table,
                date=self.date
            )

        res = DB(**DBCONFIG).query(sql)
        for item in res:
            ret.update({'newsToPush': item.get('newsToPush', 0)})
            totalPushCount = item.get('totalPushCount', 0)
            totalPushReadCount = item.get('totalPushReadCount', 0)
            ret.update({'totalPushCount': totalPushCount})
            ret.update({'totalPushReadCount': totalPushReadCount})

            try:
                pushReadRatio = '{:.3%}'.format(
                        totalPushReadCount / totalPushCount)
            except Exception:
                pushReadRatio = 0.00

            ret.update({'pushReadRatio': pushReadRatio})

        return ret

    async def getPushNewsTotalNormalReadCount(self):
        # 非推送阅读数
        ret = {}
        table = '{}_pushNewsTotalNormalReadCount'.format(self.LOCAL)

        sql = '''
                SELECT
                    totalNormalReadCount
                FROM
                    {db}.{table}
                WHERE
                    date={date}
            '''.format(
                db=DATABASE,
                table=table,
                date=self.date
            )

        res = DB(**DBCONFIG).query(sql)
        for item in res:
            ret.update({'totalNormalReadCount': item['totalNormalReadCount']})
        return ret

    async def getData(self, start_date, end_date):
        data = []

        for date in arrow.Arrow.range(
                frame='day', start=start_date, end=end_date):

            date = str(date).replace('-', '')
            date = int(date[:8])
            self.date = date

            tasks = [
                self.getNewsToPush(),
                self.getPushNewsTotalNormalReadCount()
            ]

            cur_data = dict()
            for task in asyncio.as_completed(tasks):
                cur_data.update(await task)

            data += [cur_data]
        return data

    def post(self):

        errid = 0
        errmsg = 'SUCCESS'
        data = None

        start_date = self.get_argument('start_date', default=None, strip=True)
        end_date = self.get_argument('end_date', default=None, strip=True)
        if start_date is None or end_date is None:
            errid = -1
            errmsg = 'Need date parameter'

        try:
            start_date = arrow.Arrow.strptime(start_date, '%Y%m%d')
            end_date = arrow.Arrow.strptime(
                end_date, '%Y%m%d').replace(days=-1)
        except Exception as e:
            errid = -2
            errmsg = 'date parameter should be %Y%m%d format like 20170101'

        event_loop = asyncio.get_event_loop()
        try:
            data = event_loop.run_until_complete(
                    self.getData(start_date, end_date))
        except Exception as e:
            errid = -3
            errmsg = str(e)

        res = dict()
        res['errid'] = errid
        res['errmsg'] = errmsg
        res['data'] = data
        self.write(json.dumps(res))


class BRNewsPushedHandler(BaseHandler):

    LOCAL = BRLOCAL

    async def getNewsToPush(self):
        # 推送新闻数
        # 总推送数
        # 推送阅读数
        ret = {}
        table = '{}_pushCtrNews'.format(self.LOCAL)

        sql = '''
            SELECT
                COUNT(pushNews) AS newsToPush,
                CAST(SUM(pushNews) AS UNSIGNED)
            AS
                totalPushCount,
                CAST(SUM(pushNewsRead) AS UNSIGNED)
            AS
                totalPushReadCount
            FROM
                {db}.{table}
            WHERE
                date = {date}
        '''.format(
                db=DATABASE,
                table=table,
                date=self.date
            )

        res = DB(**DBCONFIG).query(sql)
        for item in res:
            ret.update({'newsToPush': item['newsToPush']})

            try:
                totalPushCount = int(item['totalPushCount'])
            except TypeError:
                totalPushCount = 0

            try:
                totalPushReadCount = int(item['totalPushReadCount'])
            except TypeError:
                totalPushReadCount = 0

            ret.update({'totalPushCount': totalPushCount})
            ret.update({'totalPushReadCount': totalPushReadCount})

            try:
                pushReadRatio = '{:.3%}'.format(
                        totalPushReadCount / totalPushCount)
            except Exception:
                pushReadRatio = 0.00

            ret.update({'pushReadRatio': pushReadRatio})

        return ret

    async def getPushNewsTotalNormalReadCount(self):
        # 非推送阅读数
        ret = {}
        table = '{}_pushNewsTotalNormalReadCount'.format(self.LOCAL)

        sql = '''
                SELECT
                    totalNormalReadCount
                FROM
                    {db}.{table}
                WHERE
                    date={date}
            '''.format(
                db=DATABASE,
                table=table,
                date=self.date
            )

        res = DB(**DBCONFIG).query(sql)
        for item in res:
            ret.update({'totalNormalReadCount': item['totalNormalReadCount']})
        return ret

    async def getData(self, start_date, end_date):
        data = []

        for date in arrow.Arrow.range(
                frame='day', start=start_date, end=end_date):

            date = str(date).replace('-', '')
            date = int(date[:8])
            self.date = date

            tasks = [
                self.getNewsToPush(),
                self.getPushNewsTotalNormalReadCount()
            ]

            cur_data = dict()
            for task in asyncio.as_completed(tasks):
                cur_data.update(await task)

            data += [cur_data]
        return data

    def post(self):

        errid = 0
        errmsg = 'SUCCESS'
        data = None

        start_date = self.get_argument('start_date', default=None, strip=True)
        end_date = self.get_argument('end_date', default=None, strip=True)
        if start_date is None or end_date is None:
            errid = -1
            errmsg = 'Need date parameter'

        try:
            start_date = arrow.Arrow.strptime(start_date, '%Y%m%d')
            end_date = arrow.Arrow.strptime(
                end_date, '%Y%m%d').replace(days=-1)
        except Exception as e:
            errid = -2
            errmsg = 'date parameter should be %Y%m%d format like 20170101'

        event_loop = asyncio.get_event_loop()
        try:
            data = event_loop.run_until_complete(
                    self.getData(start_date, end_date))
        except Exception as e:
            errid = -3
            errmsg = str(e)

        res = dict()
        res['errid'] = errid
        res['errmsg'] = errmsg
        res['data'] = data
        self.write(json.dumps(res))


class MENewsPushedHandler(BaseHandler):

    LOCAL = MELOCAL

    async def getNewsToPush(self):
        # 推送新闻数
        # 总推送数
        # 推送阅读数
        ret = {}
        table = '{}_pushCtrNews'.format(self.LOCAL)

        sql = '''
            SELECT
                COUNT(pushNews) AS newsToPush,
                CAST(SUM(pushNews) AS UNSIGNED)
            AS
                totalPushCount,
                CAST(SUM(pushNewsRead) AS UNSIGNED)
            AS
                totalPushReadCount
            FROM
                {db}.{table}
            WHERE
                date = {date}
        '''.format(
                db=DATABASE,
                table=table,
                date=self.date
            )

        res = DB(**DBCONFIG).query(sql)
        for item in res:
            ret.update({'newsToPush': item['newsToPush']})

            try:
                totalPushCount = int(item['totalPushCount'])
            except TypeError:
                totalPushCount = 0

            try:
                totalPushReadCount = int(item['totalPushReadCount'])
            except TypeError:
                totalPushReadCount = 0

            ret.update({'totalPushCount': totalPushCount})
            ret.update({'totalPushReadCount': totalPushReadCount})

            try:
                pushReadRatio = '{:.3%}'.format(
                        totalPushReadCount / totalPushCount)
            except Exception:
                pushReadRatio = 0.00

            ret.update({'pushReadRatio': pushReadRatio})

        return ret

    async def getPushNewsTotalNormalReadCount(self):
        # 非推送阅读数
        ret = {}
        table = '{}_pushNewsTotalNormalReadCount'.format(self.LOCAL)

        sql = '''
                SELECT
                    totalNormalReadCount
                FROM
                    {db}.{table}
                WHERE
                    date={date}
            '''.format(
                db=DATABASE,
                table=table,
                date=self.date
            )

        res = DB(**DBCONFIG).query(sql)
        for item in res:
            ret.update({'totalNormalReadCount': item['totalNormalReadCount']})
        return ret

    async def getData(self, start_date, end_date):
        data = []

        for date in arrow.Arrow.range(
                frame='day', start=start_date, end=end_date):

            date = str(date).replace('-', '')
            date = int(date[:8])
            self.date = date

            tasks = [
                self.getNewsToPush(),
                self.getPushNewsTotalNormalReadCount()
            ]

            cur_data = dict()
            for task in asyncio.as_completed(tasks):
                cur_data.update(await task)

            data += [cur_data]
        return data

    def post(self):

        errid = 0
        errmsg = 'SUCCESS'
        data = None

        start_date = self.get_argument('start_date', default=None, strip=True)
        end_date = self.get_argument('end_date', default=None, strip=True)
        if start_date is None or end_date is None:
            errid = -1
            errmsg = 'Need date parameter'

        try:
            start_date = arrow.Arrow.strptime(start_date, '%Y%m%d')
            end_date = arrow.Arrow.strptime(
                end_date, '%Y%m%d').replace(days=-1)
        except Exception as e:
            errid = -2
            errmsg = 'date parameter should be %Y%m%d format like 20170101'

        event_loop = asyncio.get_event_loop()
        try:
            data = event_loop.run_until_complete(
                    self.getData(start_date, end_date))
        except Exception as e:
            errid = -3
            errmsg = str(e)

        res = dict()
        res['errid'] = errid
        res['errmsg'] = errmsg
        res['data'] = data
        self.write(json.dumps(res))
