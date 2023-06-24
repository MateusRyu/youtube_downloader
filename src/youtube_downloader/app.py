"""
An Youtube downloader
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class YouTubeDownloader(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        search_box = self.construct_search_box()
        preview_box = self.construct_preview_box()
        download_box = self.construct_download_box()

        main_box = toga.Box(
            children=[
                search_box,
                preview_box,
                toga.Divider(),
                download_box
            ],
            style=Pack(direction=COLUMN)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        self.thumb_view.refresh()

    def construct_search_box(self):
        search_button = toga.Button(
            "Search",
            on_press=self.get_stream,
            style=Pack(padding=5)
        )
        self.search_input = toga.TextInput(style=Pack(flex=1))

        search_box = toga.Box(style=Pack(direction=ROW, padding=5))
        search_box.add(search_button)
        search_box.add(self.search_input)

        return search_box
    
    def construct_preview_box(self):
        thumb_scale = .5
        thumb_size = {"width":1280*thumb_scale, "height":720*thumb_scale}
        thumb_image = toga.Image(path="resources/images/thumbnail_placeholder.jpg") # /1280x720
        self.thumb_view = toga.ImageView(
            id='thumb',
            image=thumb_image, 
            style=Pack(width=thumb_size["width"], height=thumb_size["height"])
        )

        stream_title_label = toga.Label("Title: ")
        self.stream_title = toga.Label("")

        title_box = toga.Box(style=Pack(direction=ROW, padding=5))
        title_box.add(stream_title_label)
        title_box.add(self.stream_title)

        stream_author_label = toga.Label("Author: ")
        self.stream_author = toga.Label("")

        author_box = toga.Box(style=Pack(direction=ROW, padding=5))
        author_box.add(stream_author_label)
        author_box.add(self.stream_author)

        stream_length_label = toga.Label("Length: ")
        self.stream_length = toga.Label("")

        length_box = toga.Box(style=Pack(direction=ROW, padding=5))
        length_box.add(stream_length_label)
        length_box.add(self.stream_length)

        preview_box = toga.Box(
            children=[
                self.thumb_view,
                title_box,
                author_box,
                length_box,
            ],
            style=Pack(direction=COLUMN, padding=5)
        )

        return preview_box

    def construct_download_box(self):
        download_mp4_button = toga.Button(
            "Download mp4",
            on_press=self.download_as_mp4,
            style=Pack(padding=5)
        )
        
        download_mp3_button = toga.Button(
            "Download mp3",
            on_press=self.download_as_mp3,
            style=Pack(padding=5)
        )

        download_box = toga.Box(style=Pack(direction=ROW, padding=5))
        download_box.add(download_mp4_button)
        download_box.add(download_mp3_button)

        return download_box

    def get_stream(self, widget):
        print(f"Search link: '{self.search_input.value}'")
        self.stream_title.text = f"Title of link: '{self.search_input.value}'"
        self.stream_author.text = f"Author of link: '{self.search_input.value}'"
        self.stream_length.text = f"Length of link: '{self.search_input.value}'"

    def download_as_mp4(self, widget):
        print(f"Download link '{self.search_input.value}' as mp4")

    def download_as_mp3(self, widget):
        print(f"Download link '{self.search_input.value}' as mp3")

def main():
    return YouTubeDownloader()
