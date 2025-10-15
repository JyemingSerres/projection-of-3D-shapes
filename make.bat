:: Easily configure pyInstaller options to package the project into an executable
@ECHO OFF


:: Name of the output executable file
SET execname=Projection-of-3D-shapes

:: Main script path
SET mainscript=./src/main.py

:: Where the executable is stored
SET distpath=./dist

:: Where temporary files are stored
SET workpath=./build


:: call pyInstaller
pyInstaller %mainscript% --name %execname% --onefile --noconsole --distpath %distpath% --workpath %workpath% --specpath %workpath%
ECHO.
IF %ERRORLEVEL% NEQ 0 (
    ECHO pyInstaller failed to package the project.
) ELSE (
    ECHO Executable packaged successfully!
)
