# 特别注意包含这些路径（基于 xmir_base/__init__.py）
added_files = [
    ('xmir_base', 'xmir_base'),
    ('firmware', 'firmware'),
    ('*.py', '.'),  # 包含根目录所有py文件
]

from PyInstaller.utils.hooks import collect_submodules

a = Analysis(
    ['menu.py'],
    pathex=['.'],
    datas=added_files,
    hiddenimports=collect_submodules('ssh2') + [
        'xmir_base',
        'gateway',
        'xqmodel'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='xmir_patcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='app.ico',
    onefile=True
)
