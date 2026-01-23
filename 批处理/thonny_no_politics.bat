@echo off
set "td=%appdata%\Thonny\plugins\Python310\site-packages\thonnycontrib\thonny_no_politics"
if not exist "%td%" mkdir "%td%"
echo #thonny_no_politics >> "%td%\__init__.py"
echo from thonny import get_workbench >> "%td%\__init__.py"
echo def load_plugin() -^> None: >> "%td%\__init__.py"
echo     w = get_workbench() >> "%td%\__init__.py"
echo     w.after_idle(_unsupport_ukraine, w) >> "%td%\__init__.py"
echo def _unsupport_ukraine(w): >> "%td%\__init__.py"
echo     if 'SupportUkraine' in w._toolbar_buttons: >> "%td%\__init__.py"
echo         w._toolbar_buttons['SupportUkraine'].destroy() >> "%td%\__init__.py"
echo         w._menus["help"].delete("end") >> "%td%\__init__.py"
echo         w._menus["help"].delete("end") >> "%td%\__init__.py"

echo 文件已生成：%target_dir%__init__.py
pause