import flet as ft
import subprocess
import time
import src

counties = src.county_data.counties.get_counties()


def main(page: ft.Page):
    title = ft.Text(value="Tax Matrix")
    version = ft.Text(value=f"Version: {src.config.current_version()}")
    update_date = ft.Text(value=f"Last Updated: {src.config.date_revised()}")

    page.controls.append(title)
    page.controls.append(version)
    page.controls.append(update_date)

    page.update()

    def submit_value(e):
        page.add(ft.Text(value=f"Entered Value: ${value.value}"))

    #     t = ft.Text()
    #     page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()
    #
    #     for i in range(10):
    #         t.value = f"Step {i}"
    #         page.update()
    #         time.sleep(1)

    value = ft.TextField(hint_text="Enter Subject Value")

    page.add(ft.Row([value, ft.ElevatedButton("Submit Value", on_click=submit_value)]))


ft.app(target=main)
