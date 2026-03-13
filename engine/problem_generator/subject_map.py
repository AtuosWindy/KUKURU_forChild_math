from .grade1 import subject_1001, subject_1002, subject_1003, subject_1004
from .grade2 import subject_2001, subject_2002, subject_2003, subject_2004
from .grade3 import subject_3001, subject_3002, subject_3003, subject_3004
from .grade4 import subject_4001, subject_4002, subject_4003, subject_4004
from .grade5 import subject_5001, subject_5002, subject_5003, subject_5004
from .grade6 import subject_6001, subject_6002, subject_6003, subject_6004

SUBJECT_MAP = {
    1001: subject_1001,	#1年生, 1桁の足し算
    1002: subject_1002,	#1年生, 1桁の引き算
    1003: subject_1003,	#1年生, 繰り上がりのある足し算
    1004: subject_1004,	#1年生, 繰り下がりのある引き算
    2001: subject_2001,	#2年生, 2桁の足し算
    2002: subject_2002,	#2年生, 2桁の引き算
    2003: subject_2003,	#2年生, 筆算(mix)
    2004: subject_2004,	#2年生, 九九
    3001: subject_3001,	#3年生, 3桁の足し算・引き算
    3002: subject_3002,	#3年生, かけ算（2桁 × 1桁）
    3003: subject_3003,	#3年生, わり算（1桁）
    3004: subject_3004,	#3年生, あまりのあるわり算
    4001: subject_4001,	#4年生, かけ算（2桁 × 2桁）
    4002: subject_4002,	#4年生, わり算（2桁 ÷ 1桁）
    4003: subject_4003,	#4年生, わり算（筆算）
    4004: subject_4004,	#4年生, 小数の足し算・引き算
    5001: subject_5001,	#5年生, 小数 × 小数
    5002: subject_5002,	#5年生, 小数 ÷ 小数
    5003: subject_5003,	#5年生, 分数の足し算
    5004: subject_5004,	#5年生, 分数の引き算
    6001: subject_6001,	#6年生, 分数 × 分数
    6002: subject_6002,	#6年生, 分数 ÷ 分数
    6003: subject_6003,	#6年生, 文字式（簡単な式）／例：x + 3 = 7とか
    6004: subject_6004,	#6年生, エキストラ問題
}

SUBJECT_NAME_MAP = {
    1: {
        1: "1桁の足し算",
        2: "1桁の引き算",
        3: "繰り上がりのある足し算",
        4: "繰り下がりのある引き算",
    },
    2: {
        1: "2桁の足し算",
        2: "2桁の引き算",
        3: "筆算（足し算・引き算）",
        4: "九九",
    },
    3: {
        1: "3桁の足し算・引き算",
        2: "かけ算（2桁 × 1桁）",
        3: "わり算（1桁）",
        4: "あまりのあるわり算",
    },
    4: {
        1: "かけ算（2桁 × 2桁）",
        2: "わり算（2桁 ÷ 1桁）",
        3: "わり算（筆算）",
        4: "小数の足し算・引き算",
    },
    5: {
        1: "小数 × 小数",
        2: "小数 ÷ 小数",
        3: "分数の足し算",
        4: "分数の引き算",
    },
    6: {
        1: "分数 × 分数",
        2: "分数 ÷ 分数",
        3: "文字式",
        4: "エキストラ問題",
    },
}