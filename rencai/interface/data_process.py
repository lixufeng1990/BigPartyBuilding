pre_people = [
        [
            "王博",
            "大连理工大学科学技术研究院常务副院长",
            "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=b8e8a4717e310a55d029d6a6d62c28cc/e850352ac65c10381c9df040b5119313b17e8954.jpg"
        ],
        [
            "王立峰",
            "南京航空航天大学航空宇航学院航空航天交叉研究院副院长",
            "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268/sign=6d2972b21a950a7b753549c232d0625c/d6ca7bcb0a46f21f9f2877d7f1246b600c33ae11.jpg"
        ],
        [
            "徐峰",
            "西安交通大学生命科学与技术学院/副院长",
            "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268/sign=c2cb5442a586c9170803553ff13d70c6/b7fd5266d0160924fc1912a1d60735fae6cd344f.jpg"
        ],
        [
            "杨越",
            "北京大学",
            "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/crop%3D0%2C20%2C500%2C330%3Bc0%3Dbaike80%2C5%2C5%2C80%2C26/sign=7804015b53ee3d6d3689dd8b7e264110/c8ea15ce36d3d5399f391d3f3087e950342ab0c1.jpg"
        ],
        [
            "范金燕",
            "上海交通大学",
            "http://ms2014.ctbu.edu.cn/__local/F/25/45/4C208F71FE643A99D8EA6737587_5D20F403_96A07.png"
        ],
        [
            "关启安",
            "北京大学，无行政职务",
            "https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=5e982a60f3f2b211f0238d1cabe90e5d/fd039245d688d43fc934dde1751ed21b0ef43b07.jpg"
        ],
        [
            "刘若川",
            "北京大学北京国际数学研究中心",
            "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268/sign=305367e7dd39b6004dce08b1d1513526/00e93901213fb80e5e7105d33ed12f2eb9389415.jpg"
        ],
        [
            "刘歆",
            "中国科学院数学与系统科学研究院",
            "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=f1ac380203f79052fb124f6c6d9abcaf/5ab5c9ea15ce36d30431c82130f33a87e950b1ee.jpg"
        ],
        [
            "姜鹏",
            "中国科学院国家天文台",
            "http://people.ucas.edu.cn/self/img/74ee1f6b-84be-4a15-bbf9-d89913f0803c.jpg"
        ]
    ]

after_people = []

for person in pre_people:
    after_people.append({"name":person[0], "info":person[1], "picture":person[2]})

print(after_people)