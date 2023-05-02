import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "BanderoGooseGame",
    options = {"build_exe": {"packages":["pygame", "random", "os", "PIL"],
                           "include_files":["background.png", "bonus.png", "enemy.png", "player.png", "Goose"]}},
    executables = executables

    )