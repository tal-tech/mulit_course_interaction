import interaction as inter
import numpy as np


def mulit_course_interaction(text):
    res = []
    for i in text:
        res.append(inter.interaction(i))
    return res


if __name__ == "__main__":
    text1 =  [
        {
            "text": "这句话呢，其实都是告诉你游戏规则，他就看你能不能看到他这个给你的规定了。",
            "begin_time": 1326750,
            "end_time":   1332165
        },
        {
            "text": "或者说你骂人一个游戏，它上面会有一个游戏的一个，这个攻略对不对？",
            "begin_time": 1334200,
            "end_time":   1339555
        },
    ]

    
    text2 = [{
            "text": "那你是不是要看到的这个游戏规则？女足知道了你这游戏谈话。",
            "begin_time": 1339540,
            "end_time":   1344105
        },
        {
            "text": "我什么时候该拐弯了或者什么？这种游戏是不是？",
            "begin_time": 1353120,
            "end_time":   1355985
        },
        {
            "text": "规则是不是那就是你看这句话呢76三呢，是游戏给你的一个攻略，告诉你这个游戏怎么玩",
            "begin_time": 1359510,
            "end_time":   1366485
        },
        {
            "text": "cc相同，是吧，那你看啊，这我就开始玩游戏的事嘛，对不对，那就按照他的这个说法来吧。",
            "begin_time": 1534130,
            "end_time":   1541365
        }
    ],
    text3 = [
        {
            "text": "这句话呢，其实都是告诉你游戏规则，他就看你能不能看到他这个给你的规定了。",
            "begin_time": 1326750,
            "end_time":   1332165
        },
        {
            "text": "或者说你骂人一个游戏，它上面会有一个游戏的一个，这个攻略对不对？",
            "begin_time": 1334200,
            "end_time":   1339555
        },
        {
            "text": "那你是不是要看到的这个游戏规则？女足知道了你这游戏谈话。",
            "begin_time": 1339540,
            "end_time":   1344105
        },
        {
            "text": "我什么时候该拐弯了或者什么？这种游戏是不是？",
            "begin_time": 1353120,
            "end_time":   1355985
        },
        {
            "text": "规则是不是那就是你看这句话呢76三呢，是游戏给你的一个攻略，告诉你这个游戏怎么玩",
            "begin_time": 1359510,
            "end_time":   1366485
        },
        {
            "text": "cc相同，是吧，那你看啊，这我就开始玩游戏的事嘛，对不对，那就按照他的这个说法来吧。",
            "begin_time": 1534130,
            "end_time":   1541365
        }
    ]

    text = [text1, text2, text3]
    
    print(mulit_course_interaction(text))