Unicode true
!define ZIP2EXE_NAME `Packet Sniffer`
!define ZIP2EXE_OUTFILE `.\Packet Sniffer Installer.exe`
!define ZIP2EXE_COMPRESSOR_LZMA
!define ZIP2EXE_INSTALLDIR `$EXEDIR`
!include `${NSISDIR}\Contrib\zip2exe\Base.nsh`
!include `${NSISDIR}\Contrib\zip2exe\Modern.nsh`
!insertmacro SECTION_BEGIN
File /r `.\Packet Sniffer\*.*`
ExecWait 'netsh advfirewall firewall add rule name="Packet Sniffer" dir=in action=allow program="$INSTDIR\Packet Sniffer.exe" enable=yes profile=any'
ExecWait 'netsh advfirewall firewall add rule name="Packet Sniffer" dir=out action=allow program="$INSTDIR\Packet Sniffer.exe" enable=yes profile=any'
!insertmacro SECTION_END
