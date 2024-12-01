[Code]
procedure InitializeSetup;
begin
  MsgBox('İletişim: hibrahim54@cakirhalil.com', mbInformation, MB_OK);
end;

[Setup]
AppName=Auto Clicker
AppVersion=1.0
DefaultDirName={pf}\cakirhalil\AutoClicker
DefaultGroupName=AutoClicker
OutputBaseFilename=cakirhalil-AutoClicker-1.0-setup.exe
Compression=lzma
SolidCompression=yes
SetupIconFile=D:\masaustu\halil\auto-click\image\AutoClicker.ico
LicenseFile="D:\masaustu\halil\auto-click\build\LICENSE.txt"



[Files]
Source: "‪D:\masaustu\halil\auto-click\build\build-app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\AutoClicker"; Filename: "{app}\build-app.exe"; IconFilename: "D:\masaustu\halil\auto-click\image\AutoClicker.ico"
Name: "\AutoClicker"; Filename: "{app}\build-app.exe"; IconFilename: "D:\masaustu\halil\auto-click\image\AutoClicker.ico"

[UninstallDelete]
Type: files; Name: "{app}\*.*"
