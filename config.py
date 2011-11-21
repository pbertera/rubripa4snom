import web

iPA4uri = 'http://ipa4.bertera.it'
web.config.debug = False

view = web.template.render('rubripa4snom/views', cache=False)

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}
