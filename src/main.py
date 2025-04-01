import flet as ft
from ssh_hosts import hosts_dicts_list as hdl
import multiprocessing
import asyncio

multiprocessing.set_start_method("spawn")

black = "#332323"
bg_white = "#EEE2DE"
main_bg = "#2a213e"
secondary_bg = "#201E43"
red_1 = '#B31312'
light_orange = '#EA906C'
glass_orange = '#55FC6736'
orange = '#FC6736'

# hosts_count = sum([1 for item in hdl])


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = '#232323'
    page.title = 'Ansible Assistant'
    page.window.width = 480
    page.window.height = 750
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.BLUE,
    )

    def hosts_boxes(list):  # check box for each item in hdl
        i = 0
        result = []
        for item in list:
            result.append(
                ft.dropdownm2.Option(
                    data=hdl[i],
                    text=hdl[i]['Host'],
                    on_click=button_clicked,
                    alignment=ft.alignment.center))
            i += 1
        return result

    Installing_status = ft.Text()

    hostname = ft.Text(value='')
    username = ft.Text(value='')
    keypath = ft.Text(value='')
    portno = ft.Text(value='')

    def button_clicked(e):
        page.update()
        respone.value = f"Host \' {dd.value} \' selected"
        page.update()
        print(dd.value)
        t = 0
        for host_info in hdl:
            if dd.value == host_info['Host']:
                hostname.value = host_info['Host']
                username.value = host_info['remote_user']
                keypath.value = host_info['private_key_file']
                portno.value = host_info['Port']
                page.update()
                break
            else:
                t += 1

    error = ft.TextField(
        '',
        color=bg_white,
        text_size=12,
        border_color='transparent',
        max_lines=100,
        read_only=True)
    monitor = ft.Column(controls=[error], scroll='auto')
    monitor_container = ft.Column(controls=[ft.Container(
        content=ft.Container(
            content=monitor,
            margin=0,
            padding=5,
            alignment=ft.alignment.center,
            gradient=ft.RadialGradient(
                colors=[black, secondary_bg], radius=1.5),
            height=250,
            width=450,
            border_radius=15
        ), width=500,
        height=250,
        bgcolor='#5f6176',
        border_radius=10
    )
    ]
    )

    async def ans_ins(e):
        # ... existing checkbox logic ...
        Docker_value = main_screen.content.controls[2].controls[0].value
        PostgreSQL_value = main_screen.content.controls[2].controls[1].value
        Node_value = main_screen.content.controls[2].controls[2].value
        Mongodb_value = main_screen.content.controls[2].controls[3].value
        if Docker_value:
            Installing_status.value = 'installing Docker...'
            page.update()

            cmd = (
                f'ansible-playbook ./assets/ansible/docker.yml '
                f'--user={username.value} '
                f'-c ssh '
                f'-i "{hostname.value}," '
                f'--private-key={keypath.value} '
                # f'-e "ansible_port={portno.value}" ' # uncomment here if port
                # needed
                f'-e "ansible_python_interpreter=/usr/bin/python3" -v'
            )

            try:
                process = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                # Real-time output
                while True:
                    output = await process.stdout.readline()
                    if not output:
                        break
                    error.value += output.decode()
                    page.update()

                # Get final status
                stdout, stderr = await process.communicate()
                if process.returncode == 0:
                    error.value = f'Success: {stdout.decode()}'
                else:
                    error.value = f'Error: {stderr.decode()}'

            except Exception as e:
                error.value = f'Exception: {str(e)}'

            finally:
                await asyncio.sleep(5)
                error.value = ''
                Installing_status.value = ''
                page.update()
        if PostgreSQL_value:
            Installing_status.value = 'installing PostgreSQL...'
            page.update()

            cmd = (
                f'ansible-playbook ./assets/ansible/postgre.yml '
                f'--user={username.value} '
                f'-c ssh '
                f'-i "{hostname.value}," '
                f'--private-key={keypath.value} '
                # f'-e "ansible_port={portno.value}" ' # uncomment here if port
                # needed
                f'-e "ansible_python_interpreter=/usr/bin/python3" -v'
            )

            try:
                process = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                # Real-time output
                while True:
                    output = await process.stdout.readline()
                    if not output:
                        break
                    error.value += output.decode()
                    page.update()

                # Get final status
                stdout, stderr = await process.communicate()
                if process.returncode == 0:
                    error.value = f'Success: {stdout.decode()}'
                else:
                    error.value = f'Error: {stderr.decode()}'

            except Exception as e:
                error.value = f'Exception: {str(e)}'

            finally:
                await asyncio.sleep(5)
                error.value = ''
                Installing_status.value = ''
                page.update()
        if Node_value:
            Installing_status.value = 'installing Node...'
            page.update()

            cmd = (
                f'ansible-playbook ./assets/ansible/node.yml '
                f'--user={username.value} '
                f'-c ssh '
                f'-i "{hostname.value}," '
                f'--private-key={keypath.value} '
                # f'-e "ansible_port={portno.value}" ' # uncomment here if port
                # needed
                f'-e "ansible_python_interpreter=/usr/bin/python3" -v'
            )

            try:
                process = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                # Real-time output
                while True:
                    output = await process.stdout.readline()
                    if not output:
                        break
                    error.value += output.decode()
                    page.update()

                # Get final status
                stdout, stderr = await process.communicate()
                if process.returncode == 0:
                    error.value = f'Success: {stdout.decode()}'
                else:
                    error.value = f'Error: {stderr.decode()}'

            except Exception as e:
                error.value = f'Exception: {str(e)}'

            finally:
                await asyncio.sleep(5)
                error.value = ''
                Installing_status.value = ''
                page.update()
        if Mongodb_value:
            Installing_status.value = 'installing MongoDB...'
            page.update()

            cmd = (
                f'ansible-playbook ./assets/ansible/mongo.yml '
                f'--user={username.value} '
                f'-c ssh '
                f'-i "{hostname.value}," '
                f'--private-key={keypath.value} '
                # f'-e "ansible_port={portno.value}" ' # uncomment here if port
                # needed
                f'-e "ansible_python_interpreter=/usr/bin/python3" -v'
            )

            try:
                process = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                # Real-time output
                while True:
                    output = await process.stdout.readline()
                    if not output:
                        break
                    error.value += output.decode()
                    page.update()

                # Get final status
                stdout, stderr = await process.communicate()
                if process.returncode == 0:
                    error.value = f'Success: {stdout.decode()}'
                else:
                    error.value = f'Error: {stderr.decode()}'

            except Exception as e:  # noqa: F841
                error.value = f'Exception: {str(e)}'

            finally:
                await asyncio.sleep(5)
                error.value = ''
                Installing_status.value = ''
                page.update()

    respone = ft.Text()
    dd = ft.DropdownM2(
        width=350,
        border_color='white12',
        alignment=ft.alignment.center,
        options=hosts_boxes(hdl)
    )

    hosts_select = ft.Column(
        controls=[
            dd,
            respone
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )

    install_button = ft.Container(
        content=ft.ElevatedButton(
            text='Install',
            height=35, width=95,
            icon=ft.Icons.INSTALL_DESKTOP,
            icon_color='white',
            color='white',
            bgcolor='transparent',
            on_click=ans_ins),
        height=40, width=100,
        gradient=ft.LinearGradient(colors=[black, secondary_bg]),
        border_radius=20
    )

    main_screen = ft.Container(
        content=ft.Column(
            height=900,
            width=1000,
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.SETTINGS,
                                color=light_orange,
                            ),
                            ft.Text(
                                value="Welcome to ansible assistant",
                                size=20,
                                color=bg_white,
                                weight=ft.FontWeight.W_900,
                            )
                        ], alignment='center'
                    ),
                    padding=ft.padding.all(15),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=hosts_select,
                    border_radius=15,
                    gradient=ft.LinearGradient(
                        colors=[black, secondary_bg]
                    ),
                    height=200,
                    width=450,
                    alignment=ft.alignment.center
                ),
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            label="Docker",
                            height=35, width=75,
                            fill_color='white12',
                            hover_color='#55216df2',
                            check_color='#216df2'
                        ), ft.Checkbox(
                            label="PostgreSQL",
                            height=35, width=105,
                            fill_color='white12',
                            hover_color='#55008bb9',
                            active_color=light_orange,
                            check_color='#008bb9'
                        ), ft.Checkbox(
                            label="Node",
                            height=35, width=60,
                            fill_color='white12',
                            hover_color='#5531b263',
                            active_color=light_orange,
                            check_color='#31b263'
                        ), ft.Checkbox(
                            label="Mongodb",
                            height=35, width=55,
                            fill_color='white12',
                            hover_color='#55119f1f',
                            active_color=light_orange,
                            check_color='#119f1f'
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                install_button,
                monitor_container,
                ft.Container(height=40),
                Installing_status
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ), alignment=ft.alignment.center
    )

    page.update()
    page.add(main_screen)


ft.app(target=main, assets_dir="assets")
