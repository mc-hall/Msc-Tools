
#Files saved in User H: drive location
$desktopsource = "\\Corpapps02\Users\$user\_C\Desktop\"
$documentssource = "\\Corpapps02\Users\$user\_C\Documents\"
$favoritessource = "\\Corpapps02\Users\$user\_C\Favorites\"


#Local Desktop destinations
$desktopdestination = "\\$computername\c$\Users\$user\Desktop\"
$documentdestination = "\\$computername\c$\Users\$user\Documents\"
$favoritesdestination = "\\$computername\c$\Users\$user\Favorites\"

#Mapping files source
$localinfo = "\\Corpapps02\Users\$user\_C\*.txt"

$computername = Read-Host 'Enter destination device name: '
$user = Read-Host 'Enter users AD username: '


#Copy Desktop items to local
$deskpath = Test-Path \\corpapps02\users\$user\_C\Desktop
if($deskpath -eq $true){
Write-Host 'Desktop folder exists'
Copy-Item $desktopsource -Destination $desktopdestination -Recurse
}
else {Write-Host 'Desktop folder not present'}



#copy Documents to local
$docpath = Test-Path \\corpapps02\users\$user\_C\Documents
if($docpath -eq $true){
Write-Host 'Documents folder exists'
Copy-Item $documentssource -Destination $documentdestination -Recurse
}
else {Write-Host 'Documents folder not present'}


#Copy IE favorites to local
$favpath = Test-Path \\corpapps02\users\$user\_C\Favorites
if($favpath -eq $true){
Write-Host 'Favorites folder exists'
Copy-Item $favoritessource -Destination $favoritesdestination -Recurse
}
else{Write-Host 'Favorites folder not present'}


#Copy old device info to new local desktop
Get-ChildItem "\\corpapps02\users\$user\_C\*.txt"
Copy-Item $localinfo -Destination $desktopdestination -Recurse












