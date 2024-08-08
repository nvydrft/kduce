from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # 엑셀 파일 읽기
    df = pd.read_excel('result4.xlsx')
    # HTML 테이블로 변환
    excel_data = df.to_html(index=False, classes='excel-table')
    return render_template('index.html', excel_data=excel_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')