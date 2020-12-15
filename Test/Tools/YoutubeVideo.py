try:
    from Tools.Utilities import *;
    from pytube import YouTube;
    from pytube import Playlist;
except Exception as ex:
        print('Missing modules: {0}'.format(ex.args));

class YoutubeVideo:

    def __init__(self, url, progress_callback=None, complete_callback=None):
        self.youtube = YouTube(url, on_progress_callback=self.on_progress_callback, on_complete_callback=self.on_complete_callback);
        self.title = format_title(self.youtube.title) if contains_invalid_chars(self.youtube.title) else self.youtube.title;
        self.progress_callback = progress_callback;
        self.complete_callback = complete_callback;

    def on_progress_callback(self, stream = None, chunk = None, file_handle = None, bytes_remaining = None):
        file_size = stream.filesize;
        remaining = file_size - file_handle;

        if self.progress_callback != None:
            self.progress_callback(self, file_size, remaining);
            pass;
        pass;
    
    def on_complete_callback(self, stream, file_handle):
        if self.complete_callback != None:
            self.complete_callback(self, file_handle);
            pass;
        pass;
       
    def download(self):
        video_stream = self.youtube.streams.filter().first();

        if (video_stream != None):
            return video_stream.download(filename=self.title);
        else:
            return None;