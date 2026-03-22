from .grade1 import subject_1001, subject_1002, subject_1003, subject_1004
from .grade2 import subject_2001, subject_2002, subject_2003, subject_2004
from .grade3 import subject_3001, subject_3002, subject_3003, subject_3004
from .grade4 import subject_4001, subject_4002, subject_4003, subject_4004
from .grade5 import subject_5001, subject_5002, subject_5003, subject_5004
from .grade6 import subject_6001, subject_6002, subject_6003, subject_6004

#学年(grade)ごとの単元(subject)の関数マッピング。

#各学年の単元や、単元名に使用した漢字は、文科省の以下の資料を参考にしております。
#https://www.mext.go.jp/a_menu/shotou/new-cs/youryou/syo/koku/__icsFiles/afieldfile/2016/10/27/1234920.pdf

#各難易度の問題数は、単元ごとの難易度や、回答形式(*1)、心理的にキリの良い数などを考慮し設定しております。
#*1 : かんたん→４択の選択式 ／ ふつう・むずかしい→入力式
#*2 : 注意　ー　単元6004(エキストラ問題)のみ、難易度MAX・入力式固定とします！！

SUBJECT_MAP = {
    #grade1
    #1年生, 1桁の足し算
    1001: {
        "func": subject_1001,
        "count": [5, 5, 10],
        "name": "たしざん",
    },
    #1年生, 1桁の引き算
    1002: {
        "func": subject_1002,
        "count": [5, 5, 10],
        "name": "ひきざん",
    },
    #1年生, 1桁の足し算（繰り上がりあり）
    1003: {
        "func": subject_1003,
        "count": [5, 10, 10],
        "name": "たしざん(くりあがり)",
    },
    #1年生, 1桁の(答えの)引き算（繰り下がりあり）
    1004: {
        "func": subject_1004,
        "count": [10, 10, 15],
        "name": "ひきざん(くりさがり)",
    },

    #grade2
    #2年生, 2桁の足し算
    2001: {
        "func": subject_2001,
        "count": [10, 10, 15],
        "name": "足し算(2けた)",
    },
    #2年生, 2桁の引き算
    2002: {
        "func": subject_2002,
        "count": [10, 10, 15],
        "name": "引き算(2けた)",
    },
    #2年生, 2桁の足し算・引き算（筆算）
    2003: {
        "func": subject_2003,
        "count": [10, 15, 15],
        "name": "ひっ算",
    },
    #2年生, 九九
    2004: {
        "func": subject_2004,
        "count": [5, 10, 10],
        "name": "九九(くく)",
    },

    #grade3
    #3年生, 3桁の足し算・引き算
    3001: {
        "func": subject_3001,
        "count": [10, 10, 15],
        "name": "足し算・引き算(3けた)",
    },
    #3年生, かけ算（2桁 × 1桁）
    3002: {
        "func": subject_3002,
        "count": [10, 10, 15],
        "name": "かけ算",
    },
    #3年生, わり算（1桁）
    3003: {
        "func": subject_3003,
        "count": [10, 10, 15],
        "name": "わり算",
    },
    #3年生, あまりのあるわり算
    #3004: {
    #    "func": subject_3004,
    #    "count": [10, 15, 15],
    #    "name": "わり算(あまりあり)",
    #},

    #grade4
    #4年生, かけ算（2桁 × 2桁）
    4001: {
        "func": subject_4001,
        "count": [10, 10, 15],
        "name": "かけ算(2けた)",
    },
    #4年生, わり算（2桁 ÷ 1桁）
    4002: {
        "func": subject_4002,
        "count": [10, 10, 15],
        "name": "わり算(2けた)",
    },
    #4年生, わり算（筆算）
    #4003: {
    #    "func": subject_4003,
    #    "count": [10, 15, 20],
    #    "name": "わり算(ひっ算)",
    #},
    #4年生, 小数の足し算・引き算
    4004: {
        "func": subject_4004,
        "count": [10, 10, 15],
        "name": "小数(足し算・引き算)",
    },

    #grade5
    #5年生, 小数 × 小数
    5001: {
        "func": subject_5001,
        "count": [10, 15, 20],
        "name": "小数 × 小数",
    },
    #5年生, 小数 ÷ 小数
    5002: {
        "func": subject_5002,
        "count": [10, 15, 20],
        "name": "小数 ÷ 小数",
    },
    #5年生, 分数の足し算
    5003: {
        "func": subject_5003,
        "count": [10, 15, 20],
        "name": "分数 ＋ 分数",
    },
    #5年生, 分数の引き算
    5004: {
        "func": subject_5004,
        "count": [10, 15, 20],
        "name": "分数 ― 分数",
    },

    #grade6
    #6年生, 分数 × 分数
    6001: {
        "func": subject_6001,
        "count": [10, 15, 20],
        "name": "分数 × 分数",
    },
    #6年生, 分数 ÷ 分数
    6002: {
        "func": subject_6002,
        "count": [10, 15, 20],
        "name": "分数 ÷ 分数",
    },
    #6年生, 文字式（簡単な式）／例：x + 3 = 7とか
    6003: {
        "func": subject_6003,
        "count": [10, 20, 25],
        "name": "文字式",
    },
    #6年生, エキストラ問題
    # 6004: {
    #     "func": subject_6004,
    #     "count": [20, 20, 20],
    #     "name": "総合チャレンジ!!",
    # },
}
