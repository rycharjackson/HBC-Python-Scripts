from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io


class drive:

    def __init__(self, service):
        self.service = service

    def list_files(self, size):
        # Call the Drive v3 API
        results = self.service.files().list(pageSize=size, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

    def upload_file(self, file_name, file_path, mimetype):
        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_path, mimetype=mimetype)
        myfile = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('File ID: %s' % myfile.get('id'))

    def download_app_file(self, file_id, file_path, mimeType):
        request = self.service.files().export_media(fileId=file_id, mimeType=mimeType)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        with io.open(file_path, "wb") as f:
            fh.seek(0)
            f.write(fh.read())

    def search_files(self, size, query):
        results = self.service.files().list(pageSize=size, fields="nextPageToken, files(id, name, kind, mimeType)",
                                       q="name contains '{0}'".format(query)).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            for item in items:
                return item
                # print(item)
                # print(u'<{0}> ({1}) [{2}]'.format(item['name'], item['id'], item['kind']))


