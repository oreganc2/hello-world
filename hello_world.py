
import requests



def call_http_get():
  r = requests.get('https://api.github.com/events')
  print(r.json())


def main():
  print "hello world"
  call_http_get()
  print("Testing123")
  print("Testing123456")

  print("let's see if this works")

if __name__ == '__main__':
  main()