import flet as ft

t=""

# 0 = topic
# 1 = script
# 2 = prov like seminarska -> article


def main(page: ft.Page):
    def text_button_clicked(e):
        t.value = f'{tb1.value}'
        page.update()
        print(t)  #--> kle poslemo t v uno od nika
        #print(optiontxt)
    
    """
    def switch_option(e):
        global optiontxt 
        if (switch.value == True):
            optiontxt = 1
        else:
            optiontxt = 0
            #print(optiontxt)
    """

    text = ft.Text()
    text.value = "Please enter the topic you would like to present:"
    text.size = 20

    a = ft.Container(
                    content=ft.Text("Topic"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    bgcolor=ft.colors.GREY_100,
                    on_click=zamejajopcijo0,
                )
    b = ft.Container(
                    content=ft.Text("Script"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    bgcolor=ft.colors.GREY_100,
                    on_click=zamejajopcijo0,
                )
    c = ft.Container(
                    content=ft.Text("Article"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    bgcolor=ft.colors.GREY_100,
                    on_click=zamejajopcijo2,
                )

    def zamejajopcijo0(e):
        text.value = "Please enter the topic you would like to present:"
        a.bgcolor = ft.colors.RED_100
        page.update()
    
    def zamejajopcijo1(e):
        text.value = "Please enter the script you would like to present:"
        a.bgcolor = ft.colors.RED_100
        page.update()

    def zamejajopcijo2(e):
        text.value = "Please enter the article you would like to present:"
        a.bgcolor = ft.colors.RED_100
        page.update()

    def izpisi(e):
        global text_to_present
        return text_to_present
    


    page.title = "Text custom styles"
    page.scroll = "adaptive"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # naslov
    page.add(
        ft.Text("Presenter.io", size=60, weight=ft.FontWeight.W_900, selectable=True),
        # vprasaj uporabnika zeli le zgeneriran ppt ali tudi tekst
        ft.Text(
            "Which of the following do you already have?",
            size=20, text_align=ft.TextAlign.NONE
        )
    )

    global opcija

    page.add(
        ft.Row(
            [
                a,
                b,
                c,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    page.add(text)


    global t
    t = ft.Text()
    tb1 = ft.TextField(label="User input", multiline=True, max_lines=10, max_length = 120000)
    b = ft.ElevatedButton(text="Submit", on_click=text_button_clicked, bgcolor=ft.colors.INDIGO_50)


    #bb = ft.ElevatedButton("Gumb", on_click=button_clicked, bgcolor=ft.colors.INDIGO_50)

    #page.add(tb1,b,bb)

    # switch
    #switch = ft.CupertinoSwitch(value=True, on_change=switch_option)   

    page.add(tb1,b)

ft.app(target=main)