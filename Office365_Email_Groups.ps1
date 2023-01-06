##### Must be connected to Office365 through Powershell for this to work ####

$User = Read-Host "Enter user email to check memberships: "
$Filepath = Read-Host "Enter location to save file using UNC paths: "
$Mailbox = get-mailbox $User
$DN = $Mailbox.DistinguishedName
$Filter = "Members -like ""$DN"""
Get-DistributionGroup -ResultSize Unlimited -Filter $Filter | Out-File -filepath $Filepath
