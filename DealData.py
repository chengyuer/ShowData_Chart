import random

from pyecharts import Bar, Page, Style, Pie, Bar3D, Timeline, Map
from pyecharts import Map, Page, Style

class GetData(object):
    def getxinzuo(self,month):
        if '0314' < month < '0419':
            return "白羊座"
        elif '0420' < month < '0520':
            return "金牛座"
        elif '0521' < month < '0621':
            return "双子座"
        elif '0622' < month < '0722':
            return "巨蟹座"
        elif '0723' < month < '0822':
            return "狮子座"
        elif '0823' < month < '0922':
            return "处女座"
        elif '0923' < month < '1023':
            return "天秤座"
        elif '1024' < month < '1122':
            return "天蝎座"
        elif '1123' < month < '1221':
            return "射手座"
        elif '0120' < month < '0218':
            return "水瓶座"
        elif '0219' < month < '0320':
            return "双鱼座"
        else:
            return "摩羯座"

    #得到所有的文本
    datalist = []
    def getdata(self):
        mydict = {}
        filenamelist = [str(x) for x in range(1998,2008)]
        for name in filenamelist:
            filepath=r"F:\pachong\SZday44数据清洗\age"+"\\"+ str(name)+'.txt'
            file=open(filepath,"rb")
            linelist=file.readlines()
            mydict[name] = {}
            for line in linelist:
                myline = line.decode("gbk", "ignore")
                mylinelist = myline.split(",")
                # 6123251890 0525 1315
                charstr = mylinelist[1][10:14]  # 取出月份和日期后面4位
                mykey = self.getxinzuo(charstr)  # 函数判断
                if mykey in mydict[name]:  # 存在，次数+1
                    mydict[name][mykey] += 1
                else:
                    mydict[name][mykey] = 1  # 不存在就创建
            file.close()
        return mydict

    def gettotladata(self):
        datalist = []
        for mystr in list(self.getdata().keys()):
            thedata = list(self.getdata()[mystr].values())
            datalist.append(thedata)
        return datalist

    def create_charts(self):
        page = Page()
        WIDTH = 1100
        HEIGHT = 550
        style = Style(
            width=WIDTH, height=HEIGHT
        )

        X_TIME =['处女座', '摩羯座', '水瓶座', '巨蟹座', '天秤座', '金牛座', '天蝎座', '射手座', '白羊座', '双子座', '双鱼座', '狮子座']

        Y_WEEK = [str(x) for x in range(1998,2007)]

        RANGE_COLOR = ['#313695', '#4575b4', '#74add1', '#abd9e9',
                       '#e0f3f8', '#ffffbf', '#fee090', '#fdae61',
                       '#f46d43', '#d73027', '#a50026']
        chart = Bar("10年内各星座住房爱好"+"\n"+"Power by 胡煜", **style.init_style)
        for mystr in list(self.getdata().keys()):
            chart.add(mystr, list(self.getdata()[mystr].keys()), list(self.getdata()[mystr].values()), is_stack=True)
        page.add(chart)
        chart = Bar("10年内各星座住房爱好"+"\n"+"Power by 胡煜", **style.init_style)
        for mystr in list(self.getdata().keys()):
            chart.add(mystr, list(self.getdata()[mystr].keys()), list(self.getdata()[mystr].values()), mark_point=["average"])
        page.add(chart)

        chart = Bar("10年内各星座住房爱好"+"\n"+"Power by 胡煜", **style.init_style)
        for mystr in list(self.getdata().keys()):
            chart.add(mystr, list(self.getdata()[mystr].keys()), list(self.getdata()[mystr].values()), is_convert=True)
        page.add(chart)
        chart = Pie("10年内各星座住房爱好", title_pos='center', **style.init_style)
        for mystr in list(self.getdata().keys()):
            chart.add(mystr, list(self.getdata()[mystr].keys()), list(self.getdata()[mystr].values()), is_random=True,
                      radius=[30, 75], rosetype='area',
                      is_legend_show=False, is_label_show=True)
        page.add(chart)

        data = self.gettotladata()
        chart = Timeline(is_auto_play=True, timeline_bottom=0,
                         width=WIDTH, height=HEIGHT,)
        for mystr in list(self.getdata().keys()):
            your = str(mystr)
            print(your)
            your = Bar(mystr + "各星座住宿记录数据", "数据真实可靠")
            your.add("", list(self.getdata()[mystr].keys()), list(self.getdata()[mystr].values()), is_legend_show=True)
            chart.add(your, str(mystr) + "年")
        page.add(chart)

        lastdict = {'华东': 8347764, '中南': 3473591, '西北': 1109607, '西南': 1105030, '华北': 2744619, '东北': 1819191}
        bar = Bar("全国人民住房信息统计")
        bar.add("区域分类", list(lastdict.keys()), list(lastdict.values()), is_stack=True)
        page.add(bar)
        # infodict = {'江苏': 2399942, '上海': 914870, '湖北': 975236, '山东': 1529117, '江西': 594503, '陕西': 572695, '四川': 665913,
        #             '浙江': 1338150, '北京': 494634, '广西': 193134, '海南': 48342, '辽宁': 750881, '福建': 573289, '湖南': 566187,
        #             '河南': 1119652, '内蒙古': 393545, '天津': 321102, '安徽': 981923, '黑龙江': 580329, '吉林': 457018, '河北': 792687,
        #             '广东': 562808, '重庆': 74491, '山西': 693971, '贵州': 189171, '云南': 142511, '新疆': 145680, '甘肃': 227961,
        #             '青海': 75836, '宁夏': 75110, '西藏': 17526, '澳门': 21805, '香港': 12984, '台湾': 2158}
        # map = Map("全国各地域分布住房信息", width=1200, height=600)
        # map.add("", list(infodict.keys()), list(infodict.values()), maptype='china', is_visualmap=True, visual_text_color='#000')
        # page.add(map)

        # chart = Bar3D("3D 柱状图-默认", **style.init_style)
        # chart.add("你妹", X_TIME, Y_WEEK, [[d[0], d[1], d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11]] for d in data],
        #           is_visualmap=True, visual_range=[0, 70],
        #           visual_range_color=RANGE_COLOR,
        #           grid3d_width=200, grid3d_depth=100)
        # page.add(chart)

        return page
if __name__ == '__main__':
    data = GetData()
    data.create_charts().render(r"F:\FlaskProgramm\templates\3.html")