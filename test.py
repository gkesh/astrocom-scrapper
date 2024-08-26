from engine.operations import download
from dotenv import load_dotenv


load_dotenv()

def test_download():
    """
    Testing the download functionality
    """
    source = 'https://kissmanga.in/kissmanga/tales-of-demons-and-gods-kiss-manga-free/'
    comic = 'tales'
    crawler = 'kissmanga'

    download(
        comic,
        source,
        crawler
    )


if __name__ == '__main__':
    test_download()