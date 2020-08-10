#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 21:37
# @Author  : Yuki


"""
首都类：
地区、国家、首都名
"""


class Capital:
    def __init__(self, region, country, capital):
        self.region = region
        self.country = country
        self.capital = capital

    def introduceTheCapital(self):
        print(f"{self.country}位于{self.region}地区,首都是{self.capital}.\n")


beijing = Capital("亚洲", "中国", "北京")
beijing.introduceTheCapital()

rome = Capital("欧洲", "意大利", "罗马")
rome.introduceTheCapital()

"""
古诗：
诗名、作者、朝代、原文
"""


class Poem:
    def __init__(self, name, author, dynasty, verse):
        self.name = name
        self.author = author
        self.dynasty = dynasty
        self.verse = verse

    def recite(self):
        print(f"{self.name}\n {self.dynasty}.{self.author}\n {self.verse}")


jingyesi = Poem("\t静夜思", "李白", "\t唐", "床前明月光，疑是地上霜。\n 举头望明月，低头思故乡。\n")
jingyesi.recite()

"""
口红：
品牌、色号、名称
"""


class Lipstick:
    def __init__(self, brand, num, name):
        self.brand = brand
        self.num = num
        self.name = name

    def fashionable(self):
        print(f"Omg!!{self.brand}的{self.num}色号：{self.name}，真的绝美，买它！买它！买它！！！\n")


tf16 = Lipstick("Tom Ford", "黑管16", "SCARLET ROUGE")
tf16.fashionable()

"""
5A景区：
省、市、名称、特色
"""


class Touristattractions:
    def __init__(self, province, city, name, characteristic):
        self.province = province
        self.city = city
        self.name = name
        self.characteristic = characteristic

    def guide(self):
        print(f"{self.name}5A景区位于{self.province}省{self.city}，特色：{self.characteristic}。\n")


jiuzhaigou = Touristattractions("四川", "阿坝藏族羌族自治州", "九寨沟",
                                "是一条纵深50余千米的山沟谷地，森林覆盖率超过80%。因沟内有树正寨、荷叶寨、则查洼寨等九个藏族村寨坐落在这片高山湖泊群中而得名。")
jiuzhaigou.guide()

"""
川菜：
名称，食材，创始年代，特征
"""


class SichuanCuisine:
    def __init__(self, name, ingredients, decade, features):
        self.name = name
        self.ingredients = ingredients
        self.decade = decade
        self.features = features

    def gourmet(self):
        print(f"{self.name},创始于{self.decade}，主要食材由{self.ingredients}组成，{self.features}\n")


mapodoufu = SichuanCuisine("麻婆豆腐", "豆腐、肉糜、豆瓣、花椒面", "清朝同治元年", "麻婆豆腐的特色在于麻、辣、烫、香、酥、嫩、鲜、活八字，也称之为八字箴言。\n"
                                                             "麻：指豆腐在起锅时，要洒上适量的花椒末。花椒最好用汉源贡椒，麻味纯正，沁人心脾。\n"
                                                             "辣：选用龙潭寺大红袍油椒制作豆瓣，剁细炼熟，加以少量熟油、海椒烹脍豆腐，又辣又香。\n"
                                                             "烫：豆腐的特质保持了整道菜出锅后的温度，不容易冷却。每下一次筷子，吃到的都是刚出炉的味道。\n"
                                                             "香：起锅立即上桌，闻不到制豆腐的石膏味，可冷浸豆腐的水锈味，也没有各色佐料原有的难闻气味，只有勾起食欲的香味。\n"
                                                             "酥： 炼好的肉馅子，色泽金黄，红酥不板，一颗颗，一粒粒，入口就酥，沾牙就化。\n"
                                                             "嫩：豆腐下锅，煎氽得法，色白如玉，有楞有角，一捻即碎，故多用小勺舀食。\n"
                                                             "鲜： 麻婆豆腐的原料，俱皆新鲜，鲜嫩翠绿，红白相宜，色味俱鲜，无可挑剔。\n"
                                                             "活：指麻婆豆腐店的一项绝技：豆腐上桌，寸把长的蒜苗，在碗内根根直立，翠绿湛兰，油泽甚艳，仿佛刚从畦地采摘切碎，活灵活现，但夹之入口，俱皆熟透，毫无生涩味道。")
mapodoufu.gourmet()
