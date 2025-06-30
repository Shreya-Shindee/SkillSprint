@echo off
REM Database Utility Runner for SkillSprint
REM This batch file makes it easier to run the database utility

echo SkillSprint Database Utility
echo ===========================

if "%1"=="" (
    echo Usage: db [command] [options]
    echo.
    echo Commands:
    echo   reset      Reset the database (clear all data)
    echo   seed       Seed the database with sample data
    echo   check      Check database structure
    echo   all        Perform all operations (reset, seed, check)
    echo.
    echo Options:
    echo   --fast     Use faster methods (skip some checks)
    echo.
    echo Examples:
    echo   db all                Perform all operations
    echo   db reset seed         Reset and seed the database
    echo   db all --fast         Perform all operations in fast mode
    exit /b 0
)

set CMD=python db_utils.py
set ARGS=

:parse
if "%1"=="" goto execute

if "%1"=="reset" (
    set ARGS=%ARGS% --reset
    shift
    goto parse
)

if "%1"=="seed" (
    set ARGS=%ARGS% --seed
    shift
    goto parse
)

if "%1"=="check" (
    set ARGS=%ARGS% --check
    shift
    goto parse
)

if "%1"=="all" (
    set ARGS=%ARGS% --reset --seed --check
    shift
    goto parse
)

if "%1"=="--fast" (
    set ARGS=%ARGS% --fast
    shift
    goto parse
)

echo Unknown option: %1
exit /b 1

:execute
echo Running: %CMD%%ARGS%
%CMD%%ARGS%
