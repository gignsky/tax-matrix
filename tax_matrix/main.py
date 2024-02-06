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
        # page.add(ft.Text(value=f"Entered Value: ${value.value}"))
        used_value.value = f"Subject Value being used: ${value_text_box.value}"
        page.update()

    def choose_county(e):
        # page.add(ft.Text(value=f"Selected County: {county_dropdown.value}"))
        selected_county.value = f"Selected County: {county_dropdown.value}"
        page.update()

    # declare value field for entering
    value_text_box = ft.TextField(
        hint_text="Enter Subject Value", value="", text_align="right"
    )

    # declare value field for displaying
    used_value = ft.Text(value=f"Subject Value being used: ${value_text_box.value}")
    page.add(used_value)

    list_of_county_dropdown_options = []
    # county options
    for county in list(counties):
        list_of_county_dropdown_options.append(ft.dropdown.Option(county))

    # declare county selector
    county_dropdown = ft.Dropdown(
        options=list_of_county_dropdown_options,
        on_change=choose_county,
        width=400,
    )

    # declare selected county field
    selected_county = ft.Text(value=f"Selected County: {county_dropdown.value}")
    page.add(selected_county)

    page.add(
        ft.Row(
            [value_text_box, ft.ElevatedButton("Submit Value", on_click=submit_value)]
        )
    )
    page.add(
        ft.Text(value="Please select a county: "),
    )
    page.add(county_dropdown)

ft.app(target=main)
