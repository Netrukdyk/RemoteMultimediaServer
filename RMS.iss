; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{13AB3480-695C-4D19-B1EF-0B7E4CEA8F35}
AppName=Remote Multimedia Server
AppVersion=1.0
;AppVerName=Remote Multimedia Server 1.0
AppPublisher=Inotecha, UAB
AppPublisherURL=http://www.inotecha.lt/rms
AppSupportURL=http://www.inotecha.lt/rms
AppUpdatesURL=http://www.inotecha.lt/rms
DefaultDirName={pf}\Remote Multimedia Server
DefaultGroupName=Remote Multimedia Server
DisableProgramGroupPage=yes
OutputDir=D:\Desktop
OutputBaseFilename=setup
SetupIconFile=C:\Python34\RemoteMultimediaServer\dist\icon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Python34\RemoteMultimediaServer\dist\remote.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Python34\RemoteMultimediaServer\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Remote Multimedia Server"; Filename: "{app}\remote.exe"
Name: "{commondesktop}\Remote Multimedia Server"; Filename: "{app}\remote.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\remote.exe"; Description: "{cm:LaunchProgram,Remote Multimedia Server}"; Flags: nowait postinstall skipifsilent

