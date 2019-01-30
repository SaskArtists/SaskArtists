import bs4, os

# load the file
for root, dirs, filename in os.walk('www/'):
  if filename.endswith('.html'):
    file = os.path.join(root, filename)
    with open(file) as inf:
      txt = inf.read()
      soup = bs4.BeautifulSoup(txt)
    
    # create new link"link", rel
    new_link = soup.new_tag("script", async="true", src="https://www.googletagmanager.com/gtag/js?id=UA-129512949-1")
    # insert it into the document
    soup.head.append(new_link)
    gtag = soup.new_tag("script")
    gtag.string = "window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'UA-129512949-1');"
    soup.head.append(gtag)
    with open(file, "w") as outf:
      outf.write(str(soup))
