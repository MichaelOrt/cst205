from urllib.request import Request, urlopen

# Use the web page you chose here:
my_site = "https://thespaces.com/"
req = Request(my_site, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req)

# Print out a portion of the HTML
print(html.read()[50_000:50_100]) 