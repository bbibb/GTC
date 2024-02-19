
## Implementing Hyper-V

**Installing Hyper-V**
IntelVT or AMD-V processor virtualization extensions

select Hyper-V role in Server Manager

select network interface
	creates external virtual switch

enable live migration of virtual machines
	copy a running vm from one server to another in same AD domain
		started there and stopped at origin

Credential Security Support Provider CredSSP
	authentication for starting live migration process
	Kerberos is default authentication protocol in AD

select location for files
	one or more virtual hard disks
	vm configuration files

also can install Hyper-V in PS
	Install-WindowsFeatures -Name Hyper-V ...



**Understanding Virtual Networks**
virtual networks used by VMs and the host
	each virtual network is a "virtual switch"
	same function as a physical switch

3 types of virtual switches
- external - underlying physical switch - connects VMs to a physical network
- internal - virtual network for VMs and host
- private - only for VMs to communicate

isolated networks for communication
	cluster configuration
	security
	N-tier security - must go through web app to access database server

Virtual Switch Manager in Actions pane of Hyper-V manager
	for external, select physical adapter, and check "allow management OS to share this network adapter"
		single-root I/O virtualization SR-IOV
			network interface works with Hyper-V to separate network requests from VMs

Physical switches can be partitioned in to VLANs
	select "Enable virtual LAN identification for management OS" for each virtual switch, and enter VLAN number for ethernet port

vEthernet
	properties to set IP config
	the Ethernet switch must be set to Hyper-V Extensible Virtual Switch protocol
		allows Hyper-V to use that physical interface to share with multiple VMs


**Creating Virtual Machines**
New from Actions pane -> VM -> New Virtual Machine Wizard

select location

Choose Generation
Gen 1
	- Win7 and later (32 and 64)
	- WS 2008 and later (64)
	- RHEL5 and later
	- Debian 7 and later
	- Ubuntu 12 and later
	- FreeDBS 8.4 and later
Gen 2 (64-bit)
	- Win8 and later
	- WS 2012 and later
	- RHEL 6
	- Debian 8
	- Ubuntu 14
	- FreeBSD 9.1

Gen 1 emulates:
	- IDE hd
	- IDE CDROM
	- SCSI
	- Floppy
	- BIOS
	- Legacy network adapter 
		- Preboot Execution Environment PXE
	- PS/2 keyboard and mouse
	- s3 video card
	- older serial COM and other IO

Gen2
	- UEFI
	- SAS scsi
	- VMBus network adapter net boot with PXE
	- software-based keyboard, mouse, video
	- no legacy COM

dynamic memory
	not with nested

dynamically expanding virtual HD
	127GB by default
	.vhdx extension

installation media
or network

PS
New-VM -Generation 2 - Name name -Path path -MemoryStartupBytes no -VDHPath path...



**Configuring Virtual Machines**
start in actions pane

*Generation 2*
hardware
	add hardware node, additional disks and interfaces
	firmware - boot order, security settings TPM, Shielding (bitLocker encryption of vHD)
memory
	enable dynamic memory - min, max, buffer percentage
processors
	Virtual Machine reserve percentage - minimum and maximum
	compatibility - enable live migration
	NUMA - non-uniform memory access - faster memory sharing
storage
	Serial Attaches SCSI
	New virtual hard disk
		edit, inspect, browse
	pass-through disk - physical disk that is offline can be added
	Quality of Service - min and max number of I/O operations per second IOPS
network
	associate network interface with virtual switch, enable VLAN
	Enable bandwidth management
	Options
		virtual machine queue
		IPsec task offloading
		MAC address spoofing
		DHCP guard
		Router guard
		Protected network (for clustering)
		port-mirroring
		NIC teaming
		Device naming
Management
	name
	integration services - automatic services
	checkpoints - type and location
	smart paging file location
	automatic start action - on boot
	automatic stop action - on shutdown

*Generation 1*
same except IDE and legacy SCSI
two COM ports
named pipe (connection to running process via file)
floppy
no TMP, Secure Boot, or Shielded VM

**Working with Virtual Machines**
connect in action pane
	VM connection window
	click start to boot
buttons for control-alt-del, shutdown, reset, pause

info on running VM with Hyper-V Manager
	summary
	memory
	networking
	replication

**Managing Hyper-V Features**

*Checkpoints*
snapshots
revert to previous point in time
changes after a checkpoint is made are stored in a checkpoint file (.avhdx)
Snapshots directory

if you revert, it removes the checkpoint file
if you delete a checkpoint, those changes are merged into the .vhdx file and thus made permanent

Standard checkpoints - state of running programs
Production checkpoints - no state
	default
	if "use automatic checkpoints" one is made each time VM starts
Use either VSS Volume Shadow Copy Service or File System Freeze fsfreeze


*Live Migration*
move VM to another server in the AD domain
only works if VM is in a domain

Move in Actions pane
Move Wizard
	VM HD and Config files
	or, just HD
uses lots of bandwidth
set simultaneous limit, authentication method, and protocol

*Replication*
create copy on another host, continuously updated as changes are made
	can start the replicated server if you have failure on the original
Replication Configuration node in Server section of Actions pane of Hyper-V manager




## Rapid Server Deployment

Copy a Virtual Machine Template
or perform network install with Windows Deployment Services WDS

**Using Virtual Machine Templates**
VM with a WS2019 installation that is saved to a folder
	can be imported in Hyper-V manager to create new servers

*Creating Virtual Machine Template*
Create VM with base configuration
install base roles and features
remove all unique information
	name, identifiers in registry, regional settings, license, admin password
	do this with System Preparation Tool *Sysprep* folder - *sysprep.exe*
	this shuts down the VM
		if it's booted again, you get the *OOBE Out of Box Experience* wizard to set new info
Export in Actions menu to create a template
	folder saved


*Importing a Virtual Machine Template*
Import Virtual Machine in Actions pane
	Import Virtual Machine wizard
	select folder
	create copy of the VM, location
	summary and finish

when it starts again you get the OOBE
	modify to suit needs and go ahead with new clone of original system

**Using Windows Deployment Services**
Two large Windows Imaging Format (WIM) files
	*boot.wim* boot image, bootable windows installation program
	*install.wim* OS system files

Used by WDS to deploy OS to PXE-capable devices
	boot PXE, it gets an address from DHCP, downloads boot image
	then gets the install image, and lets you install it

simultaneous on multiple machines using multicast

*Installing WDS*
WDS role in Server Manager
	Deployment Server
	Transport Server - responds to PXE requests, multicasts


*Configuring WDS*
Windows Deployment Services Tool
	tools menu in Server Manager

Configure Server
	integrate with AD domain, lets it join new machines to the domain
	choose folder
	DHCP integration

Response
	only to known clients
	require admin approval for unknown computers
	do not respond to any client computers

add boot image and install image from installation media
	choose which editions to enable

*Starting a WDS Installation*

allow WDS to respond
make sure network interface is at top of boot order for client machine
make sure DHCP is configured properly
Enter to start
	login, select OS, select HD, install

## Review

Virtual machine settings are stored in vhdx
	FALSE

what starts Hyper-V manager
	virtmgmt.msc

which virtual switch can a host OS connect to
	internal
	external
		not private

Physical network interface is not configured with IP - Hyper-V Extensible Virtual Switch
	TRUE
Which OS supposed by Gen2 VM
	Ubuntu 14
	FreeBSD 9.1

What hardware is supported by Gen 1
	IDE HD
	SCSI HD
	Serial Ports
		NOT UEFI

Guest OS require VMBus drivers for Gen 2 VM
	TRUE

Which allows a VM to use additional physical memory
	Dynamic Memory

Both Gen1 and Gen2 use Secure Boot
	FALSE

SSD pass-through - how?
	Ensure SSD is offline in Disk Management
	In VM properties, select existing virtual HD, choose Physical HD and select the SSD

What in Actions pane to get VM Connection window
	Connect

VM checkpoints used before making important change
	TRUE

To reset VM to production checkpoint - what in the Actions pane after selecting the checkpoint in Checkpoints pane?
	Apply

Any changes to US after checkpoint are stored in .avhdx file in same directory as .vhdx?
	TRUE

Which features require that the host is part of the AD domain?
	Live Migration
	Replication

Replication must be enabled before you can copy VM to a target host?
	FALSE

To create a VM template, what actions MUSt you do?
	3
		Create New VM and install guest OS
		Run the System Preparation Tool to remove unique id
		Export the VM to a folder on the filesystem
			NOT Install additional software components (optional)


After importing a template, you should rename the VM?
	TRUE

WDS can install multiple physical or virtual systems at once with PXE
	TRUE

Two files import within WDS tool?
	install.wim
	boot.wim