import flet as ft


def main(page: ft.Page):
    page.title = "¿Me perdonas?"
    page.bgcolor ="Pink"
    page.horizontal_aligment=ft.CrossAxisAlignment.CENTER
    page.vertical_aligment=ft.MainAxisAlignment.CENTER

    lbl1=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="bold"))
    ing1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50
                            )
    
    btnNo=ft.ElevatedButton("No",
                            color="green",
                            width=100,
                            height=50
                            )
    page.add(
        ft.Column(
            [
                lbl1,
                ing1,
                ft.Row(
                    [btnSi,btnNo]
                )
            ]
        )
    )
    
    
ft.app(main)
