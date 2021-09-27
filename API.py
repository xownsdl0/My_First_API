from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['post'])

def test():
    return {"result" : "test_succes"}

app.run(host='0.0.0.0', port=8080, debug=True)


# host='0.0.0.0', 외부 접속 테스트 하기 위해서
# port=8080, 포트 활당.
# debug=True 현재 코드가 수정되면 실시간으로 새로고침을 해준다.