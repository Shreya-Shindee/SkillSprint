# Database Utility Runner for SkillSprint
# This PowerShell script makes it easier to run the database utility

function Show-Help {
    Write-Host "SkillSprint Database Utility" -ForegroundColor Cyan
    Write-Host "===========================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage: .\db.ps1 [command] [options]" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Commands:" -ForegroundColor White
    Write-Host "  reset      Reset the database (clear all data)"
    Write-Host "  seed       Seed the database with sample data"
    Write-Host "  check      Check database structure"
    Write-Host "  all        Perform all operations (reset, seed, check)"
    Write-Host ""
    Write-Host "Options:" -ForegroundColor White
    Write-Host "  -fast      Use faster methods (skip some checks)"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor White
    Write-Host "  .\db.ps1 all                Perform all operations"
    Write-Host "  .\db.ps1 reset seed         Reset and seed the database"
    Write-Host "  .\db.ps1 all -fast          Perform all operations in fast mode"
}

# Show help if no parameters provided
if ($args.Count -eq 0) {
    Show-Help
    exit 0
}

$cmd = "python db_utils.py"
$argsList = @()

# Parse arguments
foreach ($arg in $args) {
    switch -regex ($arg) {
        "reset" { $argsList += "--reset" }
        "seed" { $argsList += "--seed" }
        "check" { $argsList += "--check" }
        "all" { $argsList += "--reset"; $argsList += "--seed"; $argsList += "--check" }
        "-fast" { $argsList += "--fast" }
        default { 
            Write-Host "Unknown option: $arg" -ForegroundColor Red
            Show-Help
            exit 1
        }
    }
}

# Build the command
$fullCmd = "$cmd $($argsList -join ' ')"

# Execute the command
Write-Host "Running: $fullCmd" -ForegroundColor Cyan
Invoke-Expression $fullCmd
