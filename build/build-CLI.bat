set pathtospec="../src/cli/superscript.spec"
set pathtodist="../dist/"
set pathtowork="temp/"

pyinstaller --onefile --clean --distpath %pathtodist% --workpath %pathtowork% %pathtospec%