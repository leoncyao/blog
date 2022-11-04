sh scripts/open_browser.sh &
# bundle exec jekyll serve --drafts &
rm -r _site
bundle exec jekyll serve --drafts --incremental