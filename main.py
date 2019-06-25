from urllib.parse import parse_qs, urlparse

from api_google import export_file
from send_mail import send
from utils import load_json

EX_FILEID = '16eVwhW4mUep2VL35OvGBSchna9FS1BNqafslxQYOabQ'

CONTENT = ''
PATTERN = "https://www.google.com/url?q="


def find_full(pos):
    global CONTENT
    end = CONTENT.find("\"", pos)
    url = CONTENT[pos:end]
    urlp = urlparse(url)
    href = parse_qs(urlp.query)['q'][0]
    CONTENT = CONTENT.replace(url, href, 1)
    return len(href)


def format():
    global PATTERN
    pos = 0
    while True:
        pos = CONTENT.find(PATTERN, pos)
        if pos == -1:
            break
        # print(pos)
        add_pos = find_full(pos)
        pos += add_pos


if __name__ == "__main__":
    content_email_config = load_json('content.json')
    CONTENT = export_file(content_email_config['file_id']).decode("utf-8")
    format()
    send(CONTENT, content_email_config['subject'])
    print('Done!')
