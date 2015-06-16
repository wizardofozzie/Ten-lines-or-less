# See: http://omz-forums.appspot.com/editorial/post/5906215083180032

import dropboxlogin, time

dropbox_client = dropboxlogin.get_client()

def dropbox_change_watcher(file_path, seconds_to_sleep=2):
    original_revision = new_revision = dropbox_client.metadata(file_path)['revision']
    while True:
        metadata = dropbox_client.metadata(file_path)
        if metadata['revision'] == original_revision:
            time.sleep(seconds_to_sleep)
        else:
            return metadata

if __name__ == '__main__':
    import os, pprint
    file_path_to_watch = os.path.split(__file__)[1]  # just for testing/debug
    print(file_path_to_watch)
    pprint.pprint(dropbox_change_watcher(file_path_to_watch))
    print('Done.')