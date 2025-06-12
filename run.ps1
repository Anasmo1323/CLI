param([string]$Target = "build")
$env:PYTHONPATH = "D:\CLI_module"
pytest tests/
# Temporarily allow script execution
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Run the build script
.\build.ps1 -Target $Target