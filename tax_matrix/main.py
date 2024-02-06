import flet as ft
import subprocess
import time
import src

counties = src.county_data.counties.get_counties()
Subject=src.subject.Subject()

def main(page: ft.Page):
    title = ft.Text(value="Tax Matrix")
    version = ft.Text(value=f"Version: {src.config.current_version()}")
    update_date = ft.Text(value=f"Last Updated: {src.config.date_revised()}")

    page.controls.append(title)
    page.controls.append(version)
    page.controls.append(update_date)

    def submit_value(e):
        Subject.update_value(value_text_box.value)

    def choose_county(e):
        Subject.update_county(county_dropdown.value,counties[county_dropdown.value],counties[county_dropdown.value]["county_wide"])

    def choose_city(e):
        Subject.update_city(city_dropdown.value,Subject.county_dict["cities"][city_dropdown.value])


    # declare value field for entering
    value_text_box = ft.TextField(
        hint_text="Enter Subject Value", value="", text_align="right"
    )

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

    city_dropdown=ft.Dropdown(options=None,on_change=choose_city,width=200)

    page.add(city_dropdown)

ft.app(target=main)
