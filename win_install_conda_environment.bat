@echo off
set CONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
set CONDA_INSTALLER=Miniconda-installer.exe
set ENVIRONMENT_YML=environment.yml
set ENV_NAME=doe_sample

echo Installing Miniconda...
curl -o %CONDA_INSTALLER% %CONDA_URL%
if %errorlevel% neq 0 (
    echo Failed to download Miniconda installer from %CONDA_URL%
    exit /b 1
)

start /wait %CONDA_INSTALLER% /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S
del %CONDA_INSTALLER%

echo Creating conda environment from %ENVIRONMENT_YML%...
call conda env create -f %ENVIRONMENT_YML% -n %ENV_NAME%
if %errorlevel% neq 0 (
    echo Failed to create conda environment from %ENVIRONMENT_YML%
    exit /b 1
)

echo.
echo Installation completed successfully.
echo Use 'conda activate %ENV_NAME%' to activate the environment.
echo.
