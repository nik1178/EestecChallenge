import flet as ft
import main as mn
import os

t = ""
background_image = ""

option = 0
# 0 = topic
# 1 = script
# 2 = prov like seminarska -> article

def main(page: ft.Page):
    # set basic page settings
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "SlAIdi"
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text = ft.Text()
    text.value = "Please enter the topic you would like to present:"
    text.size = 20

    def submit_click(e):
        t.value = f'{input_request.value}'
        page.update()
        print(t)  # --> kle poslemo t v uno od nika
        print(option)
        # poslji prompt, katero opcijo uporabljamo in pot background imagea
        slide_generator = mn.PresentationGenerator(t.value, option, background_image)
        slide_generator.generate_presentation()

    def barvaj_gumb(kateri):
        if kateri == 0:
            b1.bgcolor = '#bbffb3b3'
            b2.bgcolor = '#bbbbbbbb'
            b3.bgcolor = '#bbbbbbbb'
        elif kateri == 1:
            b1.bgcolor = '#bbbbbbbb'
            b2.bgcolor = '#bbffb3b3'
            b3.bgcolor = '#bbbbbbbb'
        else:
            b1.bgcolor = '#bbbbbbbb'
            b2.bgcolor = '#bbbbbbbb'
            b3.bgcolor = '#bbffb3b3'

    # posodobi globalno spremenljivko in spremeni tekst ter barvo gumba
    def klik_gumba(e, gumb):
        global option
        if gumb == 0:
            option = 0
            text.value = "Please enter the topic you would like to present:"
        elif gumb == 1:
            option = 1
            text.value = "Please enter the script you would like to present:"
        else:
            option = 2
            text.value = "Please enter the article you would like to present:"
        barvaj_gumb(gumb)
        page.update()

    # zapomni si pot do izbrane slike
    def file_selected(event):
        global background_image
        if event and event.files:
            path = event.files[0].path  # Accessing the file path directly from the event object
            print(path)
            background_image = path
        else:
            print("No file selected.")

    # PAGE TITLE
    page.add(
        ft.Text("Sl", size=50, weight=ft.FontWeight.W_500, 
                spans=[ft.TextSpan("AI", ft.TextStyle(size=50, weight=ft.FontWeight.W_700, color="#fc5858")), ft.TextSpan("di", ft.TextStyle(size=50, weight=ft.FontWeight.W_500))]),
        # vprasaj uporabnika zeli le zgeneriran ppt ali tudi tekst
        ft.Text(
            "Which of the following do you already have?",
            size=20, text_align=ft.TextAlign.NONE
        )
    )
    file_picker = ft.FilePicker(on_result=file_selected)
    page.overlay.append(file_picker)
    # gumbi so kontejnerji
    global b1, b2, b3, background_picker
    b1 = ft.Container(
        content=ft.Text("Topic"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=50,
        border_radius=15,
        ink=True,
        bgcolor='#bbbbbbbb',
        on_click=lambda e: klik_gumba(e, 0),
    )

    b2 = ft.Container(
        content=ft.Text("Script"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=50,
        border_radius=15,
        ink=True,
        bgcolor='#bbbbbbbb',
        on_click=lambda e: klik_gumba(e, 1),
    )

    b3 = ft.Container(
        content=ft.Text("Article"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=50,
        border_radius=15,
        #ink=True,
        bgcolor='#bbbbbbbb',
        on_click=lambda e: klik_gumba(e, 2),
    )

    background_picker = ft.Container(
        content=ft.Text("Choose Background image (optional)"),
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_left ,
        width=270,
        height=40,
        border_radius=5,
        ink=True,
        bgcolor='#bbbbbbbb',
        on_click=lambda e: file_picker.pick_files(file_type="image"),
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
    input_request = ft.TextField(label="User input", multiline=True, max_lines=20, max_length=120000)
    submit = ft.ElevatedButton(text="Submit", on_click=submit_click, bgcolor=ft.colors.INDIGO_50)
    # na klik se odpre okno, ki dovoli samo slike
    # background_picker = ft.ElevatedButton("Choose Background image (optional)", on_click=lambda _: file_picker.pick_files(file_type="image"))
    page.add(input_request)
    page.add(ft.Row(
            [background_picker],
            alignment=ft.MainAxisAlignment.START,
    ))
    page.add(submit)
    page.update()

ft.app(target=main)