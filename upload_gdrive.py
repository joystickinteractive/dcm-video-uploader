from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/drive"]
gauth = GoogleAuth()
gauth.auth_method = 'service'
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
drive = GoogleDrive(gauth)

about = drive.GetAbout()
print('Current user name:{}'.format(about['name']))
print('Root folder ID:{}'.format(about['rootFolderId']))
print('Total quota (bytes):{}'.format(about['quotaBytesTotal']))
print('Used quota (bytes):{}'.format(about['quotaBytesUsed']))

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': 'trashed=false', 'maxResults': 10}).GetList()
for file1 in file_list:
    print('title: {}, id: {}'.format(file1['title'], file1['id']))

file1 = drive.CreateFile({'title': 'hello.txt', 'parents': [{'id': '1Cz4LakMKZer_Bb_u3fTZ36u1scuzwZb-'}]})
file1.SetContentString('Hello')
file1.Upload()
