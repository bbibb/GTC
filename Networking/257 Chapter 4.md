




## Review

Domain controllers store local user accounts within a SAM database and domain user accounts within Active Directory. True or False?
	FALSE

Which of the following occurs when you join a computer to an Active Directory domain? (Choose all that apply.)
	- The Domain Users group is added to the local Users group
	- A computer account is created within Active Directory, if one has not been prestaged
	- The Domain Admins group is added to the local Administrators group

You can use the Install-ADDSDomain cmdlet within Windows PowerShell to configure a new forest root domain. True or False?
	FALSE

Which of the following trust relationships can be created between two domains in separate Active Directory forests?
	External Trusts

Which of the following group scopes can contain objects from any domain within the forest? (Choose all that apply.)
	- Domain local
	- Universal

You must be a member of the Enterprise Admins group in order to add a trust relationship. True or False?
	TRUE

Which of the following domain functional levels provides Kerberos armoring? (Choose all that apply.)
	- Windows Server 2012
	- Windows Server 2012 R2
	- Windows Server 2016

The schema and configuration partitions of the Active Directory database are replicated forest-wide. True or False?
	TRUE

Your domain consists of two separate physical locations. Each location contains several domain controllers, and you have noticed that domain controller replication traffic consumes a large amount of your Internet bandwidth. What can you do within Active Directory Sites and Services to ensure that replication occurs outside of business hours? (Choose all that apply.)
	- Create a site object for each physical location and ensure that domain controller objects are placed within the correct site object.
	-   In the properties of a site link object, configure a replication schedule that excludes business hours.

Which functions does the global catalog provide? (Choose all that apply.)
	- Fast object searching
	- Universal group membership
	- Domain authentication using UPNs

If a global catalog cannot be placed within a branch office site, you can enable UGMC on the site to ensure branch office domain controllers provide fast authentication. True or False?
	TRUE

Which of the following FSMO roles are stored on one domain controller within each domain? (Choose all that apply.)
	- PDC Emulator
	- RID Master


Before installing Active Directory on a Windows Server system to function as an additional domain controller within a forest, you must first ensure that the Windows Server is configured to contact a DNS server that contains the appropriate service records for the forest. True or False?
	TRUE

You have created a template user account within Active Directory Users and Computers. What must you do to create additional user accounts based on this template user account?
	Right-click the template user account, and click Copy

You wish to add a copy of the global catalog to a domain controller within Active Directory Sites and Services. For which object must you right-click and select Properties?
	NTDS Settings

The Active Directory Recycle Bin can be enabled using the Active Directory Domains and Trusts tool. True or False?
	FALSE

Which default folder under a domain within Active Directory Users and Computers contains the Administrator user account and Domain Admins group?
	Users

Which of the following PowerShell cmdlets can be used to move or seize a FSMO role?
	Move-ADDirectoryServerOperationMasterRole

Creating OUs within the Active Directory database is also called prestaging. True or False?
	FALSE

If a RODC is stolen, you can delete the computer account to reset affected user and computer accounts. True or False?
	TRUE


