from os import rename, replace
import re
from flask import Flask, request

app = Flask(__name__)


# @app.route("/test", methods=["post"])
# def test():
#     temp = request.get_json()
#     print(temp)
#     if not "key" in temp:
#         return {"result": "test_succes"}
#     else:
#         return {"result": "test_fail"}


@app.route("/addr", methods=["post"])
def addr():
    temp = request.get_json()
    user_data = temp["num"]
    sum = 0
    mod = 0
    total = 0
    if user_data:
        if "num" in temp:
            if temp["num"]:
                re_user = user_data.replace("-", "")
                cdigitmulti = 2
                for i in range(len(re_user) - 1):
                    sum = sum + (int(re_user[i]) * cdigitmulti)
                    if i > 8:
                        cdigitmulti = 2
                    cdigitmulti += 1
                    mod = sum % 11
                    total = 11 - mod
                if int(total) == int(re_user[12]):
                    return {"result": "성공"}
                else:
                    return {"result": "체크디지트가 틀립니다."}
            else:
                print("value값이 없습니다.")
        else:
            print("key 값 num이 없습니다.")
    else:
        print("JSON 데이터가 없습니다..")


app.run(host="0.0.0.0", port=8080, debug=True)


# host='0.0.0.0', 외부 접속 테스트 하기 위해서
# port=8080, 포트 활당.
# debug=True 현재 코드가 수정되면 실시간으로 새로고침을 해준다.
