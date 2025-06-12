param([string]$Target = "build")

# Temporarily allow script execution
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Run the build script
.\build.ps1 -Target $Target