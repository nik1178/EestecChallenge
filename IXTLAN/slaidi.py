import flet as ft
import main as mn

t = ""

option = 0
# 0 = topic
# 1 = script
# 2 = prov like seminarska -> article

def main(page: ft.Page):
    page.theme_mode = "light"

    def text_button_clicked(e):
        t.value = f'{tb1.value}'
        page.update()
        print(t)  # --> kle poslemo t v uno od nika
        print(option)
        # print(optiontxt)
        robot = mn.PresentationGenerator(t.value)
        robot.generate_presentation()

    def barvaj_gumb(kateri):
        if kateri == 0:
            b1.bgcolor = '#cc33ccff'
            b2.bgcolor = '#aaaaaaaa'
            b3.bgcolor = '#aaaaaaaa'
        elif kateri == 1:
            b1.bgcolor = '#aaaaaaaa'
            b2.bgcolor = '#cc33ccff'
            b3.bgcolor = '#aaaaaaaa'
        else:
            b1.bgcolor = '#aaaaaaaa'
            b2.bgcolor = '#aaaaaaaa'
            b3.bgcolor = '#cc33ccff'

    text = ft.Text()
    text.value = "Please enter the topic you would like to present:"
    text.size = 20

    def zamenjaj_opcijo0(e):
        global option
        text.value = "Please enter the topic you would like to present:"
        option = 0
        barvaj_gumb(0)
        page.update()

    def zamenjaj_opcijo1(e):
        global option
        option = 1
        text.value = "Please enter the script you would like to present:"
        barvaj_gumb(1)
        page.update()
        

    def zamenjaj_opcijo2(e):
        global option
        option = 2
        text.value = "Please enter the article you would like to present:"
        barvaj_gumb(2)
        page.update()     

    def izpisi(e):
        global text_to_present
        return text_to_present

    page.title = "Text custom styles"
    page.scroll = "adaptive"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # PAGE TITLE
    page.add(
        ft.Text("Sl", size=50, weight=ft.FontWeight.W_500, 
                spans=[ft.TextSpan("AI", ft.TextStyle(size=50, weight=ft.FontWeight.W_700)), ft.TextSpan("di", ft.TextStyle(size=50, weight=ft.FontWeight.W_500))]),
        # vprasaj uporabnika zeli le zgeneriran ppt ali tudi tekst
        ft.Text(
            "Which of the following do you already have?",
            size=20, text_align=ft.TextAlign.NONE
        )
    )
    global opcija

    global b1, b2, b3

    b1 = ft.Container(
        content=ft.Text("Topic"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=10,
        ink=True,
        bgcolor=ft.Container(bgcolor='#aaaaaaaa'),
        on_click=zamenjaj_opcijo0,
    )

    b2 = ft.Container(
        content=ft.Text("Script"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=10,
        ink=True,
        bgcolor=ft.Container(bgcolor='#aaaaaaaa'),
        on_click=zamenjaj_opcijo1,
    )

    b3 = ft.Container(
        content=ft.Text("Article"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=10,
        ink=True,
        bgcolor=ft.Container(bgcolor='#aaaaaaa'),
        on_click=zamenjaj_opcijo2,
    )
    # dodaj gumbe in tekst na stran
    page.add(
        ft.Row(
            [b1, b2, b3],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
    page.add(text)
    page.update()

    global t
    t = ft.Text()
    tb1 = ft.TextField(label="User input", multiline=True, max_lines=20, max_length=120000)
    b = ft.ElevatedButton(text="Submit", on_click=text_button_clicked, bgcolor=ft.colors.INDIGO_50)
    page.add(tb1, b)

ft.app(target=main)