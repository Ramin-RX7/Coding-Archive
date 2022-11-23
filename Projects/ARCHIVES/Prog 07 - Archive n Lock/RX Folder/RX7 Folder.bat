:End
color 2
cls
@echo off
title RX Locker
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST Ramin.RX goto MDLOCKER
:CONFIRM
color 0a
echo Do you want to lock this folder ? (Y/N)
set/p "cho=>"
if %cho%==Y goto LOCK
if %cho%==y goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Invalid Command !!
goto CONFIRM
:LOCK
ren Ramin.RX "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Folder Locked Successfully !
goto End
:UNLOCK
color c
echo Enter Password to Unlock Folder   (CH BD)
set/p "pass=>"
if NOT %pass%==06072004 goto error
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Ramin.RX
echo Folder Unlocked Successfully
goto End
:error
color 0c
echo Error, Wrong Password !
goto end
:MDLOCKER
color 0a
md Ramin.RX
echo RX Folder created !
goto End
