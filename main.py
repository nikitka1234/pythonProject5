from flask import Flask, render_template, redirect


app = Flask(__name__)

content = [
    {"title": "Название для шаблона из словаря", "text": "Текст для шаблона из словаря"},
    {"title": "Экс-глава регионального СК назначен главным федеральным инспектором", "text": "Бывший руководитель следственного управления Следственного комитета по Свердловской области Михаил Богинский назначен главным федеральным инспектором региона. Как сообщили в пресс-службе полпредства, соответствующее распоряжение подписал полномочный представитель президента в УрФО Владимир Якушев."},
    {"title": "Посол Швейцарии выступил в защиту отказа от передачи Украине боеприпасов", "text": "Посол Швейцарии в Берлине Пауль Зегер выступил в защиту решения правительства страны об отказе передавать Украине боеприпасы швейцарского производства. О своей позиции он заявил изданию Augsburger Allgemeine."}
]

content2 = {"title": "Название для шаблона из словаря",
            "text": "Текст для шаблона из словаря",
            1: False, 4: "<h1>text</h1>"}


def index():
    return render_template("index.html", news_list=content)


def news():
    return "Новости"


def news_detail(id):
    return render_template("news_detail.html", **content[id])


def category(name):
    return f"Категория {name}"


def test():
    return render_template("test.html", content=content2)


app.add_url_rule('/', 'index', index)
app.add_url_rule('/news', 'news', news)
app.add_url_rule('/news_detail/<int:id>', 'news_detail', news_detail)
app.add_url_rule('/category/<string:name>', 'category', category)
app.add_url_rule('/test', 'test', test)
