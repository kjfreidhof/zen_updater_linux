import wget 

def main():
     browser_url = "https://github.com/zen-browser/desktop/releases/download/1.0.2-b.5/zen.linux-x86_64.tar.bz2"
    # browser_url = "https://github.com/zen-browser/desktop/releases/download/1.0.2-b.3/zen.linux-specific.tar.bz2"
     file = wget.download(browser_url)

main()


