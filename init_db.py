import sqlite3
import os

# 1. 连接到 SQLite 数据库（如果当前目录没有这个文件，它会瞬间自动创建一个）
db_path = 'my_database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. 创建数据表
cursor.execute('''
CREATE TABLE IF NOT EXISTS my_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    tag TEXT
)
''')

# 3. 清空旧数据（方便你以后反复运行这个脚本测试）
cursor.execute('DELETE FROM my_notes')

# 4. 写入测试数据
notes = [
    ('Python 与 SQLite', '放弃了 MySQL，发现 SQLite 真香，单文件直接起飞，没有密码烦恼！', '编程'),
    ('我的个人主页构想', '主页要简约，核心实现一个动态搜索功能，能查到我所有的笔记。', '想法'),
    ('射频与天线复习', '明天要考电磁场与微波技术，晚上得再看一遍阻抗匹配。', '学习'),
    ('2026年终总结', '今年用 FastAPI 配合 SQLite 完成了全栈小项目的开发！', '生活')
]

# 批量插入数据
cursor.executemany('INSERT INTO my_notes (title, content, tag) VALUES (?, ?, ?)', notes)

# 提交并关闭
conn.commit()
conn.close()

print(f"✅ 数据库初始化成功！快看左边，是不是多了一个 {db_path} 文件？")