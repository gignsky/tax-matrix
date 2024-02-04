import flet as ft
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


ft.app(target=main)
