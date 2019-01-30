import bs4, os

for root, dirs, filename in os.walk('www/'):
    if filename.endswith('.html'):
        file = os.path.join(root, filename)
        with open(file) as inf:
            txt = inf.read()
            soup = bs4.BeautifulSoup(txt)
    
        gtag = soup.new_tag("script", async="true", src="https://www.googletagmanager.com/gtag/js?id=UA-129512949-1")
        gtag.head.append(gtag)
        gtag = soup.new_tag("script")
        gtag.string = "window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'UA-129512949-1');"
        soup.head.append(gtag)
    
        with open(file, "w") as outf:
          outf.write(str(soup))
