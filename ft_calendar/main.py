import flet as ft

from datetime import date
import calendar

obj = calendar.Calendar()


def main(page: ft.Page):

    _content_dic = {}
    _year_now = int(date.today().strftime("%Y"))
    _month_now = int(date.today().strftime("%m"))
    _day_now = int(date.today().strftime("%d"))

    def DeleteAnimation(e):
        if e.data == "true":
            e.control.content.controls[0].offset = ft.ft.transform.Offset(-0.50, 0)
            e.control.content.controls[0].update()

            e.control.content.controls[0].opacity = 1
            e.control.content.controls[0].update()
        else:
            e.control.content.controls[0].offset = ft.ft.transform.Offset(0, 0)
            e.control.content.controls[0].update()

            e.control.content.controls[0].opacity = 0
            e.control.content.controls[0].update()

    def _create_entry(e):
        _content_column.controls.append(
            ft.Row(
                controls=[
                    ft.Container(
                        border_radius=8,
                        padding=12,
                        expand=True,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.center_right,
                            colors=["#1e293b", "shadow"],
                        ),
                        content=ft.Text(
                            f"You have a task on\n{e.control.data}",
                            size=10,
                        ),
                    ),
                    ft.Container(
                        alignment=ft.alignment.center_right,
                        animate=ft.animation.Animation(1000, "ease"),
                        on_hover=lambda e: DeleteAnimation(e),
                        content=ft.Row(
                            alignment="end",
                            spacing=0,
                            controls=[
                                ft.Text(
                                    "DELETE",
                                    opacity=0,
                                    size=9,
                                    offset=ft.transform.Offset(0, 0),
                                    animate_offset=ft.animation.Animation(
                                        duration=900, curve="ease"
                                    ),
                                    animate_opacity=200,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_ROUNDED,
                                    icon_size=19,
                                    icon_color="#dc2626",
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )
        _content_column.update()

    def _highlight_date(e):

        if e.control.bgcolor == "#0c4a6e":
            pass
        else:
            if e.data == "true":
                e.control.bgcolor = "white10"
                e.control.update()
            else:
                e.control.bgcolor = "#0c0f16"
                e.control.update()

    def _popup(e):
        _title.visible = False
        _title.update()
        if e.control.height != _main.height * 0.55:
            e.control.height = _main.height * 0.55
            e.control.update()

            for key in _content_dic:
                for month in _content_dic[key]:
                    if month == _month_now and key == _year_now:
                        _content_dic[key][month].visible = True
                        _content_dic[key][month].update()
        else:
            for key in _content_dic:
                for month in _content_dic[key]:
                    if month == _month_now and key == _year_now:
                        _content_dic[key][month].visible = False
                        _content_dic[key][month].update()

            e.control.height = _main.height * 0.13
            e.control.update()
            _title.visible = True
            _title.update()

    # 1
    _main = ft.Container(
        width=290,
        height=590,
        border_radius=35,
        bgcolor="black",
        padding=8,
        alignment=ft.alignment.bottom_center,
    )

    # 2
    _main_column = ft.Column(spacing=2, scroll="auto", alignment="start")

    # 3
    _calendar_ft_Container = ft.Container(
        width=_main.width,
        height=_main.height * 0.13,
        border_radius=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=["#1e293b", "#0f172a"],
        ),
        alignment=ft.alignment.center,
        # 3.1 => do this after 3
        on_click=lambda e: _popup(e),
        animate=ft.animation.Animation(duration=320, curve="decelerate"),
    )

    # 4
    _calendar_ft_Container.content = _main_column

    # 5
    _title = ft.Container(
        content=ft.Text(
            "SCHEDULE",
            color="white70",
            weight="bold",
        )
    )
    _main_column.controls.append(_title)

    # 6
    _content_column = ft.Column(
        scroll="auto",
        expand=True,
        alignment="start",
        controls=[
            ft.Container(
                padding=15,
                content=ft.Text(
                    "Scheduled Tasks",
                    color="white70",
                    weight="bold",
                    size=13,
                ),
            )
        ],
    )

    # 7
    _main.content = ft.Column(
        alignment="end",
        controls=[
            ft.Container(
                expand=True,
                content=_content_column,
            ),
            _calendar_ft_Container,
        ],
    )

    # 8
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # 9
    weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    _ft_Row_weekday = ft.Row(
        spacing=2,
        alignment="center",
    )

    # 10
    for day in weekday:
        _ft_Row_weekday.controls.append(
            ft.Container(
                width=32,
                height=32,
                border_radius=5,
                alignment=ft.alignment.center,
                content=ft.Text(day, size=9, color="white70"),
            )
        )

    #

    # 11
    for year in range(2022, 2024):
        _content_dic[year] = {}
        for month in range(11, 12):
            #
            _inner_column = ft.Column(
                horizontal_alignment="start",
                spacing=2,
            )
            _inner = ft.Container(
                visible=False,
                content=_inner_column,
            )
            _main_column.controls.append(_inner)
            #
            _ft_Row_year = ft.Row(
                spacing=2,
                alignment="center",
                controls=[
                    ft.Text(f"{months[month - 1]} {year}", size=12),
                ],
            )
            _inner_column.controls.append(_ft_Row_year)
            #
            _inner_column.controls.append(_ft_Row_weekday)

            #
            for days in obj.monthdayscalendar(year, month):
                _ft_Row = ft.Row(
                    spacing=2,
                    alignment="center",
                )
                _inner_column.controls.append(_ft_Row)
                for day in days:
                    if day != 0:
                        __ = ft.Container(
                            width=32,
                            height=32,
                            bgcolor="#0c0f16",
                            border_radius=5,
                            alignment=ft.alignment.center,
                            content=ft.Text(
                                f"{day}",
                                size=10,
                                color="white70",
                            ),
                            data=f"{months[month - 1]} {day}, {year}",
                            on_click=lambda e: _create_entry(e),
                            on_hover=lambda e: _highlight_date(e),
                        )
                        _ft_Row.controls.append(__)

                        # if month == _month_now and day == _day_now:
                        #     __.bgcolor = "#0c4a6e"

                    else:
                        _ft_Row.controls.append(
                            ft.Container(
                                width=32,
                                height=32,
                                border_radius=8,
                            )
                        )

            _content_dic[year][month] = _inner

    # first setup
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(
        ft.Container(
            width=1400,
            height=750,
            padding=ft.padding.only(right=120),
            alignment=ft.alignment.center_right,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                # colors=["#111827", "#1e3a8a"],
                # colors=["#1e3a8a", "#111827"],
                colors=["#0f172a", "#64748b"],
            ),
            content=ft.Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[_main],
            ),
        )
    )
    page.update()


ft.app(target=main)
