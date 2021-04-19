from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

app.debug = True
# 오류가 생기면 화면에 보여준다. 
# 나의 폴더 구조가 다 보인다 = 해킹에 취약 = 기본값이 False
# 개발할때만 True로 함

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    articles = Articles()
    # print(articles[0]['title'])
    # Cmd창에서 확인 가능함
    return render_template('articles.html', articles = articles)
    

@app.route('/gong')
def gong():
    return render_template('gong.html')



@app.route('/', methods=['GET'])
# 인자값으로 경로를 쓴다 (기본경로 뒤에 붙는다 = localhost:500/인자값)
# methods는 기본값이 Get

def index():
    # return 'Hello World!'
    return render_template('index.html', data = 'Gong')
    # 이후 파일에 html언어가 아닌 구문도 다 html로 바꿔서 날려준다 
    # render_templates의 기능
    #(파일명, 전달한 데이터)

if __name__ == '__main__':
    app.run()
# 이게 제일 먼저 시작한다 = 이 문서의 출발점 
# 다른 파이썬 파일들은 이 곳에서 컨트롤한다.
# 서버는 파일 1개에서 띄워진다.
# 거의 관용구처럼 사용
# 인자값 X = 여러가지로 변경 가능