import requests

def call_http_get():
  r = requests.get('https://api.github.com/events')
  print(r.json())


def main():
  print "hello world"
  call_http_get()

if __name__ == '__main__':
  main()