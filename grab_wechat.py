# -*- coding: utf-8 -*-
import itchat, sys, re
from collections import defaultdict
import thulac, nltk
from langdetect import detect
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def send(user_dict):
    remark_name = input("请输入用户昵称：")
    message = input("请输入消息内容： ")
    if remark_name == user_dict[0]["NickName"]:
        remark_name = ""
    else:
        remark_name = itchat.search_friends(remarkName=remark_name)[0]["UserName"]
    itchat.send(message, toUserName=remark_name)


def sex(user_dict):
    female = male = other = 0
    total = 0.0
    for info in user_dict:
        total += 1
        if info["Sex"] == 1:
            male += 1
        elif info["Sex"] == 2:
            female += 1
        else:
            other += 1
            print(info["RemarkName"])
    print("好友总数=%s" % int(total))
    print("男性好友=%s，女性好友=%s，未标明性别好友=%s" % (male, female, other))
    print("男性好友占比=%s，女性好友占比=%s" % (male / total, female / total))


def signature(user_dict):
    sig_dict = defaultdict(int)
    lst = []
    out_lst = [",", ".", "，", "。", "...", "～", "", "!", "！", "；", "(", ")", "（", "）", "", " ", "\n", "\t",
               "『", "』", "🏻", "「", "」"]
    thu1 = thulac.thulac(T2S=True)
    for info in user_dict:
        if info["Signature"] == "": continue
        sig = info["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
        sig = re.sub("< =.*/>", "", sig)
        if sig == "": continue
        lst.append(sig)
        try:
            lang = detect(sig)
        except:
            lang = ""
        if lang == "en":
            text = nltk.tokenize.word_tokenize(sig)
            sig_lst = nltk.pos_tag(text)
        elif "zh" in lang:
            sig_lst = thu1.cut(sig)
        # sig_lst = thu1.cut(sig)
        else:
            continue
        for token in sig_lst:
            if token[0] not in out_lst:
                word = token[0].lower()
                tag = token[1].lower()
                if tag.startswith("n") or tag.startswith("a"):
                    # sig_dict[(word, tag)] += 1
                    sig_dict[word] += 1
    # x = sorted(sig_dict.keys(), reverse=True)
    x = sorted(sig_dict.items(), key=lambda x:x[1], reverse=True)
    print(x[:30])
    # word_lst = []
    # for i, (word, num) in enumerate(x):
    #     word_lst.append(word)
    # return word_lst


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    # itchat.login()
    user_dict = itchat.get_friends()
    if len(sys.argv) <= 1:
        assert False, "Specify which function to use: 'send' or 'sex' or 'signature'"
    opt = sys.argv[1]
    if opt == "send":
        send(user_dict)
    elif opt == "sex":
        sex(user_dict)
    elif opt == "signature":
        signature(user_dict)
    else:
        assert False, "Invalid command line argument"
