**Servers**
client - pc connecting to shared resources
server - computer sharing that resource

2018 - 80% of all servers in organizations
mostly rackmount
	most have one or more SAN storage area network
		HD or SSD
	one more more UPS uninterruptible power supply
	minimum height is 1.75 - 1U, 2 HD and 2 processors
		2U - 4 processors and 8 HD
		SAN is often 4U or more
## **Virtualization** 
- running more than one OS on single machine
	hypervisor
		Type2 - on top of existing OS - host operating system
			*guest operating systems* or *virtual machines*
			good for testing and dev
		Type 1 - more efficient - interacts with hardware directly
			Hyper-V, ESXi and Linux KVM
		require hypervisor acceleration - Intel VT or AMD-V
		also most require SLAT, second level address translation
	virtual hard disk file, plus small configuration file
		thick provisioning - all space allocated
		thin provisioning - dynamically allocated
		Hyper-V .vhdx
		VMWare .vmdk
		VirtualBox .vdi
		KVM .qcow2 or none
	Most systems are VMs on 1U servers plus SAN or cloud data
Hyper-V allows nested virtualization
	install Windows server Hyper-V on Windows 10, then VMs on that
	powershell command to enable nesting -ExposeVirtualizationExtensions

Containers
	subset of an OS with apps and needed system files just for those apps
	apps isolated from others in other containers, and from underlying OS
	each gets its own name and IP address
	less resources than VMs so good for cloud environments
	Docker
		underlying component that lets you use it is Windows Containers
	no kernel, but the underlying kernel can get overloaded
		Hyper-V Containers can provide a separate copy of the kernel to each container
		
## **Windows Server**
**Active Directory**
workgroup - logical grouping of computers on the network
	peer-to-peer networking: each computer has its own shared resources, users, groups, and security
	authentication - must have valid username and password on that machine
Domain - logical grouping that authenticate to central database of users
	*domain controllers* - special servers
	authentication on the domain controller - *single sign-on*
	token then follows the user around the network
Active Directory
	single sign-on
	when you join a domain, Domain Admin accounts have access to your computer
	they configure and apply *Group Policy*
	*Active Directory Certification Services* - auto deployment of encryption certs
Azure Active Directory - AD via Azure cloud

**Security**
WS2019 security on by default
Microsoft Defender
*Advanced Threat Protection ATP* - suspicious processes are inspected by Azure servers
BitLocker - encryption of virtual HD files
	*shielded virtual machines* can run Windows or Linux now
*Internet Information Services IIS* web server
file and folder permissions
event auditing
server management and monitoring

**Volume and Filesystem Features**
NTFS and ReFS (Resilient File System)
NTFS supports
	Encrypting File System EFS
	data deduplication (duplicate files stored only once)
	journaling - tracks changes to files
	self-healing - heal area of damaged disk with "worker thread"
	file system cache good for virtualization
		hyper-v dynamically allocates
ReFS, still in dev
	good for use in Storage Spaces - large fault-tolerant volumes spanned
	Storage Replicas - replicate data between 2 servers
	Storage Migration Service, good for moving data incl to Azure

**Performance and Reliability**
Privileged Mode and Protected Processes
	Windows kernel runs in privileged mode
	protected processes cannot be accessed by other user or process
Multitasking and Multithreading
	ability to run 2 or more programs at once
	multithreading - programs to run several code blocks (threads) at once
	preemptive multitasking - each program runs in its own memory area
		not the old cooperative, where programs shared memory spaces
Processor Scalability
	Physical Processor - plugged into processor socket
		windows server supports up to 64 sockets
	One processor can have multiple logical processors (*cores*)
		supports unlimited logical processors
	Virtual Processors - logical processors used in VM
Server Clustering
	two or more servers appear as one
	speed and fault tolerance
	failover - one responds if the other is down
	mission critical services, eg databases
	hyper-v machines can work in a cluster
	*Storage Spaces Direct* disks on different servers available to users

**Administration Tools**
Server Manager
	centrally manage servers on the network
	configuration, roles, security, RDP, storage, AD
Most configuration still done by *Microsoft Management Console MMC* snap-in
	eg, Group Policy Management MMC snap-in tool

Windows Powershell
	2006, compete with Unix shells
	*cmdlets* commands - action/object structure
	eg Get-WmiObject gets info from Windows Management Instrumentation
	run as admin
	configuration, installation, managing services, restarting machines, AD
Windows Admin Center
	extra download
	web-based 
	updates, resource info, certificates, storage, software, registry edits, VMs, clusters, Azure integration
	access to Powershell and RDP connections

**Small Footprint Installation Options**
smaller attack surface
fewer resources
can be in a VM, good for cloud
Two otions
	Server Core - most of the guts but no GUI
		boots into CMD, can start Powershell or DOS commands
		Server Core App Compatibility Feature on Demand FOD
			gives access to graphical tools in .NET framework
	Nano Server
		less than 500MB
		Four options:
			DNS, DHCP, Web, File server

**Hybrid Cloud Features**
Windows Server Azure Network Adapter
	connect local server to cloud servers
Azure Backup
Azure Update Management
Azure Site Recovery
Also now support for Kubernetes - coordination of local and cloud containers

**Linux Application Support**
Windows Subsystem for Linux WSL
	Linux kernel interface for Linux apps on top of Windows kernel
	can run Linux containers on Server 2019

## Windows Server 2019 editions

**Essentials Edition**
max 2 processor sockets, 64GB RAM, 50 remote connections
can be a VM
small businesses
	user groups for O365
	backups and restores for each user
	file space quotas
	Server Health Reports
	dashboard for mobile devices
	BranchCache file sharing, data access to other servers

![[CleanShot 2024-01-11 at 09.29.43@2x.jpg]]

**Standard Edition**
file and print services
secure internet
centralized management of users and resources
Windows Defender
easier config
Desired State Configuration via templates
Storage Tiers and Storage Pinning to put high demand data on fastest server
up to 2 Hyper-V vms
unlimited containers

**Datacenter edition**
large databases, virtualization and cloud, HA
unlimited VMs
Sofware Defined Networking SDN features

**Windows Storage Server**
OEM softare on storage products

**Hyper-V Server**
powershell interface
free to use, but each VM must have a valid license

## Preparing for installation

UEFI and TPM
512MB (2GB with GUI), 800MB per VM
32GB for core, 36GB with gui

*capacity planning*
roles, VMs, users, support, redundancy, growth
no of processors and memory for scalability
RAID
SAN?

## Installing
ISO
burn with Burnaware or Rufus

choose edition
custom installation with new server

install on whole drive or partition manually

## Post-installation
time and zone
	time must match within 5 minutes to work with the domain
	user Server Manager to set
IP network setup
	3 protocols: TCP, UDP, ICMP
	IP Internet Protocol address IPv4 IPv6
	IPv4
		IP address
		default gateway
		subnet mask
		unicast - communication from one machine to another using IP
		4 octets - network ID and host ID
		machines with same network ID can communicate
		loopback IP address, localhost
		ANDing - 1 only if both are 1
		.255 is the broadcast address
		connect to another network with a router - IP is default gateway
	IPv6
		8 16-bit hexadecimal numbers
		loopback is ::1
		first half is network id (46 bits for ISP, 16 for local)
		second half is LAN
		slow adoption because of proxy servers and NAT routers
	Media Access Control MAC - hardware address
Configuring IP
	DHCP dynamic host configuration protocol
	BOOTP Boot Protocol	
	DNS domain name service address resolve IPs to FQDN
		Automatic Private IP Addressing APIPA 169.254.x.x
		IPv6 APIPA is FE80
	Server Manager -> Local Server -> interface -> properties

firewall
Perimeter network, DMZ - firewalls on both sides of the server
	these servers don't need an internal firewall

default name and domain
	up to 63 characters; first part of FQDN, and NetBIOS name for broadcast
	(NetBIOS names can only be 15 characters; no special characters or spaces)
	Server Manager -> Local Server -> Computer Name in System Properties
	need to add new server to the AD domain
		default is to add it to peer-to-peer WORKGROUP
		Server Manager -> Local Server -> Workgroup
			select Domain radio buttong, add domain name of AD
			login as valid user within the domain

browser install
	Edge Chromium Chrome
	disable IE ESC (IE Enhanced Security) to permit the download
	Server Manager -> Local Server -> IE ESC -> disable
	
activation
	KMS Key management services
	AD-based Activation Role on a domain controller
		automatic activation with GVLK generic volume license key
	retail product key or MAK Multiple Activation Key
	Server Manager -> Local Server -> ProductID -> Activate
## Lab environment
Use Hyper-V on Win10, Server 2019 VM


## Review 

On-premises vs cloud servers

hardware reqs for Hyper-V
	processor with IntelVT or AMD-V and SLAT

nested virtualization
	install a vm inside another vm

Containers are often used to host web apps within cloud environments

Logical grouping of computers that participate in AD single-sign-on
	Domain

which component of Defender provides cloud-based threat analysis
	ATP Advanced Threat Protection

WS2019 supports up to 64 physical processors and 128 logical processors
	FALSE - unlimited logical

feature - create large volumes that span multiple physical storage devices
	Storage Spaces

Clustering - speed and fault tolerance
	TRUE

management tool that is not installed by default
	Windows Admin Center

Powershell commands are cmdlets
	TRUE

Two small-footprint options
	Server Core
	Nano Server


Start Windows Server Configuration Wizard: sconfig.cmd
	TRUE

Edition that supports Containers, and 2 Hyper-V machines
	Standard

Minimum memory for a graphical installation is 512MB
	FALSE - GUI requires 2GB

Which are licensed per processor core
	Standard
	Datacenter

Question you don't ask when installing WS2019
	Who will be supporting the server

To install as a VM, attach ISO image to virtual DVD drive
	TRUE

Steps after installation
	time and time zone
	activate
	name and domain membership
	ip configuration

Server Manager is typically used to perform post-install tasks
	TRUE

192.168.100.0 is in private network range
	TRUE

What is a domain, and how does it affect computers and users that are members of the domain
	A domain is a logical grouping of computers that authenticate to a central database of users stored on special servers called domain controllers. When users log into a computer that is joined to a domain, their user names and passwords are authenticated on the nearest domain controller, which maintains a central database of users and passwords on the network. Once authenticated, the user receives a token from the domain controller that follows them around the network and automatically proves their identity to other domain-joined servers and clients. Those servers and clients will then allow the user to access resources that specifically grant them access. Because users only need to authenticate once to a domain controller to prove their identity to all domain members, this feature is called single sign-on.