import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []

    i = 0
    while i < total_num:
        j = 0
        forecast = ""
        while j < num_sentences:
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = t.title() + " " + a + " " + p + "."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1

        prophecies.append(forecast)
        i = i + 1

    return prophecies
def generate_about():
    about=f"""
    """

    times_html="<ul>"
    for t in times:
        times_html=times_html + "<li>" + t + "</li>"
    times_html=times_html + "</ul>"

    advices_html="<ul>"
    for ad in advices:
        advices_html=advices_html + "<li>" + ad + "</li>"
    advices_html=advices_html + "</ul>"

    promises_html="<ul>" 
    for p in promises:
        promises_html=promises_html + "<li>" + p + "</li>"
    promises_html=promises_html + "</ul>"
    
    about= f"""<h2>Используются следующие параметры для генерации:</h2>
    <img src=http://ysia.ru/wp-content/uploads/2018/01/goro.jpg
     width=100px height=100px>
    <ol>
    <li>Времена дня: {times_html} </li>
    <li>Глоголы: {advices_html} </li>
    <li>Обещания: {promises_html} </li>
    </ol>"""

    about=about + f"""
    <hr><p><a href="index.html">К предсказаниям</a> </p>
    """
    return about