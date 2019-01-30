import bs4, os

for root, dirs, filenames in os.walk('www/'):
    for filename in filenames:
        if filename.split('.')[-1] in ['html', 'htm']:
            file = os.path.join(root, filename)
            with open(file, encoding="utf-8") as inf:
                txt = inf.read()
                soup = bs4.BeautifulSoup(txt, "html.parser")
    
            gtag = soup.new_tag("script", src="https://www.googletagmanager.com/gtag/js?id=UA-129512949-1")
            gtag.attrs['async'] = None
            soup.head.append(gtag)
            gtag = soup.new_tag("script")
            gtag.string = "window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'UA-129512949-1');"
            soup.head.append(gtag)
    
            with open(file, "w") as outf:
              outf.write(str(soup))
