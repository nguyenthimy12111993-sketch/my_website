from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 在这里定义本地管理员密码
ADMIN_PASSWORD = "521478"

@app.get("/")
def read_root():
    html_path = os.path.join(BASE_DIR, "index.html")
    
    if os.path.exists(html_path):
        return FileResponse(html_path)
    else:
        return HTMLResponse(f"<h2>出错了：找不到网页文件</h2><p>Python 去这个路径找了：<br>{html_path}</p><p>请检查这个路径下有没有 index.html 文件！</p>")

@app.get("/api/search")
def search_students(keyword: str = Query(""), password: str = Query("")):
    
    # 在查询文件前先验证密码
    if password != ADMIN_PASSWORD:
        return {"status": "error", "message": "管理员密码错误，拒绝访问！"}

    data_file = os.path.join(BASE_DIR, 'data.json')
    
    if not os.path.exists(data_file):
        return {"status": "error", "message": f"找不到 data.json，查找路径: {data_file}"}

    with open(data_file, 'r', encoding='utf-8') as f:
        students = json.load(f)

    if keyword:
        keyword = keyword.lower()
        results = []
        for student in students:
            student_info_str = f"{student['name']} {student['student_id']} {student['school']} {student['dormitory']} {student['grade']}".lower()
            if keyword in student_info_str:
                results.append(student)
    else:
        results = students

    return {"status": "success", "data": results}