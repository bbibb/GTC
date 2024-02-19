# Configuring Windows Server 2019


## Working with Server Manager


**Adding Roles and Features Using Server Manager**
navigation area - sections for servers
	section section has 4 panes
		events, services (start and stop), best practices analyzer (scan), performance
dashboard section at the top = common tasks, state
	contains welcome area for configuring local, adding roles and features
manage menu - add role, features, servers, groups
	role and server groups pane - green arrow for fully managed by SM

Storage Spaces
Other tools have MMC snap-in via Tools menu
	also right-click on a server to start relevant tools for that server

Remote Server Administration Tool RSAT on Win10 - remote admin with MMC tools

3 ways to add roles and features:
	add roles and features in Welcome to SM pane
	select Add Roles and Features from Manage Menu
	select Add Roles and Features from Tasks menu in a server pane

access post install tasks with yellow warning icon in notification area

**Using the BPA to Verify Server Roles**
best practices analyzer scan
	information - recommendation
	warning - ok for now but risky
	error - problems expected

categories
	configuration
	predeployment - prereqs
	postdeployment - services started
	performance
	BPA prereqs - can BPA analyze the role?

## Working with the Windows Admin Center
remote management


**Installing the Windows Admin Center**
WindowsAdminCenter--version--.msi

cannot be installed on a server that is the AD Domain Services role as a domain controller

when in Server 2016 or 2019 gateway server mode - manage other servers through it
when in Win10 - works like RSAT, connects to domain

trusted host settings
self-signed certificate or one signed by Certificate Authority

**Using Windows Admin Center**

valid credentials for gateway server or AD domain
add servers with Add
Edit, custom tags
Connect

similar to server manager
performance,  configuration, firewall, services and roles, status, 
restart, shutdown, edit domain
tools
	certificates
	containers
	devices
	DHCP
	events
	files
	firewall
	installed apps
	Local users and groups
	network
	processes
	registry
	roles and features
	scheduled tasks
	services
	storage
	storage replica
	system insights
	updates
	VM - monitor and manage VM
	virtual switches 

tools
	powershell on target system
	RDP
	Azure hybrid services - registration in cloud
	Azure file sync
	backup
	Storage Migration Service - servers migrated to cloud
## Configuring Server Hardware Devices

Storage devices
Disk controllers
Network adapters
input devices
specialized

Plug and Play PnP
	may need to configure or download latest driver
	may need to restart
	
**Adding Hardware Using Control Panel**
Devices and Printers utility
	force PnP
	install non PnP
	troubleshoot

Control panel ->category view
Add a Device under Hardware
View devices and printers
Right click -> Troubleshoot

**Using Device Manager**
Device Manager Utility
	Control Panel -> Hardware -> Device Manager
	update, disable, uninstall, scan for changes, properties

uninstall Generic then use mfg disk to install driver, reboot

IRQ Interrupt Request
Input/Output address
resource conflicts - uninstall, reboot, reinstall

4 tabs
	General - functioning?
	Driver
	Details - properties
	Events

## Verifying System Files

files may require a signature

System File Checker - scan for integrity, replace damaged with proper
		CMD - sfc/scannow
			sfc/scanfile:filename

File Signature Verification Tool Sigverif
	system files have a signature? 
	scans, does not fix
	log - sigverif.txt

## Configuring Windows Settings


**Configuring Performance Options**
- processor scheduling and data execution prevention
- virtual memory
- file cashing and flushing

*Configuring Processor Scheduling and Data Execution Prevention*
processor scheduling - how resources are allocated to programs
Control Panel -> System and Security-> System -> Advanced -> Performance -> Settings - Advanced
	adjust for best performance of Programs or Background Services

Data Execution Prevention DEP
	memory problems caused by malware invading system memory spaces
	exclude certain programs for performance, eg dynamic code generation apps
Same panel with Performance Settings

*Configuring Virtual Memory*
Disk storage to expand physical memory
paging, pages moved from physical to virtual memory
	in blocks of 4KB

Area of disk is "paging file"
	must be on the HD or SSD that has the OS (c:\)
	create paging file on each disk connected to the system
	not on a RAID volume
initial size - RAM x 1.5
maximum size - RAM x 2

same panel with Processor Scheduling
	Virtual Memory -> Change -> deselect Automatic->Set

*Configuring File Caching*
on by default
cache file data for reading or writing
after written, cached data is removed "flushing"

may turn off caching and flushing to enable drive hot-swap. If off:
	slows down file operations when pushed
	less memory used for file operations
	may be data loss with hot-swapping drive

Device Manager-> Disk -> Properties -> Policies - Enable Write caching

**Configuring Environment Variables**
where to find certain programs and info
2 categories:
	system Environment variables
		defined by OS, all users
	User Environment Variables
		per user basis
		override conflicting system env variables

Control Panel -> System and Security -> System -> Advanced -> Env Variables
	create, edit, delete system and user env

*Configuring Startup and Recovery*
Which OS to boot
how long to display list
how long to display recovery options

writing to system log
whether to start automatically after failure
how and where to write debugging info

Control Panel -> System and Security -> System -> Advanced -> Startup and Recovery -> settings
	Startup and Recovery window



**Configuring Power Options**
Select a Power Plan
choose what power button does
create a power plan
choose when to turn off display

Control Panel -> Hardware -> Power Options

3 power plans
	- balanced
	- power saver
	- high performance



## The Windows Registry

Database - hardware and software info
if corrupt, system may fail
	hardware components
	WS2019 services
	user profiles
	settings used to boot
	all software
	licensing
	SM and CP configurations

Registry Editor
	regedit

export to backup before modifying

**Windows Registry Contents**

key - folder on left pane - subkeys and entries
subkey - can contain entries or other subkeys
entry - item at lowest level - name, data type, value
	data parameter

5 root keys (aka subtree) - highest level of data
	HKEY_LOCAL_MACHINE
	HKEY_CURRENT_USER
	HKEY_USERS
	HKEY_CLASSES_ROOT
	HKEY_CURRENT_CONFIG

*HKEY_LOCAL_MACHINE*
hardware components
drivers
IRQ
VIOS

set of subkeys = "hive"
eg, SOFTWARE, HARDWARE, SECURITY, SYSTEM, SAM

*HKEY_CURRENT_USER*
desktop config for user currently logged in
display, keyboard, clock, env, path, sounds


*HKEY_USERS*
each user who has signed in
each profile listed under this root key


*HKEY_CLASSES_ROOT*
associated file extensions
	exe, text, graphics, clipboard, audio, etc
	

*HKEY_CURRENT_CONFIG*
current hardware profils
	monitor type, keyboard, mouse, 
	default profile plus others perhaps for docking vs undocked


## Using Windows PowerShell


**Working with Windows PowerShell**
PS C:\\Users\\Administrator>

right click icon-> more-> run as administrator

windows commands:
	copy
	\>\> output redirection
	; command chaining
	
	PS c:\Users\Adminstrator>ipconfig >> C:\IPconfig.txt ; cls

cmdlets
	action-object structure
		Get-Host
		Get-Process
		Set-Date
		Write-Error

see a list of all cmdlets

	PS C:\Users\Adminstrator>Get-Command | more
	
| pipe sends output of command to another command
piping

list all processes

	PS C:\Users\Administrator>Get-Process | more

	PS C:\Users\Administrator>help Get-Process
	PS C:\Users\Administrator>help Get-Process -full
	PS C:\Users\Administrator>help Get-Process -online
	
Other options
	\-whatif
	\-confirm
	\-verbose
	\-debug
	\-erroraction

search for right cmdlet

	PS C:\Users\Administrator>Get-Command -verb set*
	PS C:\Users\Administrator>Get-Command -noun mem*
	PS C:\Users\Administrator>Get-Command -syntax Get-Process

keys:
	up and down arrows command history
	home-end of CL
	q - quits interactive command
	tab - autocomplete

*Customizing Windows PowerShell Sessions*

powershell command
powershell -nologo
powershell -command "& {Get-Process}"
	starts temp shell, runs command, and quits

Powershell console file - .psc1
	for setting properties
	create one from current session with "export-console CustomPowerShell.psc1"


*Aliases and Functions*
shortcuts
view aliases with "Get-Alias"
	dir -> Get-ChildItem
	cd-> Set-Location

make one with "Set-Alias lala Get-Process"

also functions:
	function c {Write-Host "About to clear screen"; Start-Sleep -s 2; Clear-Host}


*PowerShell Profile Scripts*
aliases and functions die when session is over
can save them in profile script to load with new session
	Microsoft.Powershell_profile.ps1 in Documents folder

profile.ps1 a script that runs automatically when PS session starts
	not Powershell console files (psc1) are shortcuts to customized session

enable script execution
	Set-ExecutionPolicy unrestricted
	create profile:
		New-Item -path $profile -itemtype file -force
	edit profile:
		notepad $profile


*Modifying Command Output*
Get-ChildItem (gci) info about objects
	pipe to Format-Table or Out-GridView (ogv)
	-recurse option
	Sort-Object alias to sort results
	Group-Object alias to output with groups
	ConvertTo-HTML
	Export-CSV
	
	PS c:\Users\Administrator>Get-Process | ogv



*PowerShell Objects*
attributes and methods
	Get-Member (gm) to view attributes and methods of an object
	create object with a pipe, or by enclosing command in parentheses
or 

	PS C:\Users\Administrator>$a = new-object -comobject "wscsript.shell"
	an object with reference to wscript.shell object in the COM

	then
		$a | gm | more

attributes
	$a.expandenvironmentstrings
methods
	$a.run("calc.exe")

eg, .LastWriteTime attribute to debug


*PowerShell Providers*
plugins
	Get-PSProvider
	Set-Location to set which provider you're using

- filesystem provider - default

- variable provider
	Get-Variable
	New-Variable
	Set-Variable
	Remove-Variable

- environment provider
	Get_Child_Item
	New-Item
	Rename-Item
	Remove-Item

- alias provider

- function provider

- certificate provider

- registry provider
	view and modify registry keys

**System Administration Commands**

Restart-Computer
Stop-Computer
Rename-Computer newcomputername
Add-Computer -DomainName domainname -to join AD domain
Get-WindowsFeature | ogv will display installed
Remove-WindowsFeature web-server

Test-NetConnection
	optional host name and port

Get-NetIPConfiguration
Get-NetAdapter
Get-NetAdapterStatistics

New-NetIPAddress - InterfaceAlias Ethernet -IPAddress 'ip' -PrefixLength 24 -DefaultGateway 'ip'

Set-DNSClientServerAddress

Set-NetFirewallProfile
New-NetFirewallRule

Set-Service dnscache -StartupType Automatic

Stop-Process

remote with winRM component
	start, stop, and configure remote server

**Using WMI within Windows PowerShell**
Windows Management Instrumentation WMI
	programs can query hardware and software on the computer
	WMI consumers
	WMI infrastructure

WMI namespaces
	different providers
	CIMv2 is the one you want

WMI providers
	each has different classes

WMI classes 
	individual data types
	use with PS 

Get-WmiObject - list

**Creating PowerShell Scripts**
test files with .ps1 extension

windows commands and PS cmdlets


*Executing PowerShell Scripts*

Set-ExecutionPolicy unrestricted

Restricted - no scripts
AllSigned
RemoteSigned - downloaded only if they are signed
Unrestricted - all scripts, but prompts you if downloaded
Bypass - runs all with no warnings
Undefined no policy set

use full path or forced relative (./)

powershell command in CMD

*Using Windows PowerShell ISE*

Integrated Scripting Environment
Powershell pane, script pane, commands pane on the right

create and test on remote with winRM started within ISE

*Variables and Constants*
$
not case sensitive
avoid special characters and keywords

type $host -> displays computer information

Set-Variable
$variablename = value

array variable $variablename = value1, value2, value3

Set-Variable -option constant
	-option readonly

typecast - change from string type
	[int]$variablename = value

get user input:
	$answer = Read-Host

*Protecting PowerShell Metacharacters*

$
"" treats all as single unit
' ' 
\` back-quote escapes the next character


*Coloring and Formatting Output*

Write-Host -foregroundcolor color -backgroundcolor color
-separator character
-escape characters
	\`n newline
	\`t tab

*Decision Constructs*

conditional expressions

compare data
-eq equal
-ne not equal
-lt less than
-gt greater than
-ge greater or equal
-le less or equal
-ceq equal to (case-sensitive)
-ieq equal to (case-insensitive)

-and
-or
-not
! not

if
elseif
else

switch
	value 1 {}
	value2 {}

*Loop Constructs*
foreach
	foreach ($item in $collection) {}
for
	for ($counter; $condition ; $increment) {}
while
	while () {}
do...while
	do {}
		while ()
do...until
	do{}
		until ()

*Creating Your Own PowerShell Scripts*

\#
\#This script prints process information to the screen for a process 
\#that prompted to supply during script execution  
\#  
\$ans=Read-Host "What process would you like to query?" 
Get-WmiObject win32_process -Filter "name= '$ans'" |  
Format-Table HandleCount, VirtualSize, UserModeTime, KernelModeTime,  ProcessID, Name


*Finding PowerShell Scripts on the Internet*

understand scripts = *tracing*

sites such as powershellscripts.com
Google search

## Review


Server manager can be used to monitor and manage Windows Server 2008 and later
	TRUE

Which of these panes are in Server Manager
	ALL 4
		Services
		Events
		Roles and Features
		Performance

Which of these tools in navigation pane of Windows Admin Center performs capacity planning
	System Insights

The Windows Admin Center allows you to get a PS session in the browser
	TRUE

Which utility can be used to manually install a new device that isn't PnP
	Devices and Printers Utiility

What can increase the performance of a system with 3 storage devices
	Create a paging file on the 2nd and 3rd devices and remove page file from first storage

Sigverif tool used to verify and repair corrupt files
	FALSE (File System Checker repairs)

Which feature configured in Control Panel?
	ALL 4
		File caching and flushing
		environment variables
		power options
		startup and recovery options

Some software issues require you to modify registry value
	TRUE

What should be your first course of action when you see a device marked Unknown in Device manager?
	Install MFG driver and reboot

System Env variables apply to any user logged in?
	TRUE

What executes in PS to learn about syntax of Get-WMIObject?
	ALL4
		help Get-WMIObject
		Get-Help Get-WMIObject
		get-help Get-WmiObject
		Get-Help Get-WMIObject -online


Powershell console files use the ps1 extension
	FALSE (psc1)

PS alias to switch to a different provider
	sl (Set-Location)

Test-NetConnection to test network connectivity to a target computer
	TRUE

Which opens windows PS prompt connected to a remote computer
	Enter-PSSession computername

Valid methods for executing ps1 file
	3 of 4
		c:\\Scripts\\superscript.ps1
		.\\superscript.ps1
		.\/superscript.ps1

		not superscript.ps1 (relative path has to be forced with .)

In this example, 3 loops will be executed?
	$args = 1,2,3,4
	foreach ($i in $args)
		FALSE - 4 loops

PS constructs to use to perform action based on value of a single variable
	switch

Tab key can be used to autocomplete a PS cmdlet as you type
	TRUE

