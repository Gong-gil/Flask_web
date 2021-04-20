from flask import Flask, render_template, request, redirect
from data import Articles
import pymysql


app = Flask(__name__)

app.debug = True
# 오류가 생기면 화면에 보여준다. 
# 나의 폴더 구조가 다 보인다 = 해킹에 취약 = 기본값이 False
# 개발할때만 True로 함

db = pymysql.connect(
    host ='localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    # articles = Articles()
    # Articles() -> data.py의 메소드를 의미

    # print(articles[0]['title'])
    # Cmd창에서 확인 가능함
    return render_template('articles.html', articles = topics)


@app.route('/article/<int:id>')
# .../<id> = params = 변수사용가능
# 정수로 받고 싶을때 int:___로 사용

def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic where id ={};' .format(id)
    cursor.execute(sql)
    topics = cursor.fetchone()
    # 선택된 데이터 1개만 인스터스에 저장한다.

    

    # articles = Articles()
    # article = articles[id-1]
    # # print(articles[id-1])
    return render_template('article.html', article = topics)



@app.route('/add_articles', methods = ['POST', 'GET'])
def add_articles():
    cursor = db.cursor()
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']
        # form[__]은 add_article.html의 input태그의 name에 해당되는 값을 입력한다.

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author]

        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()   <- 오류의 원인이였음

        return redirect('/articles') 
    else:
        return render_template('add_articles.html')
# methods =/= request.method : -s의 여부 확인하기

# @app.route('/add_articles', methods = ['POST'])
# def insert_aricles():
#     return 'Success'      를 if문으로 돌릴거임



@app.route('/', methods=['GET'])
# 인자값으로 경로를 쓴다 (기본경로 뒤에 붙는다 = localhost:500/인자값)
# methods는 기본값이 Get

def index():
    # return 'Hello World!'
    return render_template('index.html', data = 'Gong')
    # 이후 파일에 html언어가 아닌 구문도 다 html로 바꿔서 날려준다 
    # render_templates의 기능
    #(파일명, 전달한 데이터)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    sql = 'DELETE FROM topic WHERE id = %s;'
    id = [id]
    # [id] = <int:id> /// .format()방법말고도 또 있다
    cursor.execute(sql, id)
    db.commit()
    
    return redirect('/articles') 


if __name__ == '__main__':
    app.run()
# 이게 제일 먼저 시작한다 = 이 문서의 출발점 
# 다른 파이썬 파일들은 이 곳에서 컨트롤한다.
# 서버는 파일 1개에서 띄워진다.
# 거의 관용구처럼 사용
# 인자값 X = 여러가지로 변경 가능