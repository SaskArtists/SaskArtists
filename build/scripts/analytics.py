import sys

head = False

CODE = """
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-50411886-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-50411886-2');
</script>
"""

for line in sys.stdin:
    print line,
    if "<head" in line:
        print CODE.strip(),
