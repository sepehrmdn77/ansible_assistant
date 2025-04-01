from flet import *
import subprocess
from time import sleep
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


def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = '#232323'
    page.title = 'Ansible Assistant'
    page.window.width = 480
    page.window.height = 750
    page.theme = Theme(
        color_scheme_seed=Colors.BLUE,
    )

    def hosts_boxes(list):  # in this function for each item in hdl we will have a check box
        i = 0
        result = []
        for item in list:
            result.append(
                dropdownm2.Option(
                    data=hdl[i],
                    text=hdl[i]['Host'],
                    on_click=button_clicked,
                    alignment=alignment.center))
            i += 1
        return result

    Installing_status = Text()

    hostname = Text(value='')
    username = Text(value='')
    keypath = Text(value='')
    portno = Text(value='')

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

    error = TextField(
        '',
        color=bg_white,
        text_size=12,
        border_color='transparent',
        max_lines=100,
        read_only=True)
    monitor = Column(controls=[error], scroll='auto')
    monitor_container = Column(controls=[Container(
        content=Container(
            content=monitor,
            margin=0,
            padding=5,
            alignment=alignment.center,
            gradient=RadialGradient(colors=[black, secondary_bg], radius=1.5),
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

            except Exception as e:
                error.value = f'Exception: {str(e)}'

            finally:
                await asyncio.sleep(5)
                error.value = ''
                Installing_status.value = ''
                page.update()

    respone = Text()
    dd = DropdownM2(
        width=350,
        border_color='white12',
        alignment=alignment.center,
        options=hosts_boxes(hdl)
    )

    hosts_select = Column(
        controls=[
            dd,
            respone
        ], horizontal_alignment=CrossAxisAlignment.CENTER,
        alignment=MainAxisAlignment.CENTER
    )

    install_button = Container(
        content=ElevatedButton(
            text='Install',
            height=35, width=95,
            icon=Icons.INSTALL_DESKTOP,
            icon_color='white',
            color='white',
            bgcolor='transparent',
            on_click=ans_ins),
        height=40, width=100,
        gradient=LinearGradient(colors=[black, secondary_bg]),
        border_radius=20
    )

    test_btn = ElevatedButton(
        text='test', on_click=lambda _: print([hostname, username, keypath]))

    main_screen = Container(
        content=Column(
            height=900,
            width=1000,
            controls=[
                Container(
                    content=Row(
                        controls=[
                            Icon(
                                Icons.SETTINGS,
                                color=light_orange,
                            ),
                            Text(
                                value="Welcome to ansible assistant",
                                size=20,
                                color=bg_white,
                                weight=FontWeight.W_900,
                            )
                        ], alignment='center'
                    ),
                    padding=padding.all(15),
                    alignment=alignment.center
                ),
                Container(
                    content=hosts_select,
                    border_radius=15,
                    gradient=LinearGradient(
                        colors=[black, secondary_bg]
                    ),
                    height=200,
                    width=450,
                    alignment=alignment.center
                ),
                Row(
                    controls=[
                        Checkbox(
                            label="Docker",
                            height=35, width=75,
                            fill_color='white12',
                            hover_color='#55216df2',
                            check_color='#216df2'
                        ), Checkbox(
                            label="PostgreSQL",
                            height=35, width=105,
                            fill_color='white12',
                            hover_color='#55008bb9',
                            active_color=light_orange,
                            check_color='#008bb9'
                        ), Checkbox(
                            label="Node",
                            height=35, width=60,
                            fill_color='white12',
                            hover_color='#5531b263',
                            active_color=light_orange,
                            check_color='#31b263'
                        ), Checkbox(
                            label="Mongodb",
                            height=35, width=55,
                            fill_color='white12',
                            hover_color='#55119f1f',
                            active_color=light_orange,
                            check_color='#119f1f'
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                install_button,
                monitor_container,
                Container(height=40),
                Installing_status
            ], horizontal_alignment=CrossAxisAlignment.CENTER
        ), alignment=alignment.center
    )

    page.update()
    page.add(main_screen)


app(target=main, assets_dir="assets")
