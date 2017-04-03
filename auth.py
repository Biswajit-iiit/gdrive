from oauth2client import client
import webbrowser
import httplib2
from apiclient import discovery
from apiclient.discovery import build
import creds as creds

flow = client.flow_from_clientsecrets(
    creds.client_secrets_json,
    scope='https://www.googleapis.com/auth/drive.readonly',
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

auth_uri = flow.step1_get_authorize_url()
webbrowser.open_new(auth_uri)

auth_code = raw_input()
credentials = flow.step2_exchange(auth_code)
http_auth = credentials.authorize(httplib2.Http())


drive_service = build('drive', 'v2', http=http_auth)
files = drive_service.files().list().execute()
for f in files['items']:
	print f['title']